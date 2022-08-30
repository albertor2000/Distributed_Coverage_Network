from genericpath import isfile
from turtle import goto
from agent_interfaces.srv import GetPosition
from sensor_msgs.msg import Range
from px4_msgs.msg import VehicleOdometry

import threading
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import rclpy
from rclpy.node import Node

# Id of this agent
MY_ID = 0

# Coordinates of this agent
mx = 1.0
my = 2.0
mz = 3.0

# Time before a new position calculation
step_delay_time = 3000

# id agent to ask coordinates
destination_id = 2

agents_position = [[-1, -1, 1], [-1, -1, 1], [-1, -1, 1]]

# Area to visit
destination = (.4,.5)

# K-means

SHOW_POINTS_PLOT = False
SHOW_ONLY_POINTS_PLOT = False

N_AGENTS = 3 # Agents
N_FOCUS_POINTS = 1 # Center of gaussian distribution

ITERATIONS_TO_CONVERGE = 3

heightSubscriber = None
rtpositionSubscriber = None

class PositionService(Node):
    global mx, my, mz
    global MY_ID, destination_id

    def __init__(self):
        super().__init__('pos_service_' + str(MY_ID))
        self.srv = self.create_service(GetPosition, 'get_position_' + str(MY_ID), self.add_three_ints_callback)        # CHANGE

    def add_three_ints_callback(self, request, response):

        response.x = mx
        response.y = my
        response.z = mz
        self.get_logger().info('Incoming request\nx: %d y: %d z: %d' % (response.x, response.y, response.z)) # CHANGE

        return response

"""
class PositionClient1Async(Node):
    global MY_ID, destination_id

    def __init__(self):
        super().__init__('pos_client_' + str(MY_ID) + "_" + str(1))
        self.cli = self.create_client(GetPosition, 'get_position_' + str(1))       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for agent ' + str(1))
        self.req = GetPosition.Request()                                   # CHANGE

    def send_request(self):
        print('Request sent at agent ' + str(1))
        self.future = self.cli.call_async(self.req)

class PositionClient2Async(Node):
    global MY_ID, destination_id

    def __init__(self):
        super().__init__('pos_client_' + str(MY_ID) + "_" + str(2))
        self.cli = self.create_client(GetPosition, 'get_position_' + str(2))       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for agent ' + str(2))
        self.req = GetPosition.Request()                                   # CHANGE

    def send_request(self):
        print('Request sent at agent ' + str(2))
        self.future = self.cli.call_async(self.req)
"""

class HeightSubscriber(Node):
    global MY_ID

    def __init__(self):
        super().__init__('ultrasonic_subscriber_' + str(MY_ID +1))
        self.subscription = self.create_subscription(
            Range,
            'ultrasonic_sensor_' + str(MY_ID +1),
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Altitude: %s m' % msg.range)


class RTPositionSubscriber(Node):
    global MY_ID

    def __init__(self):
        super().__init__('rt_position_'+ str(MY_ID))
        self.subscription = self.create_subscription(
            VehicleOdometry,
            '/iris'+str(MY_ID)+'/fmu/vehicle_odometry/out',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Position - x: %s, y: %s, z: %s' % (msg.x, msg.y, msg.z))


class KMeans():
    def __init__(self, K, isGaussian=True, X=None, N=0, AREA_SIZE=1, FOCUS_SIZE=0.15):
        self.K = K
        self.AREA_SIZE = AREA_SIZE
        if X == None:
            if N == 0:
                raise Exception("If no data is provided, \
                                 a parameter N (number of points) is needed")
            else:
                self.N = N
                if isGaussian: self.X = self._init_board_gauss(N, K, AREA_SIZE, FOCUS_SIZE)
                else: self.X = self._init_board(N, AREA_SIZE)
        else:
            self.X = X
            self.N = len(X)
        self.mu = None
        self.clusters = None
        self.method = None
 
    def _init_board(self, N, AREA_SIZE):
        self.c = None
        X = np.array([(random.uniform(0, AREA_SIZE), random.uniform(0, AREA_SIZE)) for i in range(N)])
        return X

    def _init_board_gauss(self, N, k, AREA_SIZE, FOCUS_SIZE):
        global destination

        n = float(N)/k
        X = []
        self.c = []
        for i in range(k):
            #c = (random.uniform(-1,1), random.uniform(-1,1))
            c = destination
            self.c.append(c)
            s = random.uniform(0.2,FOCUS_SIZE)
            x = []
            while len(x) < n:
                a,b = np.array([np.random.normal(c[0],s),np.random.normal(c[1],s)])
                # Continue drawing points from the distribution in the range [-1,1]
                if abs(a) and abs(b)<1:

                    # Transform [-1, 1] limit to [0, AREA_SIZE]
                    a += 1
                    b += 1

                    a *= AREA_SIZE/2
                    b *= AREA_SIZE/2

                    x.append([a,b])
            X.extend(x)
        X = np.array(X)[:N]

        return X
 
    def plot_board(self, drones_pos, step):
        global MY_ID

        GRAPH_OFFSET = 3

        X = self.X
        fig = plt.figure(figsize=(5,5))
        plt.xlim(0-GRAPH_OFFSET,self.AREA_SIZE+GRAPH_OFFSET)
        plt.ylim(0-GRAPH_OFFSET,self.AREA_SIZE+GRAPH_OFFSET)
        if self.mu and self.clusters:
            mu = self.mu
            clus = self.clusters
            K = self.K
            for m, clu in clus.items():
                cs = cm.Spectral(1.*m/self.K)
                plt.plot(mu[m][0], mu[m][1], marker='*', \
                         markersize=12, color=cs)
                plt.plot(drones_pos[MY_ID][0], drones_pos[MY_ID][1], marker='^', \
                         markersize=6, color='red')

                # Plot other agents position
                plt.plot(drones_pos[1][0], drones_pos[1][1], marker='<', \
                         markersize=6, color='green')
                plt.plot(drones_pos[2][0], drones_pos[2][1], marker='<', \
                         markersize=6, color='green')

                plt.plot(list(zip(*clus[m]))[0], list(zip(*clus[m]))[1], '.', \
                         markersize=8, color=cs, alpha=0.5)
        else:
            plt.plot(zip(*X)[0], zip(*X)[1], '.', alpha=0.5)
        if self.method == '++':
            tit = 'K-means++'
        else:
            tit = 'K-means with random initialization'
        pars = 'N=%s, K=%s' % (str(self.N), str(self.K))
        plt.title('\n'.join([pars, tit]), fontsize=16)
        plt.savefig(str(MY_ID) +"-"+ str(step) + 'kpp_N%s_K%s.png' % (str(self.N), str(self.K)), \
                    bbox_inches='tight', dpi=200)

        if SHOW_POINTS_PLOT:
            plt.show()  
    
    def getAgentsDestinations(self):
        if self.mu and self.clusters:
            mu = self.mu
            clus = self.clusters
        
        points = []
        for m, clu in self.clusters.items():
            points.append([mu[m][0], mu[m][1]])

        return points

    def getCenter(self):
        return self.c


    def _cluster_points(self):
        mu = self.mu
        clusters  = {}
        for x in self.X:
            bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                             for i in enumerate(mu)], key=lambda t:t[1])[0]
            try:
                clusters[bestmukey].append(x)
            except KeyError:
                clusters[bestmukey] = [x]
        self.clusters = clusters
 
    def _reevaluate_centers(self):
        clusters = self.clusters
        newmu = []
        keys = sorted(self.clusters.keys())
        for k in keys:
            newmu.append(np.mean(clusters[k], axis = 0))
        self.mu = newmu

        return self.mu
 
    def _has_converged(self):
        K = len(self.oldmu)

        print(set([tuple(a) for a in self.mu]) == \
               set([tuple(a) for a in self.oldmu])\
               and len(set([tuple(a) for a in self.mu])) == K)

        return(set([tuple(a) for a in self.mu]) == \
               set([tuple(a) for a in self.oldmu])\
               and len(set([tuple(a) for a in self.mu])) == K)

    def getStartRandomCenter(self, agents, method='random'):
        # Take some random start position from X points, generated under distribution 

        self.method = method
        X = self.X
        #K = self.K
        K = agents
        self.K = K

        # Transform numpy array to list
        mlist = []
        for i in range(len(X)):
            mlist.append([X[i, 0], X[i, 1]])

        self.oldmu = random.sample(mlist, K)
        if method != '++':
            # Initialize to K random centers
            self.mu = random.sample(mlist, K)

        return self.mu


    def setOtherAgentsPosition(self, agents_pos):

        self.mu = [[agents_pos[0][0], agents_pos[0][1]], 
                    [agents_pos[1][0], agents_pos[1][1]], 
                    [agents_pos[2][0], agents_pos[2][1]]]


    def find_centers(self, drones, step=0, method='random'):
        
        if not self._has_converged():
            self.oldmu = self.mu
            # Assign all points in X to clusters
            self._cluster_points()
            # Reevaluate centers
            self._reevaluate_centers()
            #self._reevaluate_my_center()
            #print("Io sono il robot 0 e devo andare a x:", self.mu[0][0], "y:", self.mu[0][1])

            #5 passi per arrivare alla destinazione
            for t in range (0, 6):
                #print("STEP_" + str(t) + " > ", len(drones))
                """
                for i in range(len(drones)):
                    drones[i][0] = drones[i][0]+(self.mu[i][0] - drones[i][0])/5 * t
                    drones[i][1] = drones[i][1]+(self.mu[i][1] - drones[i][1])/5 * t
                #print(drones[0][0],"+(",self.mu[0][0],"-",drones[0][0],")/5 *", t, "=", drones[0][0]+(self.mu[0][0] - drones[0][0])/5 * t)
                """

                drones[0][0] = drones[0][0]+(self.mu[0][0] - drones[0][0])/5 * t
                drones[0][1] = drones[0][1]+(self.mu[0][1] - drones[0][1])/5 * t

                #print("1.0 1.0 -> ", str(drones[0][0]), str(drones[0][1]), "->", self.mu[0][0], self.mu[0][1])
                
                self.plot_board(drones, str(step)+"_"+str(t))

            #print("---------------")
            #self.plot_board(step)
            step += 1

        else:
            print("Converged!")
        
        #return mlist
        return self.mu

def goToDestination(x, y, z) :
    # TODO Send messages to move robot to the destination

    global MY_ID
    print(str(MY_ID) + "> Going to destination... (x: %s, y: %s, z: %s)" % (str(x), str(y), str(z)))
    time.sleep(1)
    print(str(MY_ID) + "> Destination reached!")

def getOtherAgentsPosition(position_client1, position_client2):
    global agents_position
    global N_AGENTS
    global MY_ID

    clients = [None, position_client1, position_client2]

    for i in range(N_AGENTS):
        if i != MY_ID:

            agent_index = i
            destination_id = agent_index
            clients[i].send_request()

            while rclpy.ok():
                rclpy.spin_once(clients[i])
                if clients[i].future.done():
                    try:
                        response = clients[i].future.result()
                    except Exception as e:
                        clients[i].get_logger().info(
                            'Service call failed %r' % (e,))
                    else:
                        print(
                            
                            "Agent%d position (x: %d, y: %d, z: %d)" % 
                                (agent_index, response.x, response.y, response.z))

                        agents_position[i] = [response.x, response.y, response.z] 

                    break

def getAltitude():
    global heightSubscriber

    rclpy.spin_once(heightSubscriber)

def getRTPosition():
    global rtpositionSubscriber

    rclpy.spin_once(rtpositionSubscriber)


def main(args=None):
    global mx, my, mz

    global MY_ID, destination_id
    destination_id = 2

    global agents_position
    agents_position[MY_ID] = [mx, my, mz]

    global N_FOCUS_POINTS, N_AGENTS
    global ITERATIONS_TO_CONVERGE

    global heightSubscriber, rtpositionSubscriber


    # Create service and client nodes
    rclpy.init(args=args)

    position_service = PositionService()
    #position_client1 = PositionClient1Async()
    #position_client2 = PositionClient2Async()

    heightSubscriber = HeightSubscriber()
    rtpositionSubscriber = RTPositionSubscriber()
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(position_service)
    #executor.add_node(position_client1)
    #executor.add_node(position_client2)
    #executor.add_node(heightSubscriber)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()

    print("Started!")

    getAltitude()
    getRTPosition()

    while(True):
        pass
    # Main program
    # Generate random points with gaussian distribution
    mkm = KMeans(N_FOCUS_POINTS, N=100, isGaussian=True, AREA_SIZE=10, FOCUS_SIZE=.3)

    newPosition = mkm.getStartRandomCenter(N_AGENTS)

    mx, my, mz = newPosition[MY_ID][0], newPosition[MY_ID][1], 1.0

    print("My start random position is (%s, %s, %s)" % (str(newPosition[MY_ID][0]), str(newPosition[MY_ID][1]), str(1)))

    # Go to my position
    agents_position[MY_ID] = [newPosition[MY_ID][0], newPosition[MY_ID][1], 1.0]

    goToDestination(newPosition[0][0], newPosition[0][1], 0)

    old_position = [[1.0,1.0], [1.0,1.0], [1.0,1.0]]
    
    time.sleep(random.randrange(100, 600) / 100)
    
    # Continue until it converge
    for i in range (ITERATIONS_TO_CONVERGE):
        print("\n###### STEP " + str(i +1) + " ######\n")

        getOtherAgentsPosition(position_client1, position_client2)

        print("AGENTS:", agents_position)

        mkm.setOtherAgentsPosition(agents_position) # Set position of agents to kmeans algorithm

        newPosition = mkm.find_centers(drones=old_position, step=i+1)
        
        print("Calculated new destination -> My new position is (%s, %s, %s)" % (str(newPosition[MY_ID][0]), str(newPosition[MY_ID][1]), str(1)))

        old_position = [[agents_position[0][0], agents_position[0][1]], 
                        [agents_position[1][0], agents_position[1][1]], 
                        [agents_position[2][0], agents_position[2][1]]]

        agents_position[MY_ID] = [newPosition[MY_ID][0], newPosition[MY_ID][1], 1.0]
        mx, my, mz = newPosition[MY_ID][0], newPosition[MY_ID][1], 1.0

        goToDestination(newPosition[0][0], newPosition[0][1], 0)
    
    # Waiting if other agents need this agent position
    while True:
        pass
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
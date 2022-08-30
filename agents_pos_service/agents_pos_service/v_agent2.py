import random
import math
import threading
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import matplotlib.cm as cm
from scipy.spatial import Voronoi
from shapely.geometry import Polygon

from agent_interfaces.srv import GetPosition

import rclpy
from rclpy.node import Node

"""
VORONOI
"""

def bounded_voronoi(bnd, pnts):
    """
    A function that calculates and draws bounded Voronoi diagrams.
    """
    pnts2d = []

    for i in range(len(pnts) -1):
        pnts2d.append([pnts[i][0], pnts[i][1]])

    pnts2d = np.array(pnts2d)

    #print("np", len(np.array([[100, 100], [100, -100], [-100, 0]])))


    #Added 3 dummy mother points to make the Voronoi region of all mother points bounded
    gn_pnts = np.concatenate([pnts2d, np.array([[100, 100], [100, -100], [-100, 0]])])
    
    #Voronoi diagram calculation
    vor = Voronoi(gn_pnts)
    
    #Polygon for the area to be divided
    bnd_poly = Polygon(bnd)
    
    #List to store each Voronoi area
    vor_polys = []
    
    #Repeat for non-dummy mother points
    for i in range(len(gn_pnts) - 3):
        
        #Voronoi region that does not consider closed space
        vor_poly = [vor.vertices[v] for v in vor.regions[vor.point_region[i]]]
        #Calculate the intersection of the Voronoi area for the area to be divided
        i_cell = bnd_poly.intersection(Polygon(vor_poly))
        
        #Stores the vertex coordinates of the Voronoi region considering the closed space
        vor_polys.append(list(i_cell.exterior.coords[:-1]))
    
    
    #Drawing a Voronoi diagram
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111)
    
    #Mother point - Agents
    ax.scatter(pnts2d[:,0], pnts2d[:,1])
    
    ax.plot(pnts2d[MY_ID][0], pnts2d[MY_ID][1], marker='^', color='green', markersize=6)

    
    #Voronoi area
    poly_vor = PolyCollection(vor_polys, edgecolor="black",
                              facecolors="None", linewidth = 1.0)
    # Borders
    ax.add_collection(poly_vor)
    
    xmin = np.min(bnd[:,0])
    xmax = np.max(bnd[:,0])
    ymin = np.min(bnd[:,1])
    ymax = np.max(bnd[:,1])
    
    ax.set_xlim(xmin-0.1, xmax+0.1)
    ax.set_ylim(ymin-0.1, ymax+0.1)
    ax.set_aspect('equal')
    
    
    #plt.show()
    
    return vor_polys, ax



""" COLORARE I PUNTI CHE DELIMITANO OGNI REGIONE
import matplotlib.cm as cm
colors = cm.rainbow(np.linspace(0, 1, len(vor_polys)))
a = []
b = []
for iii, zzz in enumerate(colors):
    a = []
    b = []
    for a_tuple in vor_polys[iii]:
        a.append(a_tuple[0])  
        b.append(a_tuple[1])

    plt.scatter(a, b, color=zzz)
"""

"""
GAUSSIAN DISTRIBUTION
"""

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def gaussian_array(xs, mu, sig):
    return [gaussian(x,mu,sig) for x in xs]

def getProbability(m_point, dp, mu, variance) : 
    d = math.sqrt((dp[1]-m_point[1])**2+(dp[0]-m_point[0])**2) # Distance from center
    g = round(gaussian(d, mu, variance), 2) # Gaussian value

    return g


"""
CENTROIDE
"""

def getCentroid(x, y) : # x[1,2,3,4,...], y[1,2,3,4,...]

    m = 0 # Mass (Area of the voronoi area )

    x.append(x[0])
    y.append(y[0])

    # Calculate m
    for i in range (0, len(x) -1):
        m += x[i]*y[i+1] - x[i+1]*y[i]
    m /= 2

    # Cacolulate centroide coordinates
    cx = -1.0
    cy = -1.0

    for i in range (0, len(x) -1):
        cx += (x[i]+x[i+1])*(x[i]*y[i+1]-x[i +1]*y[i])
        cy += (y[i]+y[i+1])*(x[i]*y[i+1]-x[i +1]*y[i])

    cx /= 6*m
    cy /= 6*m

    return [cx, cy, m]

def getPolarMoment(x, y, c): 

    x.append(x[0])
    y.append(y[0])

    cx = c[0]
    cy = c[1]

    sum = 0
    for i in range(len(x) -1):
        sum += (x[i] - cx)*(y[i+1] - cy) - (x[i+1] - cx)*(y[i] - cy)

    return sum/12


"""
GEOMETRY
"""

def getDistance(a, b) : # a[x,y], b[x,y]
    return math.sqrt((a[1]-b[1])**2 + (a[0] - b[0])**2)

def getMiddlePoint(a, b) : #a[x,y], b[x,y]
    x = (a[0]+b[0])/2
    y = (a[1]+b[1])/2
    return [x, y]

def getWeightedMiddlePoint(a, b, tradeOffParameter=1) : #a[x,y], b[x,y]
    # Middle
    xm = (a[0]+b[0])/2
    ym = (a[1]+b[1])/2

    # Attracted to a
    x = (a[0]+xm)/2
    y = (a[1]+ym)/2

    # Attracted to b
    #x = (x+xm)/2
    #y = (y+ym)/2

    return [x, y]

###########################################################

def getAreaParent(centroids, mpoint):
    d = 999999999
    index = -1

    for i, centroide in enumerate(centroids):
        td = getDistance(centroide, mpoint)
        if td < d:
            d = td
            index = i

    
    return centroids[index]

##################### SERVICES ROS #########################

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
        self.get_logger().info('Incoming request\nx: %s y: %s z: %s' % (response.x, response.y, response.z)) # CHANGE

        return response

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
        super().__init__('pos_client_' + str(MY_ID) + "_" + str(0))
        self.cli = self.create_client(GetPosition, 'get_position_' + str(0))       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for agent ' + str(0))
        self.req = GetPosition.Request()                                   # CHANGE

    def send_request(self):
        print('Request sent at agent ' + str(0))
        self.future = self.cli.call_async(self.req)

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

    clients = [position_client2, position_client1, None]

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
                            
                            "Agent%d position (x: %s, y: %s, z: %s)" % 
                                (agent_index, response.x, response.y, response.z))

                        agents_position[i] = [response.x, response.y, response.z] 

                    break

###########################################################

# 1. Avere la mia posizione iniziale
# 2. Chiedere la posizione agli altri agenti
# 3. Calcolare il mio voronoi
# 4. Calcolare centroide pesato con massa
# 5. Andare alla destinazione (centroide pesato)
# 6. Ripetere dal 2.

MY_ID = 2       # Agent id

ITERATIONS = 5 # Iterations of all algorithm 
N_AGENTS = 3    # Agents in this scenario

# DO NOT TOUCH
M_FACTOR = 10   # Multiplicative factor (For voronoi bug)

mx = 1.0
my = 2.0
mz = 3.0

destination = [6, 7]    # Event location

agents_position = [[-1, -1, 1], [-1, -1, 1], [-1, -1, 1]]


def main(args=None):
    global MY_ID, ITERATIONS, N_AGENTS
    global M_FACTOR

    global destination, agents_position
    global mx, my, mz

    # Create service and client nodes
    rclpy.init(args=args)

    position_service = PositionService()
    position_client1 = PositionClient1Async()
    position_client2 = PositionClient2Async()
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(position_service)
    executor.add_node(position_client1)
    executor.add_node(position_client2)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()


    #Voronoi division area
    bnd = np.array([[0, 0], [M_FACTOR, 0], [M_FACTOR, M_FACTOR], [0, M_FACTOR]])




    # 1. Agents start positions
    # TODO: Heuristic position, not generated random
    mPosition = np.random.rand(1, 2)

    mx = mPosition[0, 0]
    my = mPosition[0, 1]
    mz = 1.0

    agents_position[MY_ID] = [mx, my, mz]

    print("My start position is (%s, %s, %s)" % (mx, my, mz))

    time.sleep(random.randrange(0, 500) / 100)  # Random wait to avoid 2 request at same time

    agents_position.append([0, 0, 0])   # Add extra zero element for Voronoi bug

    step = 1
    for step in range(ITERATIONS):
        print("\n###### STEP " + str(step) + " ######\n")
        # 2. Ask other agents positions
        getOtherAgentsPosition(position_client1, position_client2)

        print("agents:", agents_position)

        # 3. Calcolate vornoi region
        vor_polys, ax= bounded_voronoi(bnd, agents_position)

        #Calculate centroids for each agents
        # TODO: Do only for this agent
        #for i, region in enumerate(vor_polys):
        region = vor_polys[MY_ID]
        i = MY_ID

        x = []
        y = []
        for a_tuple in region:
            x.append(a_tuple[0] * M_FACTOR)  
            y.append(a_tuple[1] * M_FACTOR)

        # 4. Calculate weighted centroid
        #print(x, y)
        [t1, t2, mass] = getCentroid(x, y)

        # Weighted centroid
        wc = getWeightedMiddlePoint([t1/M_FACTOR, t2/M_FACTOR], destination)
        #plt.plot([t1/M_FACTOR, destination[0]], [t2/M_FACTOR, destination[1]], color='orange')
        #plt.scatter(wc[0], wc[1], color='orange')

        agents_position[i] = np.array([wc[0], wc[1]])   

        # Show centroids
        #plt.scatter(t1/M_FACTOR, t2/M_FACTOR, color='pink')

        mx = agents_position[MY_ID][0]
        my = agents_position[MY_ID][1]

        # 5. Go to the destination (my centroid)    
        goToDestination(wc[0], wc[1], 1.0)

        #plt.scatter(destination[0], destination[1], c='green')

        #if(step == ITERATIONS -1):
        if True:
            for i in range(4):
                ax.add_patch(plt.Circle([destination[0], destination[1]], i/2, color=[0,.7,0,.2]))


            plt.savefig(str(MY_ID) + "_step" + str(step))
            print("Step", str(step/ITERATIONS*100) + "%> Saved!")

    #if step % 19 == 0:
    #plt.savefig("step" + str(step) + ".png")
        
    # Waiting if other agents need this agent position
    while True:
        pass
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()

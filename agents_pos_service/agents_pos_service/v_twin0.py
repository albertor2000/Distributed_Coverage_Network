#!/usr/bin/env python3
"""! @brief Python node that do Coverage Control for Mobile Sensing Networks """


##
# @mainpage Agent0 node

##
# @file v_twin0.py
#
# @section author Author(s)
# - Created by Alberto Ruaro on 30/04/2022.


# Imports
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
from sensor_msgs.msg import Range
from px4_msgs.msg import VehicleOdometry
from interfaces.msg import Posmsg

import rclpy
from rclpy.node import Node


# Global Constants
## Subscriber to receive the height of the aget by ultrasonic sensor topic.
heightSubscriber = None
## Subscriber to get the position of the agent 0 from gazebo.
rtpositionSubscriber = None
## Subscriber to get the position of the agent 1 from gazebo.
rtposition1Subscriber = None
## Publisher to send the coordinates of the calculated position to robots_contol.
coordinatesPublisher = None

## x destination coordinate to send with coordinatesPublisher to robots_control.
dest_x = 5.0
## y destination coordinate to send with coordinatesPublisher to robots_control.
dest_y = 10.0
## z destination coordinate to send with coordinatesPublisher to robots_control.
dest_z = -30.0

## The time to wait to calculate the new position with Lloyd algorithm.
REFRESH_TIME = 5 # seconds
## Distance the agent have to maintain from the terrain.
DISTANCE_FROM_TERRAIN = 20 # meters

## The size of the map. This variable is use to convert coordinates from voronoi (0 to 10) to
# the map (0 to MAP_SIZE)
MAP_SIZE = 2400

## This agent position x coordinate (voronoi scale)
mx = 1.0
## This agent position y coordinate (voronoi scale)
my = 2.0
## This agent position z coordinate (voronoi scale)
mz = 3.0
## Altitude of this agent
mh = 4.0 # Altitude


## This agent position z coordinate (map scale)
sendx = (mx * MAP_SIZE / 10) - (MAP_SIZE / 2)
## This agent position z coordinate (map scale)
sendy = (my * MAP_SIZE / 10) - (MAP_SIZE / 2)
## This agent position z coordinate (map scale)
sendz = mz

## This agent id
MY_ID = 0

## Iterations to converge before take the photo
ITERATIONS = 5
## Number of agents used
N_AGENTS = 2

## DO NOT TOUCH: Multiplicative factor (Used to calculate voronoi cells)
M_FACTOR = 10

## Destination where my agents has to arrive
destination = [6, 7]

## Position of all agents
agents_position = [[-1, -1, 1], [-1, -1, 1]]


"""
VORONOI
"""

def bounded_voronoi(bnd, pnts):
    """! A function that calculates and draws bounded Voronoi diagrams.

    @param bnd  The bounded of the space.
    @param pnts Agents positions.
    """

    pnts2d = []

    for i in range(len(pnts) -1):
        pnts2d.append([pnts[i][0], pnts[i][1]])

    pnts2d = np.array(pnts2d)


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


"""
CENTROIDE
"""

def getCentroid(x, y) : # x[1,2,3,4,...], y[1,2,3,4,...]
    """! Calculates the centroid point of the cell passed by parameters.

    @param x    The array of x coordinates of all points that delimitates the region.
    @param y    The array of x coordinates of all points that delimitates the region.

    @return     The (x, y) coordinates of the centroid.
    """

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
    """! Calculates the polar moment of the cell passed by parameters.

    @param x    The array of x coordinates of all points that delimitates the region.
    @param y    The array of x coordinates of all points that delimitates the region.
    @param c    The c value.

    @return     The value of polar moment of the regior.
    """ 

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
    """! Calculates the distance between two points.

    @param a    The first point [x, y].
    @param b    The second point [x, y].

    @return     The value of the distance between the two given points.
    """ 

    return math.sqrt((a[1]-b[1])**2 + (a[0] - b[0])**2)

def getMiddlePoint(a, b) : #a[x,y], b[x,y]
    """! Calculates the middle point of two points.

    @param a    The first point [x, y].
    @param b    The second point [x, y].

    @return     The value of the middle point of the two given points.
    """ 

    x = (a[0]+b[0])/2
    y = (a[1]+b[1])/2
    return [x, y]

def getWeightedMiddlePoint(a, b) : #a[x,y], b[x,y]
    """! Calculates the middle point nearer to a, between two points.

    @param a    The first point [x, y].
    @param b    The second point [x, y].

    @return     The value of the weighted middle point the two given points.
    """ 

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


##################### SERVICES ROS #########################

def voronoiToMap(coordinate10):
    """! Convert voronoi scale point to map scale point.

    @param coordinate10     The coordinate in voronoi scale.

    @return     The coordinate in map scale.
    """ 

    return (coordinate10 * MAP_SIZE / 10) - MAP_SIZE/2

def MapToVoronoi(coordinateMap):
    """! Convert map scale point to voronoi scale point.

    @param coordinateMap     The coordinate in map scale.

    @return     The coordinate in voronoi scale.
    """

    return (coordinateMap + MAP_SIZE/2) * 10 / MAP_SIZE
    

class HeightSubscriber(Node):
    """! The Height Subscriber class.

    Defines the subscriber class utilized to get the altitude of the agent,
    using the ultrasonic sensor.
    """

    global MY_ID
    global mh

    def __init__(self):
        """! The Height Subscriber class initializer.
        """

        super().__init__('ultrasonic_subscriber_' + str(MY_ID +1))
        self.subscription = self.create_subscription(
            Range,
            'ultrasonic_sensor_' + str(MY_ID +1),
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        """! Callback function to get the message and save the information.

        @param msg     The message cointains the height, received by the sensor.
        """

        global mh

        #self.get_logger().info('Altitude: %s m' % msg.range)
        mh = msg.range


class RTPositionSubscriber(Node):
    """! The Real Time Position Subscriber class.

    Defines the subscriber class utilized to get the position of the agent 0.
    """

    global MY_ID
    global mx, my, mz
    global sendx, sendy, sendz
    global agents_position


    def __init__(self):
        """! The Real Time Position Subscriber class initializer.
        """

        super().__init__('rt_position_'+ str(MY_ID))
        self.subscription = self.create_subscription(
            VehicleOdometry,
            '/iris'+str(MY_ID)+'/fmu/vehicle_odometry/out',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        """! Callback function to get the message and save the position.

        @param msg     The message cointains the x, y, z coordinates, received by the topic.
        """

        global mx, my, mz
        global sendx, sendy, sendz

        #self.get_logger().info('Position - x: %s, y: %s, z: %s' % (msg.x, msg.y, msg.z))
        sendx = msg.x
        sendy = msg.y
        sendz = msg.z

        agents_position[0] = [MapToVoronoi(msg.x), MapToVoronoi(msg.y), msg.z]

        mx = MapToVoronoi(sendx)
        my = MapToVoronoi(sendy)
        mz = sendz

class RTPosition1Subscriber(Node):
    """! The Real Time Position Subscriber class.

    Defines the subscriber class utilized to get the position of the agent 1.
    """

    global MY_ID
    global mx, my, mz
    global sendx, sendy, sendz
    global agents_position

    def __init__(self):
        """! The Real Time Position Subscriber class initializer.
        """

        super().__init__('rt_position_'+ str(1))
        self.subscription = self.create_subscription(
            VehicleOdometry,
            '/iris'+str(1)+'/fmu/vehicle_odometry/out',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        """! Callback function to get the message and save the position.

        @param msg     The message cointains the x, y, z coordinates, received by the topic.
        """

        global mx, my, mz
        global sendx, sendy, sendz

        #self.get_logger().info('Position - x: %s, y: %s, z: %s' % (msg.x, msg.y, msg.z))

        agents_position[1] = [MapToVoronoi(msg.x), MapToVoronoi(msg.y), msg.z]


class CoordinatesPublisher(Node):
    """! The Coordinates Publisher class.

    Defines the publisher class utilized to send the new position to robots_control.
    """

    global MY_ID
    global dest_x, dest_y, dest_z

    def __init__(self):
        """! The Coordinates Publisher class initializer.
        """

        super().__init__('coordinates_publisher_'+str(MY_ID))

        self.publisher_ = self.create_publisher(Posmsg, 'iris'+str(MY_ID)+"/pos", 10)
        #timer_period = 5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0

    def send_coordinates(self):
        """! Function to send the coordinates to robots_control.
        """

        msg = Posmsg()
        msg.agent_id = 0
        msg.x = dest_x
        msg.y = dest_y
        msg.z = dest_z
        self.publisher_.publish(msg)
        #self.get_logger().info('%s> %s, %s, %s' % (msg.agent_id, msg.x, msg.y, msg.z))


def goToDestination(x, y, z) :
    """! The Coordinates Publisher class.

    @param x    The x coordinate of the destination to arrive.
    @param y    The y coordinate of the destination to arrive.
    @param z    The z coordinate of the destination to arrive.

    Defines the publisher class utilized to send the new position to robots_control.
    """

    global MY_ID, REFRESH_TIME, DISTANCE_FROM_TERRAIN
    global dest_x, dest_y, dest_z
    global sendx, sendy, sendz
    global mh
    
    global coordinatesPublisher

    sendx = voronoiToMap(x)
    sendy = voronoiToMap(y)
    #sendz = -25.0 # TODO: Change with altitude
    print("-----\n",DISTANCE_FROM_TERRAIN, "-", mh, "/2", "+", -sendz, "=", -DISTANCE_FROM_TERRAIN - mh/2 + sendz,"\n------")
    sendz = -(DISTANCE_FROM_TERRAIN + mh/2)

    #print(str(MY_ID) + "> Going to destination (voronoi coordinates)... (x: %s, y: %s, z: %s)" % (str(x), str(y), str(z)))
    print(str(MY_ID) + "> Going to destination... (x: %s, y: %s, z: %s)" % (str(sendx), str(sendy), str(sendz)))
    dest_x = sendx
    dest_y = sendy
    dest_z = sendz
    coordinates_publisher.send_coordinates() #TODO uncomment this line to move the robot on gazebo

    time.sleep(REFRESH_TIME)

    print(str(MY_ID) + "> Destination reached!")

###########################################################

def getAltitude():
    """! Function to call the service to get the altitude of the agent.
    """

    global heightSubscriber

    rclpy.spin_once(heightSubscriber)

def getRTPosition(drone_id):
    """! Function to call the service to get the real time position of the agent.

    @param drone_id     The drone id of which get the position
    """

    global rtpositionSubscriber, rtposition1Subscriber

    rtp_subscribers = [rtpositionSubscriber, rtposition1Subscriber]

    print("-> ASK POSITION...", drone_id)
    rclpy.spin_once(rtp_subscribers[drone_id])

    time.sleep(2)

    print("-> POSITION GETTED!", drone_id)

def main(args=None):
    """! Main program entry."""

    global MY_ID, ITERATIONS, N_AGENTS
    global M_FACTOR

    global destination, agents_position
    global mx, my, mz

    global heightSubscriber, rtpositionSubscriber, rtposition1Subscriber, coordinates_publisher
    global dest_x, dest_y, dest_z

    global REFRESH_TIME

    # Create service and client nodes
    rclpy.init(args=args)

    heightSubscriber = HeightSubscriber()
    rtpositionSubscriber = RTPositionSubscriber()
    rtposition1Subscriber = RTPosition1Subscriber()
    coordinates_publisher = CoordinatesPublisher()

    print("Started!")

    time.sleep(5)

    getAltitude()
    getRTPosition(MY_ID)

    time.sleep(2)
    #Voronoi division area
    bnd = np.array([[0, 0], [M_FACTOR, 0], [M_FACTOR, M_FACTOR], [0, M_FACTOR]])

    # 1. Agents start positions

    agents_position[MY_ID] = [mx, my, mz]

    print("My start position is (%s, %s, %s)" % (mx, my, mz))
    print("My start map position is (%s, %s, %s)" % (sendx, sendy, sendz))

    time.sleep(random.randrange(0, 500) / 100)  # Random wait to avoid 2 request at same time

    agents_position.append([0, 0, 0])   # Add extra zero element for Voronoi bug

    step = None
    for step in range(ITERATIONS):
        print("\n###### STEP " + str(step) + " ######\n")

        getAltitude()
        print("Altitude: ", mh)

        getRTPosition(0)
        agents_position[MY_ID] = [mx, my, mz]

        
        # 2. Ask other agents positions
        getRTPosition(1)
        print("agents:", agents_position)

        
        # 3. Calculate vornoi region
        vor_polys, ax= bounded_voronoi(bnd, agents_position)

        #Calculate centroids for each agents
        region = vor_polys[MY_ID]
        i = MY_ID

        x = []
        y = []
        for a_tuple in region:
            x.append(a_tuple[0] * M_FACTOR)  
            y.append(a_tuple[1] * M_FACTOR)

        # 4. Calculate weighted centroid
        [t1, t2, mass] = getCentroid(x, y)

        # Weighted centroid
        wc = getWeightedMiddlePoint([t1/M_FACTOR, t2/M_FACTOR], destination)

        agents_position[i] = np.array([wc[0], wc[1]])   

        # Show centroids using pyplot
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
            print("Step", str(step/ITERATIONS*100) + "%> Image saved!")

        
        time.sleep(2)

    # Save image each 20 steps (to see the program).
    #if step % 19 == 0:
    #plt.savefig("step" + str(step) + ".png")
        
    while True:
        pass
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()

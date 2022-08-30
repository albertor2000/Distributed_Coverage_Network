import random
import threading
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from matplotlib.collections import PolyCollection
from scipy.spatial import Voronoi
from shapely.geometry import Polygon

# SERVICE LIBRARIES
from agent_interfaces.srv import GetPosition

import rclpy
from rclpy.node import Node

# Id of this agent
MY_ID = 0

# Coordinates of this agent
mx = 2
my = 3
mz = 4

class PositionService(Node):
    global mx, my, mz

    def __init__(self):
        super().__init__('pos_service_0')
        self.srv = self.create_service(GetPosition, 'get_position_0', self.add_three_ints_callback)        # CHANGE

    def add_three_ints_callback(self, request, response):

        response.x = mx
        response.y = my
        response.z = mz
        self.get_logger().info('Incoming request\nx: %d y: %d z: %d' % (response.x, response.y, response.z)) # CHANGE

        return response

def threadingFun():
    global mx, my, mz
    print("Service started!")

    while True:
        time.sleep(2)

        print("Position changed")
        mx = random.randrange(0, 10)
        my = random.randrange(0, 10)
        mz = random.randrange(0, 10)

    #plt.scatter([2,4],[1,2], c="green")
    #plt.savefig("images/test2")

def main(args=None):
    rclpy.init(args=args)

    position_service = PositionService()
    
    x = threading.Thread(target=threadingFun)
    x.start()
    
    rclpy.spin(position_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
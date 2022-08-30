from agent_interfaces.srv import GetPosition     # CHANGE

import threading
import time
import rclpy
from rclpy.node import Node

ID = 0

class MinimalService(Node):

    def __init__(self):
        super().__init__('pos_service')
        self.srv = self.create_service(GetPosition, 'get_position', self.add_three_ints_callback)        # CHANGE

    def add_three_ints_callback(self, request, response):

        response.x = 8
        response.y = 9
        response.z = 0
        self.get_logger().info('Incoming request\nx: %d y: %d z: %d' % (response.x, response.y, response.z)) # CHANGE

        return response

def threadingFun():
    print("start spin")
    for i in range(10):
        print(i)
        i = i + 1
        time.sleep(1)

    

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()
    

    x = threading.Thread(target=threadingFun)
    x.start()
    
    rclpy.spin(minimal_service)
    print("ta ta taaaaa")

    rclpy.shutdown()

if __name__ == '__main__':
    main()
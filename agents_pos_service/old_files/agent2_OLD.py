from concurrent.futures import thread
from agent_interfaces.srv import GetPosition

import threading
import sys
import time
import rclpy
from rclpy.node import Node

# Id of this agent
MY_ID = 0

# Coordinates of this agent
mx = 1
my = 2
mz = 3

# id agent to ask coordinates
destination_id = 2

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


class PositionClientAsync(Node):
    global MY_ID, destination_id

    def __init__(self):
        super().__init__('pos_client_' + str(MY_ID))
        self.cli = self.create_client(GetPosition, 'get_position_' + str(destination_id))       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetPosition.Request()                                   # CHANGE

    def send_request(self):
        self.get_logger().info('Request sent')
        self.future = self.cli.call_async(self.req)


def main(args=None):
    global destination_id
    destination_id = 2

    rclpy.init(args=args)

    position_service = PositionService()
    minimal_client = PositionClientAsync()
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(position_service)
    executor.add_node(minimal_client)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()
    
    #rclpy.spin(position_service)

    while True:
        time.sleep(3.2)
        
        minimal_client.send_request()

        while rclpy.ok():
            rclpy.spin_once(minimal_client)
            if minimal_client.future.done():
                try:
                    response = minimal_client.future.result()
                except Exception as e:
                    minimal_client.get_logger().info(
                        'Service call failed %r' % (e,))
                else:
                    minimal_client.get_logger().info(
                        'Posizione: x: %d y: %d z: %d' %                               # CHANGE
                        (response.x, response.y, response.z))
                break
    

    rclpy.shutdown()


if __name__ == '__main__':
    main()
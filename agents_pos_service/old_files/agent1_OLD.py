from agent_interfaces.srv import GetPosition

import sys
import time
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('pos_client')
        self.cli = self.create_client(GetPosition, 'get_position_0')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetPosition.Request()                                   # CHANGE

    def send_request(self):
        self.get_logger().info('Request sent')
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()

    while True:
        time.sleep(5)
        
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

    
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Range

from px4_msgs.msg import VehicleOdometry

from interfaces.msg import Posmsg

import time

MY_ID = 0

px = 5.0
py = 10.0
pz = -30.0

class CoordinatesPublisher(Node):
    global MY_ID
    global px, py, pz

    def __init__(self):
        super().__init__('minimal_publisher')
        print("Connecting to /iris"+str(MY_ID)+"/pos ...")
        self.publisher_ = self.create_publisher(Posmsg, 'iris'+str(MY_ID)+"/pos", 10)
        #timer_period = 5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0

    def send_coordinates(self):
        msg = Posmsg()
        msg.agent_id = 0
        msg.x = px
        msg.y = py
        msg.z = pz
        self.publisher_.publish(msg)
        self.get_logger().info('%s> %s, %s, %s' % (msg.agent_id, msg.x, msg.y, msg.z))


def main(args=None):
    global px, py, pz

    rclpy.init(args=args)

    minimal_publisher = CoordinatesPublisher()

    time.sleep(5)

    minimal_publisher.send_coordinates()

    time.sleep(5)

    px = 15.0
    py = 20.0
    pz = -25.0
    minimal_publisher.send_coordinates()

    #rclpy.spin(minimal_publisher)
    while True:
        pass

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
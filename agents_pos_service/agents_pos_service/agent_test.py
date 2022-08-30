import rclpy as rospy
import time
from agent_interfaces.srv import GetPosition
import sys

def callback_receive(msg):
    rospy.wait_for_service('get_position_1')
    rospy.wait_for_service('get_position_2')

    if msg.data == 1:
        joint2 = rospy.ServiceProxy('get_position_1', GetPosition)
        joint1 = rospy.ServiceProxy('get_position_2', GetPosition)
        joint_2=joint2(True)
        joint_1=joint1(True)

    elif msg.data == 0:
        joint2 = rospy.ServiceProxy('get_position_1', GetPosition)
        joint1 = rospy.ServiceProxy('get_position_2', GetPosition)
        joint_2=joint2(False)
        joint_1=joint1(False)


if __name__ == '__main__':
    rospy.init_node('subscriber_node')
    rospy.Subscriber("/X",callback_receive)



rospy.spin()
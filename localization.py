import sys

from utilities import Logger, euler_from_quaternion
import rclpy
from rclpy.time import Time
from rclpy.node import Node

from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from nav_msgs.msg import Odometry as odom

from rclpy import init, spin
import math

rawSensor = 0
class localization(Node):
    
    def __init__(self, localizationType=rawSensor):

        super().__init__("localizer")
        
        # Remember to define your QoS profile based on the information available in "ros2 topic info /odom --verbose" as explained in Tutorial 3

        odom_qos=QoSProfile(reliability=2, durability=2, history=1, depth=10)

        self.loc_logger=Logger("robot_pose.csv", ["x", "y", "theta", "stamp"])
        self.pose=None
        
        if localizationType == rawSensor:
            self.odom = self.create_subscription(odom, 'odom', self.odom_callback, 10)
        else:
            print("This type doesn't exist", sys.stderr)
    
    
    def odom_callback(self, pose_msg):
        self.pose=[pose_msg.pose.pose.position.x,
                   pose_msg.pose.pose.position.y,
                   euler_from_quaternion(pose_msg.pose.pose.orienation),
                   pose_msg.header.stamp]
        
        # Log the data
        self.loc_logger.log_values([self.pose[0], self.pose[1], self.pose[2], Time.from_msg(self.pose[3]).nanoseconds])
    
    def getPose(self):
        return self.pose

# Here put a guard that makes the node run, ONLY when run as a main thread!
# This is to make sure this node functions right before using it in decision.py
def main():
    rclpy.init()
    loc = localization()
    rclpy.spin(loc)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped    
    
class TeleopMoveNode(Node):
    def __init__(self):
        super().__init__("teleop_move")
        self.create_subscription(Twist, "cmd_vel", self.teleop_callback, 10)
        self.publisher_=self.create_publisher(PoseStamped, "teleop_pose", 10)    
        self.teleop_pose=PoseStamped()
        self.teleop_pose.header.frame_id="map"
    def teleop_callback(self, msg):
        self.teleop_pose.header.stamp=self.get_clock().now().to_msg() 

        self.teleop_pose.pose.position.x+=msg.linear.x
        self.teleop_pose.pose.position.y+=msg.linear.y
        self.publisher_.publish(self.teleop_pose)


    
def main(args=None):
    rclpy.init(args=args)
    node = TeleopMoveNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
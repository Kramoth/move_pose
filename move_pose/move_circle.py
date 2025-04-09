#!/usr/bin/env python3
import rclpy
import rclpy.clock
import math
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
    
    
class MoveCircleNode(Node):
    def __init__(self):
        super().__init__("move_circle")
        self.pose_publisher=self.create_publisher(PoseStamped, "circle_pose", 10)
        self.create_timer(0.03, self.move_circle_pub)
        self.radius=5
        self.theta=0
        self.speed=0.05
    
    def move_circle_pub(self):
        msg=PoseStamped()
        msg.header.frame_id="map"
        msg.header.stamp=self.get_clock().now().to_msg() 

        self.theta+=self.speed
        msg.pose.position.x=self.radius*math.cos(self.theta)
        msg.pose.position.y=self.radius*math.sin(self.theta)
        msg.pose.orientation.w=1.0
        
        self.pose_publisher.publish(msg)



    
def main(args=None):
    rclpy.init(args=args)
    node = MoveCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
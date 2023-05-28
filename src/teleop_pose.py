#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped, Twist



def teleop_move():
	global pub, message
	rospy.init_node("teleop_pose_node")
	message=PoseStamped()
	message.header.frame_id="map"
	pub=rospy.Publisher("teleop_pose",PoseStamped,queue_size=1)
	rospy.Subscriber("cmd_vel",Twist,callback)
	rospy.spin()

def callback(data):
	global message
	current_time=rospy.Time.now()
	message.header.stamp=current_time
	message.pose.position.x+=data.linear.x
	message.pose.position.y+=data.linear.y
	pub.publish(message)

if __name__=="__main__":
	teleop_move()

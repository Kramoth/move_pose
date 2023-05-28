#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped
import math

def circlePose():
	rospy.init_node("circle_pose_node")
	pub=rospy.Publisher("published_topic",PoseStamped,queue_size=1)
	rate=rospy.Rate(30)
	R=4
	speed=0.1
	theta=0.0
	while not rospy.is_shutdown():
		theta=theta+speed
		message=PoseStamped()
		message.header.frame_id="map"
		message.header.stamp=rospy.Time.now()
		message.pose.position.x=R*math.cos(theta)
		message.pose.position.y=R*math.sin(theta)
		message.pose.orientation.w=1
		pub.publish(message)
		rate.sleep()

if __name__=="__main__":
	try:
		circlePose()
	except rospy.ROSInterruptException:
		pass

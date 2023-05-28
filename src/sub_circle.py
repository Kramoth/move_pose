#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped


def listener():
	rospy.init_node("circle_sub_node")
	rospy.Subscriber("subscribed_topic",PoseStamped,callback)
	rospy.spin()

def callback(data):
	print(data)

if __name__=="__main__":
	listener()

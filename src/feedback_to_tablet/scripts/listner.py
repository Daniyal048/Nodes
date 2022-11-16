#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def talker_handler(data):
    rospy.loginfo(data.data)


def listner():
    rospy.init_node('listner', anonymous=True)
    rospy.Subscriber('talk_line',String, talker_handler)

    rospy.spin()

if __name__ == "__main__":
    listner()

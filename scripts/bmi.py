#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def cb(message):
    print('{0}mile = {1}km'.format(message.data,message.data*1.6))

if __name__ == '__main__':
    rospy.init_node('mile')
    sub = rospy.Subscriber('/number', Int32, cb)
    rospy.spin()

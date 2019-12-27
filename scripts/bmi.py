#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray, Float32

def cb(message):
    pub = rospy.Publisher('bmi', Float32, queue_size = 1)
    bmi = message.data[0]/(message.data[1]*message.data[1])
    print('BMI = {}'.format(bmi))
    pub.publish(bmi)


if __name__ == '__main__':
    rospy.init_node('bmi')
    sub = rospy.Subscriber('/weight_height', Float32MultiArray, cb)
    rospy.spin()

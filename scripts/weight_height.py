#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray

rospy.init_node('weight_height')
pub = rospy.Publisher('/weight_height', Float32MultiArray, queue_size=1)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    weight = float(raw_input('input weight[kg]:'))
    height = float(raw_input('input height[m]:'))
    body_data = [weight, height]
    print(body_data)
    body_data = Float32MultiArray(data = body_data)
    pub.publish(body_data)
    rate.sleep()

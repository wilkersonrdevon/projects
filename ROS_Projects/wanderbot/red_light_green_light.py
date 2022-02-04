#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist

def mover():
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.init_node('light')

    red_light_twist = Twist()
    red_light_twist.linear.x = 0
    green_light_twist = Twist()
    green_light_twist.linear.x = 0.05

    driving_forward = True
    rate = rospy.Rate(10)
    light_change_time = rospy.Time.now()

    while not rospy.is_shutdown():
        if driving_forward:
            cmd_vel_pub.publish(green_light_twist)
        else:
            cmd_vel_pub.publish(red_light_twist)
        if rospy.Time.now() > light_change_time:
            driving_forward = not driving_forward
            light_change_time = rospy.Time.now() + rospy.Duration(3)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
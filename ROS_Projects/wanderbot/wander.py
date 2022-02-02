#!/usr/bin/env python3 
import rospy
import math
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

left = []
right = []
front = []

def scan_callback(msg):
    global left
    global right
    global front

    l=len(msg.ranges)
    range_ahead = msg.ranges[0]   

    filtered_range = [x for x in msg.ranges if not math.isinf(x)]
    filtered_range = [x for x in filtered_range if not math.isnan(x)]
    l_filtered = len(filtered_range)

    front = msg.ranges[0:60]
    front = front + msg.ranges[300:360]
    front = [x for x in front if not math.isinf(x)]
    front = [x for x in front if not math.isnan(x)]

    left = msg.ranges[60:181]
    left = [x for x in left if not math.isinf(x)]
    left = [x for x in left if not math.isnan(x)]

    right = msg.ranges[180:301]
    right = [x for x in right if not math.isinf(x)]
    right = [x for x in right if not math.isnan(x)]

def mover():
    global left
    global right
    global front

    scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.init_node('range_ahead')

    turn_twist = Twist()
    turn_twist.linear.x = 0
    turn_twist.angular.z = 0

    while not rospy.is_shutdown():
        if min(front) >= 0.3:
            turn_twist.linear.x = .22
            turn_twist.angular.z = 0
            pub.publish(turn_twist)
        elif min(right) >= 0.3:
            turn_twist.linear.x = 0
            turn_twist.angular.z = -.22
            pub.publish(turn_twist)
        elif min(left) >= 0.3:
            turn_twist.linear.x = 0
            turn_twist.angular.z = .22
            pub.publish(turn_twist)
        else:
            turn_twist.linear.x = -.22
            turn_twist.angular.z = 0
            pub.publish(turn_twist)


if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
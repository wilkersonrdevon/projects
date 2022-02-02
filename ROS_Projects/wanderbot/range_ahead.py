#!/usr/bin/env python3 
import rospy
import math
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def scan_callback(msg):
    global left, right, front
    l=len(msg.ranges)
    range_ahead = msg.ranges[0]   

    filtered_range = [x for x in msg.ranges if not math.isinf(x)]
    filtered_range = [x for x in filtered_range if not math.isnan(x)]
    l_filtered = len(filtered_range)
    filtered_range_middle = len(filtered_range)/2

    # Number of elements
    print("scan elements: {0}".format(l_filtered))
    # Scan data 
    print("scan data: {0}".format(filtered_range))
    # First element
    print("first element: {0}".format(filtered_range[0]))
    # Middle element
    print("middle element: {0}".format(filtered_range[int(filtered_range_middle)]))
    # Element with least value
    print("element with least value: {0}".format(np.min(filtered_range[0:360]))) 
    # Mean distance of all
    print("mean distance: {0}".format(np.mean(filtered_range)))

    # Mean and min of front
    front = msg.ranges[0:60]
    front = front + msg.ranges[300:360]
    front = [x for x in front if not math.isinf(x)]
    front = [x for x in front if not math.isnan(x)]
    print("mean distance front: {0}".format(np.mean(front)))
    print("min distance front: {0}".format(np.min(front)))
    # Mean and min of left
    left = msg.ranges[60:180]
    left = [x for x in left if not math.isinf(x)]
    left = [x for x in left if not math.isnan(x)]
    print("mean distance left: {0}".format(np.mean(left)))
    print("min distance left: {0}".format(np.min(left)))
    # Mean and min of right
    right = msg.ranges[180:300]
    right = [x for x in right if not math.isinf(x)]
    right = [x for x in right if not math.isnan(x)]
    print("mean distance right: {0}".format(np.mean(right)))
    print("min distance right: {0}".format(np.min(right)))

scan_sub=rospy.Subscriber('/scan', LaserScan, scan_callback)
rospy.init_node('range_ahead') 
# rospy.spin()
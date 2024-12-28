#! /usr/bin/env python

import rospy
from std_srvs.srv import *
from assignment_2_2024.srv import *
import time
from geometry_msgs.msg import Point

import math


def get_goal(data):
    res = GoalResponse()
    res.success = True
    desired_position_ = Point()
    desired_position_.x = rospy.get_param('des_pos_x')
    desired_position_.y = rospy.get_param('des_pos_y')
    res.goal_pose = desired_position_
    return res

def main():
    rospy.init_node('get_goal')

    srv = rospy.Service('get_goal', Goal, get_goal)

    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':
    main()

#! /usr/bin/env python
import rospy
import actionlib
import assignment_2_2024.msg
from geometry_msgs.msg import Point, Pose, Twist,PoseStamped
from assignment_2_2024.msg import PoseVel
from std_msgs.msg import Empty 
from nav_msgs.msg import Odometry

pos_vel_pub = None
sub_odom = None
sub_set_goal = None
sub_cancel_goal = None
action_client = None

last_x = None
last_z = None

def clbk_cancel_goal(data):
    action_client.cancel_goal()

def clbk_odom(msg):
    global last_x
    global last_z

    # position
    position_ = msg.pose.pose.position
    pose_vel = PoseVel()
    pose_vel.x = position_.x
    pose_vel.y = position_.y

    pose_vel.vel_x = 0
    pose_vel.vel_z = 0
    
    if last_x:
        pose_vel.vel_x = position_.x - last_x
    if last_z:
        pose_vel.vel_z = position_.z - last_z
    last_x = position_.x
    last_z = position_.z

    pos_vel_pub.publish(pose_vel)


def feedback_callback(feedback):
    rospy.loginfo("feedback {}".format(feedback.stat))
    rospy.loginfo("pos x {} pos y {}".format(feedback.actual_pose.position.x,feedback.actual_pose.position.y))





def bug_client(goal):
    # SimpleActionClient construction, targeting the fibonacci topic of type Fibonacci
    

    # Waits until the action server has started up and started
    # listening for goals. (So the goals aren't ignored.)
    action_client.wait_for_server()

    new_goal = PoseStamped()
    new_goal.pose = goal
    new_goal.header.stamp = rospy.Time.now()  # Current time
    new_goal.header.frame_id = "odom"
    # Creates a goal to send to the action server.
    goal = assignment_2_2024.msg.PlanningGoal(target_pose=new_goal)

    # Sends the goal to the action server.
    action_client.send_goal(goal,feedback_cb=feedback_callback)

    # Waits for the server to finish performing the action.
    action_client.wait_for_result()

    # Prints out the result of executing the action
    return action_client.get_result()

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('bug_client_py')

        pos_vel_pub = rospy.Publisher('/pos_vel', PoseVel,queue_size=1)

        sub_odom = rospy.Subscriber('/odom', Odometry, clbk_odom)
        sub_set_goal = rospy.Subscriber('/set_goal', Pose, bug_client)
        sub_cancel_goal = rospy.Subscriber('/cancel_goal', Empty, clbk_cancel_goal)
        
        action_client = actionlib.SimpleActionClient('/reaching_goal', 
                                          assignment_2_2024.msg.PlanningAction)
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            rate.sleep()
    except rospy.ROSInterruptException:
        print("program interrupted before completion")













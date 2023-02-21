#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
global cmd
def controller_callback(data: Twist)->None:
    #global cmd
    cmd.linear.x=data.linear.x
    cmd.angular.z=data.angular.z
if __name__=="__main__":
    rospy.init_node("go_node")
    #rospy.spin()
    cmd=Twist()
    while not rospy.is_shutdown():
        go_sub=rospy.Subscriber("ready_node",Twist,controller_callback)
        go_pub=rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
        go_pub.publish(cmd)
    

    

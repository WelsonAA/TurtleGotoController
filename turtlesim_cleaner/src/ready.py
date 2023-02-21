#!/usr/bin/env python3
import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
global goalX,goalY,currentX,currentY,currentTheta,dist,deltaX,deltaY
goalX=-1
goalY=-1
currentX=-1
currentY=-1
currentTheta=-1
dist=8
deltaX=-1
deltaY=-1
def update_pose(data):
    currentX=data.x
    currentY=data.y
    currentTheta=data.theta
    deltaX=goalX-currentX
    deltaY=goalY-currentY
def find_dist():
    dist=math.sqrt(deltaX*deltaX+deltaY*deltaY)
    return dist
def calc(beta,phi):
    linvX=beta*dist
    angvZ=phi*(math.atan2(deltaY,deltaX)-currentTheta)
    cmd=Twist()
    cmd.linear.x=linvX
    cmd.angular.z=angvZ
    return cmd
if __name__=="__main__":
    rospy.init_node("ready_node")
    beta=int(input("Enter Beta: ")) #Linear Speed
    phi=int(input("Enter Phi: ")) #Rotation Speed
    goalY=rospy.get_param("goalX",0)
    goalX=rospy.get_param("goalY",0)
    while dist>=0.01:
        ready_sub=rospy.Subscriber("turtle1/pose",Pose,update_pose)
        ready_pub=rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
        dataa=calc(beta,phi)
        ready_pub.publish(dataa)
    rospy.spin()
        
#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

global talker1_out
global talker2_out

def isPrime(num) : 
 
    # Corner cases 
    if (num <= 1) : 
        return False
    if (num <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (num % 2 == 0 or num % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

def callback1(data):
	global talker1_out
	rospy.loginfo(rospy.get_caller_id() + 'I heard from talker1: %s', data.data)
	talker1_out = data.data
	int_process()

def callback2(data):
	global talker2_out
	rospy.loginfo(rospy.get_caller_id() + 'I heard from talker2: %s', data.data)
	talker2_out = data.data
	int_process()

def int_process():
	global talker1_out,talker2_out
	if(talker1_out != 0 and talker2_out != 0):
		print('Start processing...')
		if(isPrime(talker1_out) and isPrime(talker2_out)):
			rospy.loginfo('Number requested is: %s', max(talker1_out,talker2_out))
			# print('Number requested is: ', max(talker1_out,talker2_out))
		elif(isPrime(min(talker1_out,talker2_out))):
			rospy.loginfo('Number requested is: %s', min(talker1_out,talker2_out))
			# print('Number requested is: ', min(talker1_out,talker2_out))
		else:
			rospy.loginfo('Number requested is: %s', max(talker1_out,talker2_out))
			# print('Number requested is: ', max(talker1_out,talker2_out))
		talker1_out = 0
		talker2_out = 0


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter1', Int64, callback1)
    rospy.Subscriber('chatter2', Int64, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	global talker1_out,talker2_out
	talker1_out = 0
	talker2_out = 0
	listener()

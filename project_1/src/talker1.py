#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import Int64
import random

def talker1():
    pub = rospy.Publisher('chatter1', Int64, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        int_sent = random.randint(1,1000) % rospy.get_time()
        rospy.loginfo(int_sent)
        pub.publish(int_sent)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass

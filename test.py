import rospy
from std_msgs.msg import String


pub = rospy.Publisher('chatter', String, queue_size=10)
rospy.init_node('talker', anonymous = True)

rate = rospy.Rate(1)

i=0
while not rospy.is_shutdown():
    hello_str = "hello world %s" % i
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    i=i+1
	    
#if _name_ == '_main_':
#	try:
#		talker()
#	except rospy.ROSInterruptException:
#		pass

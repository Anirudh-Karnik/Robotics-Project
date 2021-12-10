#Anirudh Karnik
#19BEC0353

from gpiozero import Servo
from time import sleep
import rospy
from std_msgs.msg import String

servo = Servo(25)

def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("chatter", String, chatter_callback)
    
    rospy.spin()
    
def chatter_callback(message):
    print(message.data)
    if(str(message.data) == "Expired"):
        print("I am here")
        servo.min()
    elif(str(message.data) == "Available"):
        servo.max()

if __name__ == "__main__":
    listener()
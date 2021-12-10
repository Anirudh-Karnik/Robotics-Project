#Anirudh Karnik
#19BEC0353

import cv2
from gpiozero import Servo
from time import sleep
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('chatter', String, queue_size=10)
rospy.init_node('talker', anonymous = True)

rate = rospy.Rate(1)

# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()
# servo = Servo(25)

# def listener():
#     rospy.init_node('listener', anonymous = True)
#     rospy.Subscriber("chatter", String, chatter_callback)
#     
#     rospy.spin()
#     
# def chatter_callback(message):
#     print(message.data)
#     if(str(message.data) == "Expired"):
#         print("I am here")
#         servo.min()
#     elif(str(message.data) == "Available"):
#         servo.max()
    
while True:
#     listener()
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
            if int(data)<20211122:
                print("Expired2")
                hello_str = "Expired"
                rospy.loginfo(hello_str)
                pub.publish(hello_str)
                #servo.min()
                sleep(0.5)
            else:
                print("Available2")
                hello_str = "Available"
                #rospy.loginfo(hello_str)
                pub.publish(hello_str)
                #servo.max()
                sleep(0.5)
#     # display the image preview
#     cv2.imshow("code detector", img)
#     if(cv2.waitKey(1) == ord("q")):
#         break
# # free camera object and exit
cap.release()
cv2.destroyAllWindows()


#!/usr/bin/env python3

# Bibliotecas necessarias
import rospy
import cv2
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


# Funcao q ira publicar os comandos no topico
def talker():
    # Objeto q ira publicar no topico teleop_topic
    pub = rospy.Publisher('picamera/image_raw', Image, queue_size=10)
    
    # Inicio do node teleop_pub
    rospy.init_node('picamera_node', anonymous=True)

    # Criacao do ojeto de conversao
    bridge = CvBridge()

    # Setup da camera 
    cap = cv2.VideoCapture(0)

    # Setup de largura e altura da captura
    cap.set(3, 320)
    cap.set(4, 240)

    while not rospy.is_shutdown():           
        # Captura de um frame na camera
        ret, cv2_frame = cap.read()

        # Converter a img cv2 em img ROS
        ros_frame = bridge.cv2_to_imgmsg(cv2_frame, "bgr8")
    
        # Publicacao da img no topico
        print('[info] imagem sendo publicada')  
        pub.publish(ros_frame)

# Funcao main
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
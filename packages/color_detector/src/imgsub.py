#!/usr/bin/env python3
# modified on the basis of https://github.com/duckietown/dt-duckiebot-interface/blob/daffy/packages/camera_driver/src/camera_node.py

import os
import rospy
import cv2
import atexit
import numpy as np
from threading import Thread
import argparse 

from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage, CameraInfo
from sensor_msgs.srv import SetCameraInfo, SetCameraInfoResponse
from cv_bridge import CvBridge

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_topic", type=str, default="")

class MySubscriberNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MySubscriberNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.sub = rospy.Subscriber('chatter', String, self.callback)

    def callback(self, data):
        rospy.loginfo("I heard %s", data.data)

if __name__ == '__main__':
    # create the node
    node = MySubscriberNode(node_name='my_subscriber_node')
    # keep spinning
    rospy.spin()
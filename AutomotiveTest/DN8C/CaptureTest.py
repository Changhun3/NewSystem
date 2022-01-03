import datetime
import cv2
import keyboard
from api_class import *
import os

api = api_class

while True:
    time.sleep(0.1)

    if keyboard.is_pressed(80):
        api.CameraCapture()
    elif keyboard.is_pressed('delete'):
        api.CameraStop()
        time.sleep(3)
        break
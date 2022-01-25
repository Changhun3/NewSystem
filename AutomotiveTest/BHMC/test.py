import datetime
import cv2
from api_class import *
import os
import time

api = api_class

# Test 해보는 곳인데, time.sleep이 없으면 준비도 전에 진행해서 Error 발생 함.
time.sleep(3)

api.Enter_Radio_Screen()
for i in range(0, 10):  # 10
    os.system("adb shell input tap " + str(365) + " " + str(165))
    time.sleep(20)
    os.system("adb shell input tap " + str(365) + " " + str(245))
    time.sleep(20)
    os.system("adb shell input tap " + str(365) + " " + str(355))
    time.sleep(20)

os.system("adb shell input tap " + str(365) + " " + str(165))
time.sleep(3) #

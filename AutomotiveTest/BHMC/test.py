import datetime
import cv2
from api_class import *
import os

api = api_class

# Test 해보는 곳인데, time.sleep이 없으면 준비도 전에 진행해서 Error 발생 함.
time.sleep(3)

api.Enter_Tingban_Screen()
for i in range(0, 1):  # 45
    api.Tingban_SeekDown(30)
    api.Tingban_SeekDown(30)
    api.Tingban_SeekUp(30)
time.sleep(2)

api.Enter_Home_Screen()

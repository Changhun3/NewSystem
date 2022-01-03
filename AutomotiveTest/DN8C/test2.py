import os
import time

print("# adb connect")
os.system("adb start-server")
time.sleep(1)
os.system("adb devices")
time.sleep(1)


print("# adb - Home Key 동작")
os.system("adb shell input keyevent 3")
time.sleep(1)
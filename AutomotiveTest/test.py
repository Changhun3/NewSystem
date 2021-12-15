import datetime
import cv2
from api_class import *
import os


#hhghj
"""capture = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == 27:
        break
    elif key == 26:
        print("캡쳐")
        cv2.imwrite("./data/" + str(now) + ".png", frame)

capture.release()
cv2.destroyAllWindows()"""

# Test

#configuration = eval(open("./data/data.conf").read())
#print(configuration[0]["Swipe_roofPopupDown"])
#print(configuration[1]["Swipe_roofPopupDown"])
#print(datetime.datetime.now())

api = api_class
api.BAT_On()
#time.sleep(3)

#Home_Screen = "./referenceimage/HomeScreen.png"
#imagematchingResult = api.ImageCompareResult(Home_Screen)


#if imagematchingResult:
#    print("PASS~~~~")
#else:
#    print("Fail~~~~!!!")

#bMusic_Button = [20, 200]

#os.system("adb shell input tap " + str(bMusic_Button[0]) + " " + str(bMusic_Button[1]))
count = 0

adb_connect = os.popen("adb devices").readlines()
DeviceID = '00d6f7955f1c'

print(adb_connect)

for line in adb_connect:
    print(line)
    if DeviceID in line:
        print("Connected ADB Server!")
        break
    else:
        print("Not Connected ADB Server..")
        count += 1


"""start_time = time.time()
end_time = start_time + (60 * 60 * 24)

count = 0
while((time.time()) < end_time):
    api.Application_Button()
    api.Audio_Button()
    api.Music_Button()
    api.Navi_Button()
    api.Home_Button()
    count += 1
    print("count = " + count)
    time.sleep(3)"""

"""
api.BAT_Off(5)
api.BAT_On(40)
api.ACC_On(5)

for i in range(0, 1000):
    api.adb_test2()
    api.adb_test()
    time.sleep(2)


radio = "./referenceimage/radio_icon.png"
usb = "./referenceimage/usb_icon.png"
BT = "./referenceimage/BT_icon.png"
Yandex = "./referenceimage/Yandex_icon.png"

test = api.ImageLocation(radio)
print("1")
print(test)
print("++++++++++++++++++++++++++++++++++++++++++++++")

test = api.ImageLocation(usb)
print("2")
print(test)
print("++++++++++++++++++++++++++++++++++++++++++++++")

test = api.ImageLocation(BT)
print("3")
print(test)
print("++++++++++++++++++++++++++++++++++++++++++++++")

test = api.ImageLocation(Yandex)
print("4")
print(test)
print("++++++++++++++++++++++++++++++++++++++++++++++")
"""
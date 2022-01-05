# -*- coding: utf-8 -*-
import os
import time
from aibox import *
from camera import *
import threading

# #####################################
configuration = eval(open("./data/data.conf").read())

# Avtovaz #######################################################################
bHome_Button = configuration["bHome_Button"]
bNavi_Button = configuration["bNavi_Button"]
bMusic_Button = configuration["bMusic_Button"]
bAudio_Button = configuration["bAudio_Button"]
bApplication_Button = configuration["bApplication"]
bMusic_Mode_Button = configuration["bMusic_Mode_Button"]
bRadio_Icon = configuration["bRadio_Icon"]
bUSB_Icon = configuration["bUSB_Icon"]
bBT_Icon = configuration["bBT_Icon"]
bYandex_Icon = configuration["bYandex_Icon"]


# Camera Setting
Camera_Start = camera.camera_start
Camera_Stop = camera.camera_stop
Camera_Capture = camera.camera_capture
Camera_Reboot = camera.camera_RebootDetect
Camera_Freeze = camera.camera_FreezeDetect

th1 = threading.Thread(target=Camera_Start)
th2 = threading.Thread(target=Camera_Reboot)
th3 = threading.Thread(target=Camera_Freeze)

# Device ID. cmd에 "adb devices" 치면 나옴
DeviceID = '00d6f7955f1c'
# Device ID
deviceFile = open('./data/DeviceID.txt', mode='rt', encoding='utf-8')
DeviceID = deviceFile.readline()

class API_Class():
    rebootIndicator = False
    freezeIndicator = False

    def __init__(self):
        # ADB 연결
        print("# adb connect")
        time.sleep(1)
        os.system("adb start-server")
        time.sleep(1)
        os.system("adb devices")
        time.sleep(1)

        # USB Camera 동작 시작
        print("# Camera Start")
        th1.start()

        # AIBOX 연결
        print("# AIBOX Connect")
        aibox.connect()

    def adb_test(self):
        print("# adb - Home Key 동작")
        os.system("adb shell input keyevent 3")
        time.sleep(3)

    def adb_test2(self):
        print("# adb - Menu Tap 동작")
        os.system("adb shell input tap 20 300")
        time.sleep(3)

    # Reboot 및 Freeze 감지 API #######################################################################################
    def rebootDetect(self, value):
        print("# Reboot 감지 동작 Enable")
        self.rebootIndicator = value

        if self.rebootIndicator == True:
            print("Reboot 감지 동작 시작")
            th2.start()
        else:
            print("Reboot 감지 동작 중단")
            th2.join()

    def freezeDetect(self, value):
        print("# Freeze 감지 동작 Enable")
        self.freezeIndicator = value

        if self.rebootIndicator == True:
            print("Freeze 감지 동작 시작")
            th3.start()
        else:
            print("Freeze 감지 동작 중단")
            th3.join()


    # Camera 및 Image 비교 관련 API ###################################################################################
    def ImageCompareResult(self, referenceImage):
        result = camera.camera_detectImage(referenceImage)
        if result:
            return True
        else:
            print("Not Matched Image!")
            #print("max_val : " + max_val)
            camera.camera_issue()
            return False

    def CameraCapture(self):
        print("# Screen Capture")
        Camera_Capture()

    def CameraStop(self):
        print("Camera Stop")
        Camera_Stop()
        th1.join()

    def ImageLocation(self, detecImage):
        print("Image Location")
        location = camera.camera_searchLocation(detecImage)
        print("Icon Location is " + str(location))

    # ADB - Menu 또는 특정 항목 관련 동작 API #########################################################################
    def Enter_Home_Screen(self, wait_time=5):
        print("#Entered Home Screen.")
        os.system("adb shell input keyevent 3")
        time.sleep(wait_time)

    def Enter_Navi_Screen(self, wait_time=5):
        print("#Entered Navi Screen.")
        os.system("adb shell input tap " + str(bNavi_Button[0]) + " " + str(bNavi_Button[1]))
        time.sleep(wait_time)

    def Enter_FM_Radio_Screen(self, wait_time=3):
        print("#Entered FM Radio Screen.")
        # Media 버튼
        self.Music_Button(3) #########################질문 왜 b가 안붙는지?
        self.Music_Mode_Button(3)

        # Radio Icon tap
        print("# Tap Radio Icon")
        os.system("adb shell input tap " + str(bRadio_Icon[0]) + " " + str(bRadio_Icon[1])) #################### 질문 왜 self.cis.tap(bList_sMediaMusic[0], bList_sMediaMusic[1]) 형식이 아닌지
        time.sleep(wait_time)

    def Enter_USB_Music_Screen(self, wait_time=3):
        print("#Entered USB Music Screen.")
        # Media 버튼
        self.Music_Button(3)
        self.Music_Mode_Button(3)

        # USB Icon tap
        print("# Tap USB Icon")
        os.system("adb shell input tap " + str(bUSB_Icon[0]) + " " + str(bUSB_Icon[1]))
        time.sleep(wait_time)

    def Enter_BT_Music_Screen(self, wait_time=3):
        print("#Entered BT Music Screen.")
        # Media 버튼
        self.Music_Button(3)
        self.Music_Mode_Button(3)

        # BT Icon tap
        print("# Tap BT Icon")
        os.system("adb shell input tap " + str(bBT_Icon[0]) + " " + str(bBT_Icon[1]))
        time.sleep(wait_time)

    def Enter_Yandex_Music_Screen(self, wait_time=3):
        print("#Entered Yandex Music Screen.")
        # Media 버튼
        self.Music_Button(3)
        self.Music_Mode_Button(3)

        # Yandex Icon tap
        print("# Tap Yandex Icon")
        os.system("adb shell input tap " + str(bYandex_Icon[0]) + " " + str(bYandex_Icon[1]))
        time.sleep(3)

        # Play 여부 확인 후, Play 버튼 동작 수행
        playImage = "./referenceimage/PlayImage.png"
        matchResult = camera.camera_waitImage(playImage)

        if matchResult:
            print("Yandex Music Play")
            os.system("adb shell input keyevent 85")

        time.sleep(wait_time)

    # ADB - Key 관련 동작 API ############################################################################
    def Seek_Up(self, wait_time=3):
        print("#Selected 'Seek_Up' button.")
        """Seek_Up 동작하면 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Seek_Up 동작 안됨으로 처리함"""
        os.system("adb shell input keyevent 88")
        time.sleep(wait_time)
        #self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Seek_Up wasn't operated."))

    def Seek_Down(self, wait_time=3): ########## 질문 keyevent 어디 정의 되어 있는지?
        print("#Selected 'Seek_Down' button.")
        """Seek_Down 동작하면 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Seek_Down 동작 안됨으로 처리함"""
        os.system("adb shell input keyevent 87")
        time.sleep(wait_time)
        #self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Seek_Down wasn't operated."))


    # ADB - Android Tab / Swipe등 관련 동작 API #######################################################################
    def Home_Button(self, wait_time=3):
        print("# Selected 'Home_Button' button.")
        os.system("adb shell input tap " + str(bHome_Button[0]) + " " + str(bHome_Button[1]))
        time.sleep(wait_time)

    def Navi_Button(self, wait_time=3):
        print("# Selected 'Navi_Button' button.")
        os.system("adb shell input tap " + str(bNavi_Button[0]) + " " + str(bNavi_Button[1]))
        time.sleep(wait_time)

    def Music_Button(self, wait_time=3):
        print("# Selected 'Music_Button' button.")
        os.system("adb shell input tap " + str(bMusic_Button[0]) + " " + str(bMusic_Button[1]))
        time.sleep(wait_time)

    def Audio_Button(self, wait_time=3):
        print("# Selected 'Audio_Button' button.")
        os.system("adb shell input tap " + str(bAudio_Button[0]) + " " + str(bAudio_Button[1]))
        time.sleep(wait_time)

    def Application_Button(self, wait_time=3):
        print("# Selected 'Application_Button' button.")
        os.system("adb shell input tap " + str(bApplication_Button[0]) + " " + str(bApplication_Button[1]))
        time.sleep(wait_time)

    def Music_Mode_Button(self, wait_time=3):
        print("# Selected 'Music_Mode_Button' button.")
        os.system("adb shell input tap " + str(bMusic_Mode_Button[0]) + " " + str(bMusic_Mode_Button[1]))
        time.sleep(wait_time)

    # AIBOX - BAT On/Off 등 AITEST BOX 관련 동작 API ##################################################################
    def BAT_On(self, wait_time=50):
        print("# Turned on Battery : " + str(wait_time) + "secs.")

        if wait_time > 8:
            count = 0
            while count < 5:
                aibox.bat_on()
                time.sleep(5)
                bootImage = "./referenceimage/BootImage.png"
                matchResult = camera.camera_waitImage(bootImage)

                if matchResult:
                    print("Detected BootImage!")
                else:
                    print("Booting Fail!")
                time.sleep(wait_time - 5)

                if wait_time > 40:
                    adb_connect = os.popen("adb devices").readlines()
                    for line in adb_connect:
                        if DeviceID in line:
                            print("Connected ADB Server!")
                            print(">>> " + line)
                            return True
                        else:
                            continue
                print("Not Connected ADB Server..")
                print("Restart BAT Off/On..")
                self.BAT_Off(5)
                count += 1
            return False
        else:
            aibox.bat_on()
            time.sleep(wait_time)

    def BAT_Off(self, wait_time=5):
        print("# Turned off Battery : "+str(wait_time)+"secs.")
        aibox.bat_off()
        time.sleep(wait_time)


api_class = API_Class()

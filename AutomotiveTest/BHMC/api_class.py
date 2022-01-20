# -*- coding: utf-8 -*-
import os
import time
from aibox import *
from camera import *
import threading

# #####################################
configuration = eval(open("./data/data.conf").read())

# BHMC #######################################################################
# Swipe 관련 옵션 설정
swipeRoofPopupDown = configuration["Swipe_roofPopupDown"]
swipeUp = configuration["Swipe_up"]
swipeLeft = configuration["Swipe_left"]
swipeRight = configuration["Swipe_right"]
swipeDown = configuration["Swipe_down"]
swipeDuration = configuration["Swipe_duration"]
# Direct command : adb shell input swipe 10(x1) 10(y1) 10(x2) 10(y2)


# 각 버튼의 Tap 위치 설정
bBack_sAllLauncher = configuration["bBack_sAllLauncher"]
bAgree_sMainLauncher = configuration["bAgree_sMainLauncher"]
bQRCode_sMainLauncher = configuration["bQRCode_sMainLauncher"]
bQQMusic_sMainLauncher = configuration["bQQMusic_sMainLauncher"]
bTingban_sMainLauncher = configuration["bTingban_sMainLauncher"]
bTingbanAudio_sSeekdown = configuration["bTingbanAudio_sSeekdown"]
bTingbanAudio_sSeekUp = configuration["bTingbanAudio_sSeekUp"]
bBaiduapps_sMainLauncher = configuration["bBaiduapps_sMainLauncher"]
bBaiduVR_sMainLauncher = configuration["bBaiduVR_sMainLauncher"]
bBaiduweather_sMainLauncher = configuration["bBaiduweather_sMainLauncher"]
bMusic_sMainLauncher = configuration["bMusic_sMainLauncher"]
bVideo_sMainLauncher = configuration["bVideo_sMainLauncher"]
bImage_sMainLauncher = configuration["bImage_sMainLauncher"]
bRadio_sMainLauncher = configuration["bRadio_sMainLauncher"]
bUserProfile_sMainLauncher = configuration["bUserProfile_sMainLauncher"]
bUserOne_sMainLauncher = configuration["bUserOne_sMainLauncher"]
bUserTwo_sMainLauncher = configuration["bUserTwo_sMainLauncher"]
bUserGuest_sMainLauncher = configuration["bUserGuest_sMainLauncher"]
bSetting_sMainLauncher = configuration["bSetting_sMainLauncher"]
bNavigation_sMainLauncher = configuration["bNavigation_sMainLauncher"]
bCarlife_sMainLauncher = configuration["bCarlife_sMainLauncher"]
bCall_sMainLauncher = configuration["bCall_sMainLauncher"]



bBTAudio_sMusicLauncher = configuration["bBTAudio_sMusicLauncher"]
bBTAudio_sSeekdown = configuration["bBTAudio_sSeekdown"]
bBTAudio_AVc_sMusicLauncher = configuration["bBTAudio_AVc_sMusicLauncher"]
bUSB_sMusicLauncher = configuration["bUSB_sMusicLauncher"]
bUSB_sVideoLauncher = configuration["bUSB_sVideoLauncher"]
bUSB_sImageLauncher = configuration["bUSB_sImageLauncher"]
bList_sMediaMusic = configuration["bList_sMediaMusic"]

bDisplay_sControlCenter = configuration["bDisplay_sControlCenter"]
bSplit_sNavigation = configuration["bSplit_sNavigation"]

bSystemLanguage_sSetting = configuration["bSystemLanguage_sSetting"]
bBTSetting_sSetting = configuration["bBTSetting_sSetting"]
bBTTurnOn_sBTSetting = configuration["bBTTurnOn_sBTSetting"]
bBTTurnOff_sBTSetting = configuration["bBTTurnOff_sBTSetting"]

bRadio_sP1 = configuration["bRadio_sP1"]
bRadio_sP2 = configuration["bRadio_sP2"]
bRadio_sP3 = configuration["bRadio_sP3"]
bRefresh = configuration["bRefresh"]
bSlideshow = configuration["bSlideshow"]
bSlideshowfivesec = configuration["bSlideshowfivesec"]
bLanguageCh_sMainLauncher = configuration["bLanguageCh_sMainLauncher"]
bLanguageEn_sMainLauncher = configuration["bLanguageEn_sMainLauncher"]
bLanguageKo_sMainLauncher = configuration["bLanguageKo_sMainLauncher"]

# Avtovaz #######################################################################
"""bHome_Button = configuration["bHome_Button"]
bNavi_Button = configuration["bNavi_Button"]
bMusic_Button = configuration["bMusic_Button"]
bAudio_Button = configuration["bAudio_Button"]
bApplication_Button = configuration["bApplication"]
bMusic_Mode_Button = configuration["bMusic_Mode_Button"]
bRadio_Icon = configuration["bRadio_Icon"]
bUSB_Icon = configuration["bUSB_Icon"]
bBT_Icon = configuration["bBT_Icon"]
bYandex_Icon = configuration["bYandex_Icon"]"""


# Camera Setting
Camera_Start = camera.camera_start
Camera_Stop = camera.camera_stop
Camera_Capture = camera.camera_capture
Camera_Reboot = camera.camera_RebootDetect
Camera_Freeze = camera.camera_FreezeDetect

th1 = threading.Thread(target=Camera_Start)
th2 = threading.Thread(target=Camera_Reboot)
th3 = threading.Thread(target=Camera_Freeze)

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
        result = camera.camera_waitDetectImage(referenceImage)
        if result:
            return True
        else:
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

        if camera.camera_waitDetectImage('./referenceImage/HomeScreen.png', 10, False):
            print("This is HomeScreen")
        else:
            print("This is NOT HomeScreen")
            os.system("adb shell input keyevent 3")
        time.sleep(wait_time)

    def Enter_Navigation_Screen(self):
        print("#Entered Navigation_Screen.")
        os.system("adb shell input keyevent 3")
        time.sleep(10)
        print("#Entered Home_Screen.")
        os.system("adb shell input keyevent 3")
        time.sleep(10)

    def Enter_Radio_Screen(self):
        print("#Entered Radio_Screen.")
        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bRadio_sMainLauncher[0]) + " " + str(bRadio_sMainLauncher[1]))
        time.sleep(3)
        ### Radio screen으로 정상 진입 했는지 image 비교.
        '''
        if camera.camera_waitDetectImage('./referenceImage/BootImage.png', 10, True, 'Radioscreen'):
            print("This is RadioScreen")
        else:
            print("This is NOT RadioScreen")
        '''


    def Enter_Refresh(self):
        print("#Refresh")
        os.system("adb shell input tap " + str(bRefresh[0]) + " " + str(bRefresh[1]))
        time.sleep(3)
        print("#Refresh")
        os.system("adb shell input tap " + str(bRefresh[0]) + " " + str(bRefresh[1]))
        time.sleep(3)

    ##### Avtovaz꺼..
    def Enter_USB_Music_Screen(self, wait_time=3):
        print("#Entered USB Music Screen.")
        # Media 버튼
        self.Music_Button(3)
        self.Music_Mode_Button(3)

        # USB Icon tap
        print("# Tap USB Icon")
        os.system("adb shell input tap " + str(bUSB_Icon[0]) + " " + str(bUSB_Icon[1]))
        time.sleep(wait_time)

    def Enter_BTMusicPlay_Screen(self):
        print("#Entered BTMusicPlay_Screen.")
        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bMusic_sMainLauncher[0]) + " " + str(bMusic_sMainLauncher[1]))
        time.sleep(3)
        os.system("adb shell input tap " + str(bBTAudio_sMusicLauncher[0]) + " " + str(bBTAudio_sMusicLauncher[1]))
        time.sleep(3)

    def BTMusic_SeekDown(self, wait_time=3):
        print("#SeekDown in BT Music screen")
        os.system("adb shell input tap " + str(bBTAudio_sSeekdown[0]) + " " + str(bBTAudio_sSeekdown[1]))
        time.sleep(wait_time)

    def Enter_Tingban_Screen(self):
        print("#Entered Tingban Screen.")
        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bTingban_sMainLauncher[0]) + " " + str(bTingban_sMainLauncher[1]))
        time.sleep(3)

    def Tingban_SeekDown(self, wait_time=3):
        print("#SeekDown in Tingban Music screen")
        os.system("adb shell input tap " + str(bTingbanAudio_sSeekdown[0]) + " " + str(bTingbanAudio_sSeekdown[1]))
        time.sleep(wait_time)

    def Tingban_SeekUp(self, wait_time=3):
        print("#SeekUp in Tingban Music screen")
        os.system("adb shell input tap " + str(bTingbanAudio_sSeekUp[0]) + " " + str(bTingbanAudio_sSeekUp[1]))
        time.sleep(wait_time)

    def Enter_UserProfile_Screen(self):
        print("#Entered User Change_Screen > 2 > Guest > 1")
        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bUserProfile_sMainLauncher[0]) + " " + str(bUserProfile_sMainLauncher[1]))
        time.sleep(3)
        print("#User 2 change")
        os.system("adb shell input tap " + str(bUserTwo_sMainLauncher[0]) + " " + str(bUserTwo_sMainLauncher[1]))
        time.sleep(15)

        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bUserProfile_sMainLauncher[0]) + " " + str(bUserProfile_sMainLauncher[1]))
        time.sleep(3)
        print("#User Guest change")
        os.system("adb shell input tap " + str(bUserGuest_sMainLauncher[0]) + " " + str(bUserGuest_sMainLauncher[1]))
        time.sleep(15)

        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bUserProfile_sMainLauncher[0]) + " " + str(bUserProfile_sMainLauncher[1]))
        time.sleep(3)
        print("#User 1 change")
        os.system("adb shell input tap " + str(bUserOne_sMainLauncher[0]) + " " + str(bUserOne_sMainLauncher[1]))
        time.sleep(15)

    def Enter_Baidu_App_Screen(self):
        print("#Baidu_App_Screen")
        self.Swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        os.system("adb shell input tap " + str(bBaiduapps_sMainLauncher[0]) + " " + str(bBaiduapps_sMainLauncher[1]))
        time.sleep(3)

    def Enter_Baidu_VR_Screen(self):
        print("#Entered Baidu VR Screen")
        os.system("adb shell input tap " + str(bBaiduVR_sMainLauncher[0]) + " " + str(bBaiduVR_sMainLauncher[1]))
        time.sleep(3)

    def Enter_Baidu_Weather_Screen(self):
        print("#Entered Baidu Weather Screen")
        os.system("adb shell input tap " + str(bBaiduweather_sMainLauncher[0]) + " " + str(bBaiduweather_sMainLauncher[1]))
        time.sleep(3)

####### 삭 제 해 야 함

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
                matchResult = camera.camera_waitDetectImage(bootImage)

                if matchResult:
                    print("Detected BootImage!")
                else:
                    print("Booting Fail!")
                time.sleep(wait_time - 5)

                if wait_time > 40:
                    adb_connect = os.popen("adb devices").readlines()
                    print(adb_connect)
                    for line in adb_connect:
                        print(line)
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
            return False #booting fail 되어도 계속 진행하려면 return True 로 변경 해서 진행.
        else:
            aibox.bat_on()
            time.sleep(wait_time)

    def BAT_Off(self, wait_time=5):
        print("# Turned off Battery : "+str(wait_time)+"secs.")
        aibox.bat_off()
        time.sleep(wait_time)

    def Swipe(self, swipeX0, swipeY0, swipeX1, swipeY1, duration=swipeDuration):
        print("# Swipe Action!")
        os.system("adb shell input swipe " + str(swipeX0) + " " + str(swipeY0) + " " + str(swipeX1) + " " + str(swipeY1) + " " + str(duration))
        time.sleep(3)

























    '''
    # ## 이전 API #####################################################################################################
    def Play(self):
        print("#Selected 'Play' button.")
        """실제 Play 중일 때 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Play 동작 안됨으로 처리함"""
        if self.Ignore_Failure(self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPlay_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message=""))):
            os.system("adb shell input keyevent 85")
        time.sleep(3)

    def Pause(self):
        print("#Selected 'Pause' button.")
        """실제 Pause 중일 때 Pause 아이콘이 표시되어 Play 아이콘 표시되면 Pause 동작 안됨으로 처리함"""
        if self.Ignore_Failure(self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message=""))):
            os.system("adb shell input keyevent 85")
        time.sleep(3)

    #def Seek_Up(self):
    #    print("#Selected 'Seek_Up' button.")
    #    """Seek_Up 동작하면 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Seek_Up 동작 안됨으로 처리함"""
    #    os.system("adb shell input keyevent 88")
    #    time.sleep(3)
    #    self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Seek_Up wasn't operated."))

    #def Seek_Down(self):
    #    print("#Selected 'Seek_Down' button.")
    #    """Seek_Down 동작하면 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Seek_Down 동작 안됨으로 처리함"""
    #    os.system("adb shell input keyevent 87")
    #    time.sleep(3)
    #    self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Seek_Down wasn't operated."))

    def Fast_Rewind(self):
        print("#Selected 'Fast_Rewind' button.")
        """Fast_Rewind 동작하면 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Fast_Rewind 동작 안됨으로 처리함"""
        os.system("adb shell input keyevent 89")
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Fast_Rewind wasn't operated."))

    def Fast_Forward(self):
        print("#Selected 'Fast_Forward' button.")
        """Fast_Forward 동작하면 Play 아이콘이 표시되어 Pause 아이콘 표시되면 Fast_Forward 동작 안됨으로 처리함"""
        os.system("adb shell input keyevent 90")
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bPause_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Fast_Forward wasn't operated."))

    def Enter_Home_Screen(self):
        print("#Entered Home_Screen.")
        if self.Ignore_Failure(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_homescreen.jpg", timeout=3, region=None, threshold=0.9, failure_message="")) == False:
            os.system("adb shell input keyevent 3")
            time.sleep(3)
        if self.Ignore_Failure(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_homescreen.jpg", timeout=3, region=None, threshold=0.9, failure_message="")) == False:
            self.cis.swipe(swipeLeft[0], swipeLeft[1], swipeLeft[2], swipeLeft[3], duration=swipeDuration)
            time.sleep(3)
            self.cis.swipe(swipeLeft[0], swipeLeft[1], swipeLeft[2], swipeLeft[3], duration=swipeDuration)
            time.sleep(3)

    def Enter_QQMusic_Screen(self):
        print("#Entered QQMusic_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bQQMusic_sMainLauncher[0], bQQMusic_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_iQQMusic_sQQMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="The system didn't enter QQMusic App."))

    def Enter_MusicMain_Screen(self, usb_port):
        print("#Entered MusicMain_Screen.")
        usb_text = "[Issue] USB" + str(usb_port) + " wasn't recognized."
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bMusic_sMainLauncher[0], bMusic_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bUSB_sMusicLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message=usb_text))

    def Enter_USBMusicPlay_Screen(self, usb_port=1):
        print("#Entered USBMusicPlay_Screen.")
        usb_text = "[Issue] USB"+str(usb_port)+" wasn't recognized."
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bMusic_sMainLauncher[0], bMusic_sMainLauncher[1])
        time.sleep(5)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bUSB_sMusicLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message=usb_text))
        self.cis.tap(bUSB_sMusicLauncher[0], bUSB_sMusicLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_info_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="There is no file information.("+str(usb_port)+")"))

    def Enter_USBMusicPlay_Screen_WithoutComparingFileInformation(self, usb_port=1):
        print("#Entered USBMusicPlay_Screen_WithoutComparingFileInformation.")
        usb_text = "[Issue] USB"+str(usb_port)+" wasn't recognized."
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bMusic_sMainLauncher[0], bMusic_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bUSB_sMusicLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message=usb_text))
        self.cis.tap(bUSB_sMusicLauncher[0], bUSB_sMusicLauncher[1])
        time.sleep(3)

    def Enter_USBMusicPlay_Screen_WithoutUSB(self, usb_port=1):
        print("#Entered USBMusicPlay_Screen_WithoutUSB.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bMusic_sMainLauncher[0], bMusic_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bUSB_sMusicLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message=""))
        self.cis.tap(bUSB_sMusicLauncher[0], bUSB_sMusicLauncher[1])
        time.sleep(3)

    def Enter_USBMusicList_Screen(self):
        print("#Entered USBMusicList_Screen.")
        self.cis.tap(bList_sMediaMusic[0], bList_sMediaMusic[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_i3000files_sMusic.jpg", timeout=3, region=None, threshold=0.9, failure_message="Media files wasn't recognized."))

    def Enter_BTMusicPlay_Screen(self):
        print("#Entered BTMusicPlay_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bMusic_sMainLauncher[0], bMusic_sMainLauncher[1])
        self.cis.tap(bBTAudio_sMusicLauncher[0], bBTAudio_sMusicLauncher[1])
        time.sleep(3)

    def Enter_USBImagePlay_Screen(self):
        print("#Entered USBImagePlay_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bImage_sMainLauncher[0], bImage_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bUSB_sImageLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message="The USB was not recognized."))
        self.cis.tap(bUSB_sImageLauncher[0], bUSB_sImageLauncher[1])
        time.sleep(3)

    def Enter_USBVideoPlay_Screen(self):
        print("#Entered USBVideoPlay_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bVideo_sMainLauncher[0], bVideo_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bUSB_sVideoLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message="The USB was not recognized."))
        self.cis.tap(bUSB_sVideoLauncher[0], bUSB_sVideoLauncher[1])
        time.sleep(3)

    def Enter_Radio_Screen(self):
        print("#Entered Radio_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bRadio_sMainLauncher[0], bRadio_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_radio.jpg", timeout=3, region=None, threshold=0.9, failure_message="It's not radio mode."))

    def Enter_Carlife_Screen_Android(self):
        print("#Entered Carlife_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bCarlife_sMainLauncher[0], bCarlife_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_CarlifeScreen_Android.jpg", timeout=10, region=None, threshold=0.9, failure_message="It didn't connect mobile."))

    def Enter_Carlife_Screen_IOS(self):
        print("#Entered Carlife_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bCarlife_sMainLauncher[0], bCarlife_sMainLauncher[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_CarlifeScreen_IOS.jpg", timeout=5, region=None, threshold=0.9, failure_message="It didn't connect mobile."))

    def Enter_BT_Setting_Screen(self):
        print("#Entered BT_Setting_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bSetting_sMainLauncher[0], bSetting_sMainLauncher[1])
        time.sleep(3)
        self.cis.tap(bBTSetting_sSetting[0], bBTSetting_sSetting[1])
        time.sleep(3)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_iBT_sBTSetting.jpg", timeout=3, region=None, threshold=0.9, failure_message="It didn't enter BTscreen."))

    def Enter_UserProfile_Screen(self):
        print("#Entered UserProfile_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bUserProfile_sMainLauncher[0], bUserProfile_sMainLauncher[1])
        time.sleep(3)

    def Enter_SystemLanguage_Screen(self):
        print("#Entered SystemLanguage_Screen.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bSetting_sMainLauncher[0], bSetting_sMainLauncher[1])
        time.sleep(3)
        self.cis.tap(bSystemLanguage_sSetting[0], bSystemLanguage_sSetting[1])
        time.sleep(3)

    def Enter_Navigation_Screen(self):
        print("#Entered Navigation_Screen.")
        self.cis.tap(bNavigation_sMainLauncher[0], bNavigation_sMainLauncher[1])
        time.sleep(3)

    def Click_Split_Screen(self, wait_time=0.2):
        print("#Clicked Split_Screen : " + str(wait_time) + " seconds.")
        self.cis.tap(bSplit_sNavigation[0], bSplit_sNavigation[1])
        time.sleep(wait_time)

    def BT_Turn_On(self, wait_time=1):
        print("#Turned on BT : "+str(wait_time)+"secs.")
        self.cis.tap(bBTTurnOn_sBTSetting[0], bBTTurnOn_sBTSetting[1])
        time.sleep(wait_time)
        if wait_time >= 10:
            self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bBTTurnOn_sBTSetting.jpg", timeout=10, region=None, threshold=0.9, failure_message="It didn't on BT : "+str(wait_time)+" seconds."))

    def BT_Turn_Off(self, wait_time=1):
        print("#Turned off BT : "+str(wait_time)+"secs.")
        self.cis.tap(bBTTurnOff_sBTSetting[0], bBTTurnOff_sBTSetting[1])
        time.sleep(wait_time)
        if wait_time >= 3:
            self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bBTTurnOff_sBTSetting.jpg", timeout=3, region=None, threshold=0.9, failure_message="It didn't off BT : "+str(wait_time)+" seconds."))

    def Enter_Call_Mode(self):
        print("#Entered Call_Mode.")
        self.cis.swipe(swipeRight[0], swipeRight[1], swipeRight[2], swipeRight[3], duration=swipeDuration)
        time.sleep(3)
        self.cis.tap(bCall_sMainLauncher[0], bCall_sMainLauncher[1])
        time.sleep(5)
#        os.system("adb shell input keyevent 5")
#        time.sleep(3)

    def Exit_Call_Mode(self):
        print("#Exited Call_Mode.")
        os.system("adb shell input keyevent 6")
        time.sleep(3)

    def ACC_On(self, wait_time=40):
        print("# Turned on ACC : "+str(wait_time)+"secs.")
        aibox.acc_on()
        """if wait_time >= 3:
            time.sleep(3)
            # self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_boot_image.jpg", timeout=3, region=None, threshold=0.9, failure_message="The booting image wasn't displayed."))
            if wait_time >= 80:
                time.sleep(43)
                # self.cis.tap(bQRCode_sMainLauncher[0], bQRCode_sMainLauncher[1])
                time.sleep(5)
                # self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_BTmobile_sMainLauncher.jpg", timeout=2, region=None, threshold=0.9, failure_message="BT mobile isn't connected."))
                time.sleep(wait_time - 52)
            else:
                time.sleep(wait_time-3)
        else:
            time.sleep(wait_time)"""
        time.sleep(wait_time)

    def ACC_Off(self, wait_time=3):
        print("# Turned off ACC : "+str(wait_time)+"secs.")
        aibox.acc_off()
        """if wait_time >= 3:
            self.cis.keep(lambda: self.cis.wait_single_color(timeout=3, threshold=127, interval=0.1, failure_message="It didn't off ACC."))
            time.sleep(wait_time-3)
        else:
            time.sleep(wait_time)"""
        time.sleep(wait_time)

    def DISP_On(self, wait_time=2):
        print("#Turned on DISP : "+str(wait_time)+"secs.")
        os.system("adb shell auto_svc key 26 0.5")
        time.sleep(wait_time-0.5)

    def DISP_Off(self, wait_time=5):
        print("#Turned off DISP : "+str(wait_time)+"secs.")
        if wait_time >= 5:
            self.cis.swipe(swipeRoofPopupDown[0], swipeRoofPopupDown[1], swipeRoofPopupDown[2], swipeRoofPopupDown[3], duration=swipeDuration)
            time.sleep(1)
            if self.Ignore_Failure(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_bDisplay_sControlCenter.jpg", timeout=1, region=None, threshold=0.9, failure_message="")) == False:
                self.cis.swipe(swipeRoofPopupDown[0], swipeRoofPopupDown[1], swipeRoofPopupDown[2], swipeRoofPopupDown[3], duration=swipeDuration)
                time.sleep(1)
            self.cis.tap(bDisplay_sControlCenter[0], bDisplay_sControlCenter[1])
            time.sleep(1)
            self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_TOD_screenxxxxxx.jpg", timeout=2, region=None, threshold=0.9, failure_message="The system didn't enter TOD mode with DISP off : "+str(wait_time)+"secs"))
            time.sleep(wait_time-5)
        else:
            self.cis.swipe(swipeRoofPopupDown[0], swipeRoofPopupDown[1], swipeRoofPopupDown[2], swipeRoofPopupDown[3], duration=swipeDuration)
            time.sleep(1)
            self.cis.tap(bDisplay_sControlCenter[0], bDisplay_sControlCenter[1])
            time.sleep(1)
            time.sleep(wait_time-1)

    def Power_On(self, wait_time=5):
        print("#Turned on 'Power' : "+str(wait_time)+"secs.")
        if wait_time >= 2:
            if self.Ignore_Failure(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_TOD_screenxxxxxx.jpg", timeout=1, region=None, threshold=0.9, failure_message="")):
                os.system("adb shell auto_svc key 26 0.5")
            time.sleep(wait_time-1.5)
        else:
            os.system("adb shell auto_svc key 26 0.5")
            time.sleep(wait_time)

    def Enter_AVOff_Screen(self):
        print("#Entered AVOff_Screen.")
        if self.Ignore_Failure(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_iAVOff_sMainLauncher.jpg", timeout=2, region=None, threshold=0.9, failure_message="")) == False:
            os.system("adb shell auto_svc key 26 0.5")
        time.sleep(2)
        self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_iAVOff_sMainLauncher.jpg", timeout=3, region=None, threshold=0.9, failure_message="The system didn't enter AV off mode."))

    def Enter_PowerOff_Screen(self, wait_time=10):
        print("#Entered PowerOff_Screen. : "+str(wait_time)+"secs.")
        if self.Ignore_Failure(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_TOD_screenxxxxxx.jpg", timeout=1, region=None, threshold=0.9, failure_message="")) == False:
            os.system("adb shell auto_svc key 26 1")
        if wait_time >= 10:
            self.cis.keep(lambda: self.cis.wait_image("/opt/hats/scripts/dn8c/sqe/image/IMG_TOD_screenxxxxxx.jpg", timeout=5, region=None, threshold=0.9, failure_message="The system didn't enter TOD mode with power off : "+str(wait_time)+"secs"))
            time.sleep(wait_time-6)
        else:
            time.sleep(wait_time-1)

    '''
api_class = API_Class()

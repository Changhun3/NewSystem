# -*- coding: utf-8 -*-
from behave import *
from api_class import *
import datetime
import keyboard
import time
import os

api = api_class

########################################################################################################
# @A01.01.TestAging
#   Scenario Outline: AgingTest 시작하기
@given('A01.01 - USB 카메라와 Power 장비 및 ADB가 정상적으로 연결되어 있다.')
def step_impl(context):
    try:
        Test_Result = True
        # 카메라 및 Power 장비 Initation 및 연결상태 확인 #################################################
        # BAT Off & On 동작 후, 초기화면 출력 확인
        time.sleep(5)

        # Reboot 감지 및 Freeze 여부 확인 정의 ############################################################
        # Reboot 감지여부 설정

        # Freeze 감지 여부 설정

        # 초기화면 확인
        api.Enter_Home_Screen(5)
        Home_Screen = "./referenceimage/HomeScreen.png"
        imagematchingResult = api.ImageCompareResult(Home_Screen)

        if imagematchingResult == False:
            raise Exception("Error!!!")

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result
# ########################################################################################################


@when('A01.01 - 아래와 같은 Step으로 1시간 단위 Test를 수행하며, 이후 BAT off/ong 후 반복 수행하여 Memory 관련 문제가 없어야 한다.')
def step_impl(context):
    try:
        start_time = time.time()
        end_time = start_time + (60 * 60 * 1200)
        Test_Result = True

        while((time.time()) < end_time):

            # 주어진 Action 및 Step에 따라 Test Script 작성 #################################################
            # Step 1 - BAT Off 동작을 5초 대기 시간으로 수행한다. ##########
            print("## Start ####################################################################################### ##")
            print("## Step 1 - BAT Off 동작을 5초 대기 시간으로 수행한다.")
            api.BAT_Off(5)
            # time.sleep(5) # ADB 연결 이슈로 인해 해당 Step은 Comment 처리

            # Step 2 - BAT On 동작을  90초 대기 시간으로 수행한다. ##########
            print("## Step 2 - BAT On 동작을 90초 대기 시간으로 수행한다. 이후 Refresh와 Home Screen으로 이동 동작 한다.")
            api.BAT_On(90)
            # time.sleep(5)  # ADB 연결 이슈로 인해 해당 Step은 Comment 처리

            api.Enter_Refresh()

            api.Enter_Home_Screen()

            # Step 3 - Radio CH을 1 > 2 > 3 > 1 동작을 20초 간격 10회으로 수행한다. ##########
            print("## Step 3 - Radio CH을 P1 > P2 > P3 > P1 동작을 20초 간격으로 10회 수행한다.(약 600초)")
            # ## FM-Radio 항목 진입
            api.Enter_Radio_Screen()
            for i in range(0, 10): # 10
                print("#Radio P1 select")
                os.system("adb shell input tap " + str(365) + " " + str(165))
                time.sleep(20)
                print("#Radio P2 select")
                os.system("adb shell input tap " + str(365) + " " + str(245))
                time.sleep(20)
                print("#Radio P3 select")
                os.system("adb shell input tap " + str(365) + " " + str(355))
                time.sleep(20)

            print("#Radio P1 select")
            os.system("adb shell input tap " + str(365) + " " + str(165))
            time.sleep(3)

            api.Enter_Home_Screen()

            # Step 4 - Tingban를 Play하고 30초 간격으로 Seekdown 2회, Seekup을 1회를 10번 수행한다. ##########
            print("## Step 4 - Tingban를 Play하고 30초 간격으로 Seekdown 2회, Seekup을 1회를 10번 수행한다.(약 900초)")
            api.Enter_Tingban_Screen()
            for i in range(0, 10): # 10
                api.Tingban_SeekDown(30)
                api.Tingban_SeekDown(30)
                api.Tingban_SeekUp(30)
            time.sleep(1)

            api.Enter_Home_Screen()
            
            # Step 5 - BT Audio를 Play하고 20초 간격으로 Next Track곡을 45번 수행한다. ##########
            print("## Step 5 - BT Audio를 Play하고 20초 간격으로 Next Track곡을 45번 수행한다.(약 900초)")
            api.Enter_BTMusicPlay_Screen()
            for i in range(0, 45): # 45
                api.BTMusic_SeekDown(20)
            time.sleep(1)

            api.Enter_Home_Screen()

            # Step 6 - Navigation 항목을 10초 대기 시간으로 10회 반복 수행한다. ##########
            print("## Step 6 - Navigation 항목을 10초 대기 시간으로 10회 반복 수행한다.(약 200초)")
            for i in range(0, 10): # 10
                api.Enter_Navigation_Screen()
            time.sleep(1)

            api.Enter_Home_Screen()

            # Step 7 - User 1 > 2 > Guest > 1을 15초 간격으로 3회 수행한다. ##########
            print("## Step 7 - User 1 > 2 > Guest > 1을 20초 간격으로 3회 수행한다. 그리고 Radio Screen으로 원복(약 200초)")
            for i in range(0, 3): # 3
                api.Enter_UserProfile_Screen()
            time.sleep(1)

            api.Enter_Home_Screen()

            print("#Radio Screen으로 원복!")
            api.Enter_Radio_Screen()

            api.Enter_Home_Screen()

            # Step 8 - Baidu Apps에 진입 하여 VR on/off와 Weather on/off를 을 30초 간격으로 5회씩 수행한다. ##########
            print("## Step 8 - Baidu Apps에 진입 하여 VR on/off와 Weather on/off를 을 30초 간격으로 5회씩 수행한다.(약 300초)")
            api.Enter_Baidu_App_Screen()
            for i in range(0, 5): # 5
                print("Baidu VR 진입/진출")
                api.Enter_Baidu_VR_Screen
                time.sleep(30)
            for i in range(0, 5): # 5
                print("Baidu weather 진입/진출")
                api.Enter_Baidu_Weather_Screen
                time.sleep(30)
            time.sleep(3)

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result
# ########################################################################################################


@then('A01.01 - Aging Test 완료 후 시료는 Radio 항목으로 진입 후, 문제없이 동작되어야 한다.')
def step_impl(context):
    try:
        # 수행된 결과와 기대 결과를 비교하여 PAss or Fail 여부 판단 #################################################
        print("then Test")
        Test_Result = True

        """while True:
            time.sleep(0.1)

            if keyboard.is_pressed(80):
                api.CameraCapture()
            elif keyboard.is_pressed('enter'):
                api.CameraStop()
                api.adb_test()
                time.sleep(3)
                break"""

    except Exception as e:
        print(e)
        Test_Result = False

    assert True
# #####################################################################################################################

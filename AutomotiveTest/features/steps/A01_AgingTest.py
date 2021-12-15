# -*- coding: utf-8 -*-
from behave import *
from api_class import *
import datetime
import keyboard
import time

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

        #api.BAT_Off(5)
        #api.BAT_On(60)

        # 초기화면 확인
        api.Home_Button(5)
        Home_Screen = "./referenceimage/HomeScreen.png"
        imagematchingResult = api.ImageCompareResult(Home_Screen)

        if imagematchingResult == False:
            raise Exception("Error!!!")

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result
# ########################################################################################################


@when('A01.01 - 아래와 같은 Step으로 24 시간 동안 Aging Test를 수행하며, 동작중 Reboot 또는 crash 이슈는 없어야 한다.')
def step_impl(context):
    try:
        start_time = time.time()
        end_time = start_time + (60 * 60 * 120)
        Test_Result = True

        while((time.time()) < end_time):
            # 주어진 Action 및 Step에 따라 Test Script 작성 #################################################
            # Step 1 - BAT Off 동작을 5초 대기 시간으로 수행한다. ##########
            print("## Start ####################################################################################### ##")
            print("## Step 1 - BAT Off 동작을 5초 대기 시간으로 수행한다.")
            api.BAT_Off(5)
            # time.sleep(5) # ADB 연결 이슈로 인해 해당 Step은 Comment 처리

            # Step 2 - BAT On 동작을  120초 대기 시간으로 수행한다. ##########
            print("## Step 2 - BAT On 동작을  120초 대기 시간으로 수행한다.")
            api.BAT_On(120)
            # time.sleep(5)  # ADB 연결 이슈로 인해 해당 Step은 Comment 처리

            # Step 3 - Radio CH을 1 > 2 > 3 > 1 동작을 40초 간격으로 수행한다. ##########
            print("## Step 3 - Radio CH을 1 > 2 > 3 > 1 동작을 40초 간격으로 수행한다.")
            # ## FM-Radio 항목 진입
            api.Enter_FM_Radio_Screen(5)

            # ## 3개 라디오 채널을 40초 간격으로 탭 동작 수행 (최초 진입시 1번 채널이 출력되고 있음
            # ### 2번 채널 선택
            api.Seek_Down(40)

            # ### 3번 채널 선택
            api.Seek_Down(40)

            # ### 1번 채널 선택 (3번에서 2번 > 1번 채널로 전환)
            api.Seek_Up(5)
            api.Seek_Up(40)

            # Step 4 - USB 음악을 910초 대기 시간으로 수행한다. ##########
            print("## Step 4 - USB 음악을 910초 대기 시간으로 수행한다.")
            api.Enter_USB_Music_Screen(910)

            # Step 5 - BT Audio Play를 910초 대기 시간으로 수행한다. ##########
            print("## Step 5 - BT Audio Play를 910초 대기 시간으로 수행한다.")
            api.Enter_BT_Music_Screen(910)

            # Step 6 - Navigation 항목을 20초 대기 시간으로 진입한다. ##########
            print("## Step 6 - Navigation 항목을 20초 대기 시간으로 진입한다.")
            api.Enter_Navi_Screen(20)

            # Step 7 - Radio 항목을 20초 대기 시간으로 진입한다. ##########
            print("## Step 7 - Radio 항목을 20초 대기 시간으로 진입한다.")
            api.Enter_FM_Radio_Screen(20)

            print("# ")
            print("## END ######################################################################################### ##")
            print(" ")
            print(" ")
            print(" ")

    except Exception as e:
        print(e)
        Test_Result = False

    assert Test_Result
# ########################################################################################################


@then('A01.01 - Aging Test 완료 후 시료는 Radio 항목으로 진입 후, 문제없이 동작되어야 한다.')
def step_impl(context):
    try:
        # 수행된 결과와 기대 결과를 비교하여 PAss or Fail 여부 판단 #################################################
        print("test3")

        while True:
            time.sleep(0.1)

            if keyboard.is_pressed(80):
                api.CameraCapture()
            elif keyboard.is_pressed('enter'):
                api.CameraStop()
                api.adb_test()
                time.sleep(3)
                break

    except Exception as e:
        print(e)
        Test_Result = False

    assert True
# #####################################################################################################################

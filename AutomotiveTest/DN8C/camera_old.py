# -*- coding: utf-8 -*-
import datetime
import time
import cv2

class USBCamera():
    #RUN_TIME_ENV = os.environ.get("RUN_TIME_ENV", None)
    #print("RUN_TIME_ENV = %s" % RUN_TIME_ENV)

    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    image_frame = None
    test_value = True

    def camera_start(self):
        while self.test_value:
            #capture = cv2.VideoCapture(1)
            ret, frame = self.capture.read()
            self.image_frame = frame
            cv2.imshow("VideoFrame", self.image_frame)
            key = cv2.waitKey(50)

    def camera_capture(self):
        #print("이미지 캡쳐")
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        cv2.imwrite("./data/" + "Capture" + str(now) + ".png", self.image_frame)
        #return ("./data/" + "Capture" + str(now) + ".png", self.image_frame)

    def camera_issue(self):
        #print("Error! 이미지 캡쳐")
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        cv2.imwrite("./data/" + "Issue_" + str(now) + ".png", self.image_frame)

    def camera_stop(self):
        #print("카메라 정지")
        #print("## 카메라 1번")
        self.test_value = False
        time.sleep(1)
        #print("## 카메라 2번")
        self.capture.release()
        #print("## 카메라 3번")
        cv2.destroyWindow("VideoFrame")
        #print("## 카메라 4번")

    def camera_detectImage(self, detectImagePath):
        cv2.imwrite("./data/temp.png", self.image_frame)
        sourceimage_temp = cv2.imread("./data/temp.png")
        sourceimage = cv2.cvtColor(sourceimage_temp, cv2.COLOR_RGB2GRAY)

        template_temp = cv2.imread(detectImagePath)
        template = cv2.cvtColor(template_temp, cv2.COLOR_RGB2GRAY)

        height, width, channel = sourceimage_temp.shape
        #print(height, width, channel)

        res = cv2.matchTemplate(sourceimage, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #print(max_val)

        if(max_val > 0.70): # 기존 0.96
            print("Pass")
            print("mac_val :: " + str(max_val))
            return True
        else:
            print("Fail")
            print("mac_val :: " + str(max_val))
            return False

    def camera_waitImage(self, detectImagePath, waitTime=3):
        startTime = time.time()
        endTime = startTime + waitTime

        while(time.time() < endTime):
            cv2.imwrite("./data/temp.png", self.image_frame)
            sourceimage_temp = cv2.imread("./data/temp.png")
            sourceimage = cv2.cvtColor(sourceimage_temp, cv2.COLOR_RGB2GRAY)

            template_temp = cv2.imread(detectImagePath)
            template = cv2.cvtColor(template_temp, cv2.COLOR_RGB2GRAY)

            height, width, channel = sourceimage_temp.shape
            #print(height, width, channel)

            res = cv2.matchTemplate(sourceimage, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            #print(min_val)
            print(max_val)

            if (max_val > 0.96):
                print("# Find Match Image!")
                return True

            time.sleep(1)

        print("# No Match Image")
        return False


    def camera_searchLocation(self, detectImagePath):
        cv2.imwrite("./data/temp.png", self.image_frame)
        sourceimage_temp = cv2.imread("./data/temp.png")
        sourceimage = cv2.cvtColor(sourceimage_temp, cv2.COLOR_RGB2GRAY)

        template_temp = cv2.imread(detectImagePath)
        template = cv2.cvtColor(template_temp, cv2.COLOR_RGB2GRAY)

        height, width, channel = template_temp.shape
        print(height, width, channel)

        res = cv2.matchTemplate(sourceimage, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(max_val)

        if(max_val > 0.96):
            print("# Image Detect!")
            top_left = max_loc
            center = (top_left[0] + int(width/2), top_left[1] + int(height/2))
            print(center)
            return center
        else:
            print("# No search")
            return False


camera = USBCamera()
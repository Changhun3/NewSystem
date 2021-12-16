# -*- coding: utf-8 -*-
from pypylon import pylon
import datetime
import time
import cv2

class USBCamera():
    # conecting to the first available camera
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

    # Grabing Continusely (video) with minimal delay
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
    converter = pylon.ImageFormatConverter()

    # converting to opencv bgr format
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    image_frame = None
    test_value = True
    grabResult = None

    def camera_start(self):
        while self.test_value:
            self.grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            # Access the image data
            image = self.converter.Convert(self.grabResult)
            self.image_frame = image.GetArray()
            cv2.namedWindow('VideoFrame', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('VideoFrame', 960, 600)
            cv2.imshow('VideoFrame', self.image_frame)
            k = cv2.waitKey(20)

    def camera_capture(self):
        #print("이미지 캡쳐")
        now = datetime.datetime.now().strftime("%Y/%m/%d_%H-%M-%S")
        cv2.imwrite("./data/" + "Capture" + str(now) + ".png", self.image_frame)
        #return ("./data/" + "Capture" + str(now) + ".png", self.image_frame)

    def camera_issue(self):
        #print("Error! 이미지 캡쳐")
        now = datetime.datetime.now().strftime("%Y/%m/%d_%H-%M-%S")
        cv2.imwrite("./data/" + "Issue_" + str(now) + ".png", self.image_frame)

    def camera_stop(self):
        #print("카메라 정지")
        #print("## 카메라 1번")
        self.test_value = False
        time.sleep(1)
        #print("## 카메라 2번")
        self.grabResult.release()
        self.camera.StopGrabbing()
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

        if(max_val > 0.96):
            print("Pass")
            print("mac_val :: " + str(max_val))
            return True
        else:
            print("Fail")
            print("mac_val :: " + str(max_val))
            return False

    def camera_waitImage(self, detectImagePath, waitTime=10):
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

            time.sleep(0.7)

        print("# No Match Image")
        now = datetime.datetime.now().strftime("%Y/%m/%d_%H-%M-%S")
        cv2.imwrite("./data/" + "No_Boot_Image_" + str(now) + ".png", self.image_frame)
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
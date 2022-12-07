from mobiusAPI import *
from datetime import datetime
import base64
import cv2

# 카메라 정상 여부
def getCameraState(cap):
    return cap.isOpened()

def imgSave(cap,pwm):
    # 이미지 저장
    ret, image = cap.read()
    now = datetime.now()
    name = "Image/"
    name += str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + ".jpg"
    cv2.imwrite(name,image)
    return name

def imgEncode(name):
     content = base64.b64encode(open("/home/pi/Desktop/SRS-IOT/" + name, "rb").read())


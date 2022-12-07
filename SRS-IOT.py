from RecycleAI import *
from mobiusAPI import *
from Servo import *
from lineSensor import *
from dcMotor import *
from Camera import *
from WeightSensor import *
from deviceState import *
import RPi.GPIO as GPIO
import time


servo = 12
ENA = 25
ENB = 2 
IN1 = 23  
IN2 = 6  
IN3 = 16 
IN4 = 26 

IR1 = 27
IR2 = 4
IR3 = 17

start, dest = 0, 0

weight = 0

addr = ''

def autoDriving(pwm1, pwm2):
    while True:
        line_status1, line_status2, line_status3 = readLineSenSorStatus()
        if line_status1 == 0 and line_status3 == 0:
            goStraight(pwm1, pwm2, line_status2)
        elif line_status1 ==1 and line_status3 == 1:
            stop()
            break
        elif line_status1 == 1:
            turnLeft()
        else:
            turnRight()

def trangerAIresult(result):
    createContentInstance('robot1', '/AIresult', result, addr)

def tranferWeight(weight):
    createContentInstance('robot1', '/weightdata/cnt1', weight, addr)

def tranferImage(name):
    createContentInstance('robot1', '/imagedata/RAWdata', name[6:-4], addr)

def transferWifiState():
    # 인터넷 연결 시 날짜, 시간 모비우스로 전송
    now = datetime.now()
    content = str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    if getWifiState():
        createContentInstance('robot1', '/status/wificonn', content, addr)  


def transferCameraState():
    # 카메라 연결 시 날짜, 시간 모비우스로 전송
    now = datetime.now()
    content = str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    if getCameraState():
        createContentInstance('robot1', '/status/camstat', content, addr) 

def transferCPUGPUTemp():
    # CPU, GPU 온도 모비우스로 전송
    createContentInstance('robot1', '/status/CPUdegree', getRasberyPiCPUTemp(), addr)
    createContentInstance('robot1', '/status/GPUdegree', getRasberyPiGPUTemp(), addr)

def transferWifiState():
    # 인터넷 연결 시 날짜, 시간 모비우스로 전송
    now = datetime.now()
    content = str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    createContentInstance('robot1', '/status/wificonn', content, addr)  


def getDestination():
    return getContentInstance('robot1', '/spacedata/la', addr)  

def tranferArival(destination):
    createContentInstance('robot1', '/spacedata/arrival', destination, addr)  


def init():
    
    cap = cv2.VideoCapture(0)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    
    pwm1 = GPIO.PWM(ENA, 100)
    pwm2 = GPIO.PWM(ENB, 100)
    pwm1.start(0)
    pwm2.start(0)

    time.sleep(2)
    GPIO.setup(IR1, GPIO.IN)
    GPIO.setup(IR2, GPIO.IN)
    GPIO.setup(IR3, GPIO.IN)

    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    
    GPIO.setup(servo, GPIO.OUT)

    pwm3 = GPIO.PWM(servo, 50)
    
    return pwm1, pwm2, pwm3, cap


def work():
    pwm1, pwm2, pwm3, cap= init()
    try:
        while True:
            dest = getDestination()
            if dest == "":
                continue
            dest = int(dest)
            if start != dest:
                autoDriving(pwm1, pwm2)
            tranferArival(str(dest))
            classfication = imgSave(pwm3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        cap.release()


if __name__ == "__main__":
    work()
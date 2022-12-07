import time
import RPi.GPIO as GPIO

def turnServo(pwm, recycle_result):
    pwm.start(3.0)
    if recycle_result == "플라스틱":
        pwm.ChangeDutyCycle(12.5)
        time.sleep(0.6)
    elif recycle_result == "유리병":
        pwm.ChangeDutyCycle(3)
        time.sleep(0.6)
    else:
        pwm.ChangeDutyCycle(7.5)
        time.sleep(0.6)
    pwm.stop()
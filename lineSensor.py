import RPi.GPIO as GPIO

def readLineSenSorStatus(IR1, IR2, IR3):
    return GPIO.input(IR1), GPIO.input(IR2), GPIO.input(IR3)
import RPi.GPIO as GPIO

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

def stop():
    # 모터 멈춤
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.HIGH)

def goStraight(pwm1, pwm2, line_status2):
    pwm1.ChangeDutyCycle(80)
    pwm2.ChangeDutyCycle(100)
    
    # 양쪽 바퀴 정방향
    if line_status2 == 0:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
    
    # 왼쪽 바퀴 역방향, 오른쪽 바퀴 정방향
    else:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH) 

def turnRight():
    
    #오른쪽 바퀴 역방향, 왼쪽 바퀴 정방향
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    
    
    


def turnLeft():
    
    #왼쪽 바퀴 역방향, 오른쪽 바퀴 정방향 
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
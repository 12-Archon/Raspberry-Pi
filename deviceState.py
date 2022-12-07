import subprocess

#인터넷 연결 상태
def getWifiState():
    # received 패킷 수 확인
    result = subprocess.check_output(['ping', '-c1',  'google.com']).decode('ascii').split(',')
    rev = int(result[1][:2]) 
    
    # received 패킷이 있으면 True 반환, 없으면 False, 반환
    if rev != 0:  
        return True
    else:
        return False

#라즈베리파이 CPU온도측정
def getRasberyPiCPUTemp():
    data = subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp'])
    data = str(data[0:3])
    data = data[2:5]
    return str(int(data)/10)



#라즈베리파이 GPU온도측정
def getRasberyPiGPUTemp():
    data = subprocess.check_output(['vcgencmd', 'measure_temp'])
    data = str(data[5:9])
    data = data[2:6]
    return data
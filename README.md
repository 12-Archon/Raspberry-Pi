# Raspberry-Pi

## Device Architecture
 ![initial](https://user-images.githubusercontent.com/55491260/206272472-d94caf35-c98b-48b0-86f2-65192280421f.png) 
---------------------------
## Device State
1. internet connection status
2. CPU Temperature
3. GPU Temperature

---------------------------
## Servo Motor
1. Glass - PWM(3) 0degree 
2. Can - PWM(7.5) 90degree
3. plastic - PWM(12.5) 180degree


---------------------------
## DC Motor

### Funciton
1. stop
2. goStraight
3. turnLeft
4. turnRight


---------------------------
## Weight Sensor(Load Cell)

### Installation HX711py
```
git clone https://github.com/tatobari/hx711py.git
cd hx711py
python setup.py install
``` 
### Raspberry PI BCM
(DT, SCK) : (20, 21)

### How it works in robot
1. throw away the garbage, measure the weight, and send the value to the Mobius server
2. If the weight exceeds a certain value, move to the admin


---------------------------
## Line Sensor(TCRT 5000)

### Raspberry PI BCM
(left, center, right) = 27, 4, 17

### value 
black = 1
else = 0

---------------------------
## Camera


--------------------------
## AI
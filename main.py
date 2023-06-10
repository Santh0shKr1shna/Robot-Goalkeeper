import serial
import time
from Compvision import detectBall

# Connect with port here
port = 'com8'
arduino = serial.Serial(port, 115200)
time.sleep(1)

while True:
    pos = detectBall()
    arduino.write(str.encode(str(pos)))

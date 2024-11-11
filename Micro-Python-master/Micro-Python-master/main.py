'''
from machine import Pin
import time

# Motor A
motor1Pin1 = 18; 
motor1Pin2 = 19; 
enable1Pin = 14; 


p0=Pin(motor1Pin1, Pin.OUT);
p1=Pin(motor1Pin2, Pin.OUT);
p3=Pin(enable1Pin, Pin.OUT);

while True:
    #Move the DC motor forward at maximum speed
    p3.on()
    print("Moving Forward");
    p0.off()
    p1.on()
    time.sleep(1)
    # Stop the DC motor
    print("Motor stopped");
    p0.off()
    p1.off()
    time.sleep(1)

    #Move DC motor backwards at maximum speed
    print("Moving Backwards");
    p0.on()
    p1.off() 
    time.sleep(1)

  #Stop the DC motor
    print("Motor stopped");
    p0.off()
    p1.off()
    time.sleep(1)
'''
import machine
import time
led=machine.Pin(2,machine.Pin.OUT)
while True:
    led.value(1)
    time.sleep(5)
    led.value(0)
    time.sleep(5)
    


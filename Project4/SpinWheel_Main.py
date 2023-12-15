import os
import sys
import io
import time
import machine
from machine import ADC, Pin, PWM
from hardware import *
import M5
#from M5 import *


class Servo:
    # These defaults work for the standard TowerPro SG90
    __servo_pwm_freq = 50
    __min_u10_duty = 26
    __max_u10_duty = 123
    min_angle = 0
    max_angle = 180
    current_angle = 0.001
    
    def __init__(self, pin):
        self.__initialise(pin)

    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)

    def move(self, angle):
        angle = round(angle, 2)
        if angle == self.current_angle:
            return
        self.current_angle = angle
        duty_u10 = self.__angle_to_u10_duty(angle)
        self.__motor.duty(duty_u10)

    def __angle_to_u10_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty
    


servoshutter_pin = 38 
servo_st = Servo(servoshutter_pin) #ST = Shutter Servo

servomove_pin = 7
servo_mo = Servo(servomove_pin) #MO = Move Servo

angle_rest = 40 #servo_st rest
angle_push = 70 #servo_st push shutter
angle_move = 26 #servo_mo moves
angle_stop = 90 #serbo_mo stops

servo_st.move(angle_rest)
servo_mo.move(angle_stop)

M5.begin()

#def loop():
while True:
    M5.update()
    if M5.BtnA.wasPressed():
        print('button pressed..')
        for i in range(30):
            time.sleep(2)
            servo_mo.move(49)
            time.sleep(0.2)
            servo_mo.move(angle_stop)
            time.sleep(2)
    #print('hello')
    time.sleep_ms(100)
    

    
    #servo_mo.move(angle_stop)
    #time.sleep(1)
          
          
          
def map_value(in_val, in_min, in_max, out_min, out_max):
    # Map an input value (in_val) from one range to another
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    return max(min(int(v), out_max), out_min)


#if __name__ == '__main__':
#    while True:
#        loop()
import os
import sys
import io
import time
from machine import ADC, Pin, PWM

# Assuming you have the necessary methods from M5 stack already imported or defined somewhere

# Define the Servo class within the same script
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

# Now the rest of your script that uses the Servo class
servo_pin = 7  # Define the servo pin
servo = Servo(servo_pin)  # Initialize the servo on pin 8
light_adc = ADC(Pin(6), atten=ADC.ATTN_11DB)  # Initialize the ADC for the light sensor on pin 6


angle_rest = 40
angle_push = 130 #this is how much does the servo move
servo.move(130)  # straight up
#servo.move(120)  # about 90 degrees

shutter_state = 'released'

def loop():
    global shutter_state
    light_val = light_adc.read()
    adc_val_8bit = map_value(light_val, in_min=0, in_max=4095, out_min=0, out_max=255)
    print(adc_val_8bit)
    time.sleep_ms(100)
    if (adc_val_8bit > 190) and (shutter_state == 'released'):
        time.sleep_ms(2000)
        servo.move(angle_push)
        time.sleep_ms(500)
        servo.move(angle_rest)
        print('shutter Released')
        shutter_state = 'wind'
    elif (adc_val_8bit < 190) :
        shutter_state = 'released'
    
    
def map_value(in_val, in_min, in_max, out_min, out_max):
    # Map an input value (in_val) from one range to another
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    return max(min(int(v), out_max), out_min)

if __name__ == '__main__':
    while True:
        loop()

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

light_sensor_adc = None
angle_sensor_adc = None
light_sensor_val = None
angle_sensor_val = None

def setup():
    global light_sensor_adc, angle_sensor_adc, light_sensor_val, angle_sensor_val
    M5.begin()
    # configure ADC input for light sensor on pin G1 with 11dB attenuation:
    light_sensor_adc = ADC(Pin(1), atten=ADC.ATTN_11DB)
    # configure ADC input for angle sensor on pin G6 with 11dB attenuation:
    angle_sensor_adc = ADC(Pin(6), atten=ADC.ATTN_11DB)

def loop():
    global light_sensor_adc, angle_sensor_adc, light_sensor_val, angle_sensor_val
    M5.update()
    # read 12-bit analog value (0 - 4095 range) from light sensor:
    light_sensor_val = light_sensor_adc.read()
    # read 12-bit analog value (0 - 4095 range) from angle sensor:
    angle_sensor_val = angle_sensor_adc.read()
  
    # convert light_sensor_val from 12-bit to 8-bit (0 - 255 range):
    light_sensor_val_8bit = map_value(light_sensor_val, in_min=0, in_max=4095, out_min=0, out_max=255)
    # convert angle_sensor_val from 12-bit to 8-bit (0 - 255 range):
    angle_sensor_val_8bit = map_value(angle_sensor_val, in_min=0, in_max=4095, out_min=0, out_max=255)
  
    # print 8-bit ADC values for both sensors, ending with comma:
    #print('Lit',light_sensor_val_8bit, end=',  ')
    #print('Agl',angle_sensor_val_8bit, end=',  ')
    print(light_sensor_val_8bit, end=',')
    print(angle_sensor_val_8bit, end=',')
  
    # print built-in button value converted to integer:
    #print('Btn',int(BtnA.isPressed()))
    print(int(BtnA.isPressed()))
    time.sleep_ms(100)

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")





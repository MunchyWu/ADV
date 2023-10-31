# fade the brightness of an LED connected pin 1
# using for loops and Pulse Width Modulation (PWM)

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# global pwm1 variable:
pwm1 = None

def setup():
  global pwm1
  # initialize M5 board:
  M5.begin()
  # initialize PWM on pin 1 with default settings:
  pwm1 = PWM(Pin(1))
  # initialize PWM on pin 1 with frequency and duty parameters:
  # pwm1 = PWM(Pin(1), freq=20000, duty=512)

def loop():
  global pwm1
  # update M5 board:
  M5.update()
  # gradually increase led brightness in a loop:
  for i in range(100):
    # change the PWM duty cycle (pulse width) 
    # with increasing value of loop variable i:
    pwm1.duty(i)
    time.sleep_ms(10)
  # gradually decrease led brightness in a loop:
  for i in range(100):
    # change the PWM duty cycle (pulse width)
    # with decreasing value of 100 - i: 
    pwm1.duty(100 - i)
    time.sleep_ms(10)

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
import os, sys, io
import M5
from M5 import *
from hardware import *
import time


pin1 = None
pwm1 = None


b = None


def setup():
  global pin1, pwm1, b

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  pwm1 = PWM(Pin(1), freq=20000, duty=512)


def loop():
  global pin1, pwm1, b
  M5.update()
  for b in range(1, 501, 7):
    pwm1.duty(b)
    time.sleep_ms(2)
  for b in range(500, 0, -3):
    pwm1.duty(b)
    time.sleep_ms(2)


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

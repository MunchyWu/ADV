import os, sys, io
import M5
from M5 import *
from hardware import *
import time


pin1 = None
rgb = None


def setup():
  global pin1, rgb

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  rgb = RGB()


def loop():
  global pin1, rgb
  M5.update()
  if BtnA.wasClicked():
    pin1.value(1)
    time.sleep(1)
    pin1.value(0)
    time.sleep(0.2)
    pin1.value(1)
    time.sleep(1)
    pin1.value(0)
    time.sleep(0.2)
    pin1.value(1)
    time.sleep(1)
    pin1.value(0)
    time.sleep(0.2)
    pin1.value(1)
    time.sleep(0.3)
    pin1.value(0)
    time.sleep(0.1)
    pin1.value(1)
    time.sleep(0.3)
    pin1.value(0)
    time.sleep(0.1)
    pin1.value(1)
    time.sleep(0.3)
    pin1.value(0)
    time.sleep(0.1)
    pin1.value(1)
    time.sleep(1)
    pin1.value(0)
    time.sleep(0.2)
    pin1.value(1)
    time.sleep(1)
    pin1.value(0)
    time.sleep(0.2)
    pin1.value(1)
    time.sleep(1)
    pin1.value(0)
    time.sleep(0.2)
  else:
    pass


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
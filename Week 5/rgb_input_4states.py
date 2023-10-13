# change RGB LED colors with digital input and time using state logic
# 4 states are implemented as shown:
# 'ON'  -> turns on RGB green
# 'UNWIND'   -> Pulsate Red
# 'WINDED' -> Pulsate in Yellow
# 'READY' -> fade in RGB Green 2 seconds after 'WINDED' state

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb = None
state = 'ON'
state_timer = 0

def setup():
  global rgb, input_pin
  M5.begin()
  
  # custom RGB setting using pin G35 (M5 AtomS3 built-in LED):
  rgb = RGB(io=35, n=1, type="SK6812")
  #io=PinNumber n=1一个灯珠 
  # custom RGB setting using pin G2 (M5 AtomS3 bottom connector) and 10 LEDs:
  #rgb = RGB(io=2, n=10, type="SK6812")
  
  # initialize pin G41 (M5 AtomS3 built-in button) as input:
  #input_pin = Pin(41)
  
  # initialize pin G39 (M5 PortABC Extension red connector) as input:
  input_pin = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)
  #pull= pin.pull_up 黑线负极 白线是检测pin39
  
  # turn on RGB green and wait 2 seconds:
  if (state == 'ON'):
    print('on with RGB green..')
    rgb.fill_color(get_color(0, 255, 0))
    time.sleep(2)  
    check_input()

def loop():
  global state, state_timer
  M5.update()
      
  if (state == 'UNWIND'):
    #for i in range(1, 100000, 1):
      #print('pulsate Red i time')
    print('pulsate Red')
    # fade in RGB Red:
    for i in range(1, 180, 4):
      rgb.fill_color(get_color(i, 0, 0))
      time.sleep_ms(14)
    # fade out RGB Red:
    for i in range(180, 0, -8):
      rgb.fill_color(get_color(i, 0, 0))
      time.sleep_ms(14)
    check_input()
    
  elif (state == 'WINDED'):
    # if less than = 3 seconds passed since change to 'WINDED':
    if(time.ticks_ms() < state_timer + 3000):
      print('Pulsate in yellow..')
      for i in range(1, 180, 4):
        rgb.fill_color(get_color(i, i, 0))
        time.sleep_ms(20)
      for i in range(180, 0, -8):
          rgb.fill_color(get_color(i, i, 0))
          time.sleep_ms(20)
      
        
    
    # if more than 3 seconds passed since change to 'WINDED':
    elif(time.ticks_ms() > state_timer + 3000):
      state = 'READY'
      print('change to', state)
      # save current time in milliseconds:
      state_timer = time.ticks_ms()
      #statetimer是计时器，timetick是时钟。让他们相等 计时器就可以归零
  elif (state == 'READY'):
      print('Ready to shoot, change from yellow to green')
      rgb.fill_color(get_color(i, 255, 0))
          time.sleep_ms(1000)
      state_timer = time.tick_ms()
      if (input_pin.value() == 0):
          if(state != 'UNWIND'):
              print('change to UNWIND')
              state = 'UNWIND'
          
    
'''
  elif (state == 'READY'):
      if (input_pin.value() == 0):
        state_timer = time.ticks_ms()
        if(state != 'UNWIND'):
            print('change to UNWIND')
        state = 'UNWIND'
      elif:
          state_timer = time.ticks_ms()
          print('fade from yellow to green..')
          for i in range(180, 0, -1):
              rgb.fill_color(get_color(i, 255, 0))
        #time.sleep_ms(1000)
'''
    
        
      
    # if 2 seconds passed since change to 'FINISH':
'''
    if(time.ticks_ms() > state_timer + 2000):
      print('fade from red to black..') 
      for i in range(100):
        rgb.fill_color(get_color(100-i, 0, 0))
        time.sleep_ms(20)
      time.sleep(1)
      check_input()
'''

# check input pin and change state to 'UNWIND' or 'WINDED'
def check_input():
    global state, state_timer
    if (input_pin.value() == 0):
        if(state != 'WINDED'):
            print('chaneg to WINDED')
        state = 'WINDED'
        state_timer = time.ticks_ms()
    else:
        if(state != 'UNWIND'):
            print('change to UNWIND')
        state = 'UNWIND'
'''
  global state, state_timer
  if (input_pin.value() == 0):
    if(state != 'WINDED'):
      print('change to WINDED')
    state = 'WINDED'
    # save current time in milliseconds:
    state_timer = time.ticks_ms()
  else:
    if(state != 'UNWIND'):
      print('change to UNWIND')
    state = 'UNWIND'
'''

    
    
# convert separate r, g, b values to one rgb_color value:  
def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

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


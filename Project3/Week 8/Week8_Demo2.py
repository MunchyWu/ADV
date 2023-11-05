import network
import os, sys, io
import urequests as urq
import M5
from M5 import *
from hardware import *


wlan = network.WLAN(network.STA_IF)
if wlan.isconnected(): print('wlan is connected')


while (True):
    M5.update()
    if BtnA.wasPressed():
        print('Button Pressed')
        req = urq.request(
            method = 'POST',
            url = 'https://maker.ifttt.com/trigger/button_press/json/with/key/K3p-F8g_VX72ZOYscyC4a',
            json = { "Test" : 'Date' },
            headers = {'Content-Type' : 'application/json'}
            )
        print('Gotit')
            
            
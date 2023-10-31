import js as p5
from js import document, Math
import time

data = None
currentColor = [Math.random() * 255, Math.random() * 255, Math.random() * 255]  # initial random color
buttonPressed = False
img = p5.loadImage('SQ618.jpg')
button_val = None
button_state = 'UP'

sound = p5.loadSound('polaroid-taking-picture.wav')

def setup():
  p5.createCanvas(600, 600)
  #print('hello!')



def draw():
    global data, currentColor, buttonPressed, img, sound, button_state, button_val
    p5.background(255)
    p5.image(img, 0, 0, 600, 600)

    data_string = document.getElementById("data").innerText
    data_list = data_string.split(',')
    light_data = data_list[0]  # Now using the light sensor data
    angle_data = data_list[1]
    button_val = int(data_list[2])
    
  
    # If the button is pressed, change the current color to a new random color
    # if button_val == 1 and not buttonPressed:
    #     currentColor = [Math.random() * 255, Math.random() * 255, Math.random() * 255]
    #     buttonPressed = True
    # elif button_val == 0:
    #     buttonPressed = False
      
    inverted_light_data = 255 - int(light_data)  # invert the light sensor value
    alpha = p5.map(inverted_light_data, 0, 255, 0, 255)  # map the inverted data to a valid alpha range
    #p5.fill(currentColor[0], currentColor[1], currentColor[2], alpha)  # set the fill color with the current alpha

    # change to HSB color mode:
    p5.colorMode(p5.HSB)
    p5.fill(angle_data, 255, inverted_light_data)
    p5.rect(330, 38, 255, 80, 40)  # draw the rectangle
    p5.colorMode(p5.RGB)
    # change back to RGB color mode:
  
    if(button_val == 1) and (button_state == 'UP'):
      sound.play()
      button_state = 'DOWN'
      #print('flash!')
    elif(button_val == 0):
      button_state = 'UP'
        
    if(button_val == 0):
      # do 300 milliseconds of every 1000 milliseconds..
      if(p5.millis() % 7000 < 150):



        #this is been draw for 11 times
        #Outglow of the flash
        for i in range(10):
          p5.noStroke()
          p5.colorMode(p5.HSB, 255, 255, 255, 255)
          p5.fill(angle_data, 100, inverted_light_data, i/70)
          p5.rect(282 + i*4, 0 + i*4, 350 - i*8, 156 - i*8, 40+i*2)
          p5.colorMode(p5.RGB)

        # the current flash color
        p5.colorMode(p5.HSB)
        p5.fill(angle_data, 255, inverted_light_data)
        p5.rect(330, 38, 255, 80, 40)  # draw the rectangle
        p5.colorMode(p5.RGB)
        
        # inner light for the flash
        for i in range(12):
          p5.colorMode(p5.RGB)
          p5.fill(255, i*10)  # (gray, transparency)
          p5.noStroke()
          p5.rect(330 + i*4, 38 + i*4, 255 - i*8, 80 - i*8, 40-i*2)
          p5.colorMode(p5.RGB)

      if(p5.millis() % 7000 < 80):
        p5.fill(20)
        p5.noStroke()
        p5.circle(330, 357, 90)

        p5.fill(0,30)
        p5.noStroke()
        p5.circle(85, 247, 57)

        p5.fill(200)
        p5.rect(41, 80, 43, 43, 8)

        #whole screen light
        p5.colorMode(p5.HSB, 255, 255, 255, 255)
        p5.fill(angle_data, 20, 255, inverted_light_data)
        p5.rect(0, 0, 600, 600)  # draw the rectangle
        p5.colorMode(p5.RGB)






          
          
    
    
    

'''
# Define a new method for drawing a rectangle with rounded corners
def rounded_rect(x, y, w, h, r):
    p5.push()  # save the current drawing style settings and transformations
    p5.translate(x, y)  # move the origin to the rectangle's top-left corner
    p5.beginShape()  # create a custom shape
    p5.vertex(r, 0)  # top-left vertex, adjusted for the corner radius
    p5.vertex(w - r, 0)  # top-right vertex, adjusted for the corner radius
    p5.quadraticVertex(w, 0, w, r)  # top-right corner
    p5.vertex(w, h - r)  # bottom-right vertex, adjusted for the corner radius
    p5.quadraticVertex(w, h, w - r, h)  # bottom-right corner
    p5.vertex(r, h)  # bottom-left vertex, adjusted for the corner radius
    p5.quadraticVertex(0, h, 0, h - r)  # bottom-left corner
    p5.vertex(0, r)  # top-left vertex, adjusted for the corner radius
    p5.quadraticVertex(0, 0, r, 0)  # top-left corner
    p5.endShape(p5.CLOSE)  # close the custom shape
    p5.pop()  # restore the drawing style settings and transformations
'''
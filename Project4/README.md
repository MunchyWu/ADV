# 360 Photo booth
<img src="IMG_6811.jpg" alt="Parts" width="450"/>  <img src="IMG_6802.JPG" alt="Parts" width="450"/>

## 1. Ideations

<img src="WechatIMG626.png" alt="Ideation1" width="450"/> <img src="WechatIMG627.png" alt="Ideation2" width="450"/>



## 2. Connections
<img src="Connection.jpg" alt="Connections" width="900"/>

## 3. 3D Modeling
<img src="3D_modeling.jpg" alt="3D Modeling" width="900"/>

<img src="3D1.gif" alt="3D Modeling" width="300"/>  <img src="3D2.gif" alt="3D Modeling" width="300"/>  <img src="3D3.gif" alt="3D Modeling" width="300"/>

## 4. How does it work


- Place an object on the tower
* The light sensor on the tower will receive a lower light value
+ Lower light value will till the board to move the servos
- This loop will repeat 10 times
  > - Servo_Move will move 36 degrees
  > - Servo_Move stops
  > - Wait 1 second
  > - Servo_Shutter will push the Shutter button to take a photo
  > - Servo_Shutter back to rest position
  > - Wait 7 seconds

<img src="Moving1.gif" alt="Moving1" width="400"/> <img src="Moving2.gif" alt="Moving2" width="400"/>
  


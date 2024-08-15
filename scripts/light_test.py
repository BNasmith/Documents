from sense_hat import SenseHat
from random import randint
from time import sleep
sense=SenseHat()
sense.clear()
R=255,0,0
O=255,100,0
Y=255,255,0
G=0,255,0
C=0,255,255
B=0,0,255
P=255,0,255
W=255,255,255

colors=[R,O,Y,G,C,B,P,W]
for y in range(0,8):
     for x in range(0,8):
          sense.set_pixel(x,y,colors[y])
          sleep(0.1)

sense.clear()
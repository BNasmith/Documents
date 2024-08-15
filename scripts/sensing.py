from sense_hat import SenseHat
from math import floor
sense = SenseHat()

red=255,0,0
blue=0,0,255
myfile=open('test.txt','a')

temp=floor(sense.get_temperature())
hum=floor(sense.get_humidity())
press=floor(sense.get_pressure())

sense.show_message(str(temp),0.1,red)
sense.show_message(str(hum),0.1,blue)
sense.show_message(str(press))

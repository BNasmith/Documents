from sense_hat import SenseHat
from time import sleep
sense=SenseHat()
myfile=open('test.txt','a')
while True:
    myfile=open('test.txt','a')
    temp=sense.get_temperature()
    myfile.write(str(temp))
    myfile.write('\n')
    myfile.close()
    sleep(1)
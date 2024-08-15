import matplotlib.pyplot as plt
from sense_hat import *
from time import sleep
sense=SenseHat()

data=[]
for i in range(0,100):
    data.append(sense.get_temperature())
    sleep(0.1)
print(data)
plt.plot(data)
plt.xlabel('time')
plt.ylabel('temperature in C')
plt.show()

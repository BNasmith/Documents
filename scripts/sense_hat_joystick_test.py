#imports

from sense_hat import SenseHat
from time import sleep

#varabals
sense=SenseHat()
player_x=3
player_y=3

#lists

#def

def move_up(event):
    global player_y
    if event.action=='pressed' and player_y>0:
        player_y-=1

def move_down(event):
    global player_y
    if event.action=='pressed' and player_y<7:
        player_y+=1

def move_left(event):
    global player_x
    if event.action=='pressed' and player_x>0:
        player_x-=1

def move_right(event):
    global player_x
    if event.action=='pressed' and player_x<7:
        player_x+=1


#game
sense.stick.direction_up=move_up
sense.stick.direction_down=move_down
sense.stick.direction_left=move_left
sense.stick.direction_right=move_right
while True:
    sense.clear()
    sense.set_pixel(player_x,player_y,0,0,255)
    sleep(0.25)

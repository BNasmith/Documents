from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white=(255,255,255)
bat_y=4
ball_position = [3, 3]
ball_velocity = [1, 1]
score=0
# Functions

def draw_bat():
    sense.set_pixel(0,bat_y,white)
    sense.set_pixel(0,bat_y+1,white)
    sense.set_pixel(0,bat_y-1,white)
def move_up(event):
    global bat_y
    if event.action=='pressed' and bat_y>1:
        bat_y-=1
def move_down(event):
    global bat_y
    if event.action=='pressed' and bat_y<6:
        bat_y+=1


def draw_ball():
    sense.set_pixel(ball_position[0],ball_position[1],0,0,255)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]

    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]

    if ball_position[0] == 1 and (ball_position[1]==bat_y or ball_position[1]==bat_y+1 or ball_position[1]==bat_y-1):
        ball_velocity[0] = -ball_velocity[0]
        global score
        score=score+1

    
    if ball_position[0]==0:
        sense.show_message('Your score is '+str(score))
        sense
        ball_position[0]=3
        ball_position[1]=3
        score=0

                    
#Main
sense.stick.direction_up = move_up
sense.stick.direction_down=move_down
while True:
    sense.clear(0, 0, 0)
    draw_bat()
    draw_ball()
    sleep(0.25)

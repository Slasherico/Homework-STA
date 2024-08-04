#import the pygamezero(pgzero) game library
import pgzrun
#imports specific function from library form random it imports randint
from random import randint

#Standard title for game window
TITLE='Watch out!!!'

#Setting width and height window parameters
w = 500
h = 500
WIDTH = w 
HEIGHT = h

#Used to create character
npc= Actor('pink_invader_image')
#Used to set character postion - .pos
npc.pos= 250,250

msg = ''
cnt = 0

#Default function that is called to update the screen
def draw():
    #clears the screen
    screen.clear()
    #Screen Color       R   G   B
    screen.fill(color=(204,225,225))
    #Draws Character
    npc.draw()
    #Message          var    location      fontsize
    screen.draw.text(msg,center=(250,25),fontsize=30)

def placenpc():
    npc.x=randint(100,w-20)
    npc.y=randint(100,h-20)

def on_mouse_down(pos):
    #Allows variable to be changes outside from a seperate place
    global msg, cnt
    if npc.collidepoint(pos):
        cnt += 1
        msg = 'Good Shot :) - Counter: ' + str(cnt)
        placenpc()
    else:
        msg = 'You missed :( - Counter: ' + str(cnt)
   
#starts/runs the code
pgzrun.go()
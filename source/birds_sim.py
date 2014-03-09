# Artificial Intelligence Homework
# Project: Birds V formation simulation
# 
# By: Ryan Gilera
# Date: 16/02/14
#


#import simpleguitk as simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

#Global Variables
HEIGHT = 600
WIDTH = 900
DISTANCE_BET_BIRDS = 20
SPEED_LIMIT = 20
RADIUS = 120 

v_key = 12
balls = [] #A list that will hold the balls clas members
formation_circle = False
formation_v = True
max_birds = 0



###########################################################    
class Ball:
    def __init__(self, ball_pos, radius, ball_velocity, tag, speed_limiter, in_formation):
        self.radius = radius
        self.ball_pos = ball_pos
        self.ball_vel = ball_velocity
        self.tag = tag
        self.speed_limiter = speed_limiter
        self.in_formation = in_formation
        self.new_pos = [0,0]
        self.fixed_tag = False
    
    def update_new_pos(self,x,y):
        self.new_pos[0] = x
        self.new_pos[1] = y
    
    def set_ball(self,canvas):
        #update ball
        self.ball_pos[0]+=self.ball_vel[0]
        self.ball_pos[1]+=self.ball_vel[1]        
        
        if self.ball_vel[0] < 0:
            canvas.draw_image(imageL, (134/2,127/2), (134,127), self.ball_pos, (134/2,127/2))
        else:
            canvas.draw_image(imageR, (134/2,127/2), (134,127), self.ball_pos, (134/2,127/2))
     
    def bounce(self):
        if self.ball_pos[0] > WIDTH-self.radius:
            self.ball_vel[0]= -self.ball_vel[0]
        
        if self.ball_pos[1] > HEIGHT-self.radius:
            self.ball_vel[1]= -self.ball_vel[1]
        
        if self.ball_pos[0] < self.radius:
            self.ball_vel[0]= -self.ball_vel[0]
        
        if self.ball_pos[1] < self.radius:
            self.ball_vel[1]= -self.ball_vel[1]


def button_cplus():
    global RADIUS
    RADIUS += 5
    

def button_cminus():
    global RADIUS
    RADIUS -= 5
  

def button_vplus():
    global v_key
    v_key += 1
    

def button_vminus():
    global v_key
    v_key -= 1


#randomizer for ball spawn intial position    
def spawnPOS():
    ball_vel = [0,0]
    
    while ball_vel[0] < 2 and ball_vel[0] > -2:
        ball_vel[0] += random.randrange(-5,5)
    
    while ball_vel[1] < 2 and ball_vel[1] > -2:
        ball_vel[1] += random.randrange(-5,5)
    
    return ball_vel


#Magic starts here :) Spawn new bird in each click
def mouseclick(pos):
    global balls, max_birds
    posList = [pos[0],pos[1]] 
    
    if max_birds < 9:
        balls.append(Ball(posList, 10, spawnPOS(), False, SPEED_LIMIT, False))
        max_birds += 1


#button handler function for circle formation
def button_handler_c():
    global formation_circle, formation_v
    
    if formation_circle == False:
        formation_circle = True    
        formation_v = False
        
        for h, ball in enumerate(balls):
            balls[h].tag = False
            balls[h].speed_limiter = SPEED_LIMIT
            
            if balls[h].ball_vel[0] == 0:
                balls[h].ball_vel[0] += random.randrange(2,5) 
                balls[h].ball_vel[1] += random.randrange(2,5)


#button handler function for V formation                
def button_handler_v():
    global formation_circle, formation_v
    
    if formation_v == False:
        formation_circle = False   
        formation_v = True
        
        for o, ball in enumerate(balls):
            balls[o].tag = False
            balls[o].speed_limiter = SPEED_LIMIT
            
            if balls[o].ball_vel[0] == 0:
                balls[o].ball_vel[0] += random.randrange(2,5) 
                balls[o].ball_vel[1] += random.randrange(2,5) 
                

#drawing handler function. Automatically runs itself 60 times per second (to produce animation like movement)
def draw_handler(canvas):
    #draw background image
    canvas.draw_image(bg, (900 / 2, 600 / 2), (900, 600), (900/2, 600/2), (900, 600))
    
    #draw Title
    canvas.draw_text("F", (81,36),28,"Navy","sans-serif")
    canvas.draw_text("LAPPYBIRD", (98,30),18,"Navy","sans-serif")
    canvas.draw_text("S", (182,36),28,"Navy","sans-serif")

    #draw sub title
    canvas.draw_text("Flight Formation Simulation", (21,50),16,"Red","monospace")
    canvas.draw_text("Flight Formation Simulation", (21,50),16,"Red","monospace")
    canvas.draw_text("Flight Formation Simulation", (21,50),16,"Black","monospace")
    
    canvas.draw_text("By: Ryan Gilera", (91,80),12,"Black","monospace")
    
    #draw birds
    for i, ball in enumerate(balls):
        balls[i].set_ball(canvas)
        balls[i].bounce()
        
    alignBall()
    
    
#the main part of the program. It updates birds positions and velocity
def alignBall():
    key = 0
    
    for j, bola in enumerate(balls):
        if j > 0:
            distance = math.sqrt(
                                 math.pow((balls[j].ball_pos[0] - balls[0].ball_pos[0]),2) +
                                 math.pow((balls[j].ball_pos[1] - balls[0].ball_pos[1]),2))

            
            #updates birds positions for formation V
            if formation_v ==  True and formation_circle == False:
                if ((j % 2) == 1):
                    key += v_key
                    birdLeft(key)
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                else:
                    birdRight(key)
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                
            #updates birds positions for formation V
            if formation_circle == True and formation_v ==  False:
                if j == 1:
                    updateCTopPos()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 2:
                    updateCBottomPos()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 3:
                    updateCLeftPos()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 4:
                    updateCRightPos()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 5:
                    updateCTopRight()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 6:
                    updateCTopLeft()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 7:
                    updateCBottomRight()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])
                if j == 8:
                    updateCBottomLeft()
                    balls[j].update_new_pos(new_pos[0], new_pos[1])    
                    
            new_pos_distance = math.sqrt(math.pow((balls[j].ball_pos[0] - new_pos[0]),2) +
              math.pow((balls[j].ball_pos[1] - new_pos[1]),2))                                                   

            #If birds are in position, maintain velocity so that it will be fix on that new position
            if balls[j].tag == True:
                balls[j].in_formation = True
                balls[j].ball_vel[0] = (balls[j].new_pos[0] - balls[j].ball_pos[0]) 
                balls[j].ball_vel[1] = (balls[j].new_pos[1] - balls[j].ball_pos[1])         
                
            else:        
                #Else sets the birds into accelaration mode
                if (distance <= (math.hypot(ref_vel[0],ref_vel[1]) + 50)):
                    balls[j].fixed_tag = True
                
            #Accelerates the birds so that they can move to the new_pos
            #This is always true if the birds are still far from the new_pos
            if balls[j].fixed_tag == True or ((balls[j].in_formation == True) and balls[j].tag == False):
                if new_pos_distance > 0:
                    balls[j].ball_vel[0] = (balls[j].new_pos[0] - balls[j].ball_pos[0])/balls[j].speed_limiter 
                    balls[j].ball_vel[1] = (balls[j].new_pos[1] - balls[j].ball_pos[1])/balls[j].speed_limiter
    
                    #This updates and increases the acceleration if necessary to reach new_pos
                    if (math.hypot(balls[j].ball_vel[0],balls[j].ball_vel[1]) <= math.hypot(balls[0].ball_vel[0],balls[0].ball_vel[1]) and	
                        balls[j].speed_limiter > 1):
                        balls[j].speed_limiter -= 1
                    else:
                        #if all seems in seems in position, tag it to True
                        balls[j].tag = True   
                else: 
                    #if all seems in seems in position, tag it to True
                    balls[j].tag = True
                    balls[j].fixed_tag = False   
                
                
def birdLeft(multiplier):
    global ref_vel, pre_pos, new_pos, formation_pos, v_mid_length
    ref_vel = [balls[0].ball_vel[0] * multiplier, balls[0].ball_vel[1] * multiplier]
    pre_pos = [balls[0].ball_pos[0] - ref_vel[0], balls[0].ball_pos[1] - ref_vel[1]]
    new_pos = [pre_pos[0] + ref_vel[1], pre_pos[1] - ref_vel[0]]
    

def birdRight(multiplier):
    global ref_vel, pre_pos, new_pos, v_mid_length
    ref_vel = [balls[0].ball_vel[0] * multiplier, balls[0].ball_vel[1] * multiplier]
    pre_pos = [balls[0].ball_pos[0] - ref_vel[0], balls[0].ball_pos[1] - ref_vel[1]]
    new_pos = [pre_pos[0] - ref_vel[1], pre_pos[1] + ref_vel[0]]


def updateCTopPos():
    global new_pos
    new_pos = [balls[0].ball_pos[0], balls[0].ball_pos[1] - RADIUS ]   
    

def updateCBottomPos():
    global new_pos
    new_pos = [balls[0].ball_pos[0], balls[0].ball_pos[1] + RADIUS ]    
   

def updateCLeftPos():
    global new_pos
    new_pos = [balls[0].ball_pos[0] - RADIUS, balls[0].ball_pos[1]]


def updateCRightPos():
    global new_pos
    new_pos = [balls[0].ball_pos[0] + RADIUS, balls[0].ball_pos[1]]


def updateCTopRight():
    global new_pos
    x = (balls[0].ball_pos[0] + (RADIUS * (math.cos(math.radians(45)))))
    y = (balls[0].ball_pos[1] - (RADIUS * (math.sin(math.radians(45)))))
    new_pos = [x,y]    


def updateCTopLeft():
    global new_pos
    x = (balls[0].ball_pos[0] - (RADIUS * (math.cos(math.radians(45)))))
    y = (balls[0].ball_pos[1] - (RADIUS * (math.sin(math.radians(45)))))
    new_pos = [x,y]     
    

def updateCBottomRight():
    global new_pos
    x = (balls[0].ball_pos[0] + (RADIUS * (math.cos(math.radians(45)))))
    y = (balls[0].ball_pos[1] + (RADIUS * (math.sin(math.radians(45)))))
    new_pos = [x,y]    
    
    
def updateCBottomLeft():
    global new_pos
    x = (balls[0].ball_pos[0] - (RADIUS * (math.cos(math.radians(45)))))
    y = (balls[0].ball_pos[1] + (RADIUS * (math.sin(math.radians(45)))))
    new_pos = [x,y]


    

    
frame=simplegui.create_frame("Birds Formation Simulation",WIDTH,HEIGHT)

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw_handler)

labelA = frame.add_label('Formation Control')
button1 = frame.add_button('Circle Formation', button_handler_c)
label1 = frame.add_label(' ')
button2 = frame.add_button('V Formation', button_handler_v)
label2 = frame.add_label(' ')
label3 = frame.add_label(' ')
label4 = frame.add_label(' ')
labelA = frame.add_label('Circle Diameter Control')
buttonA = frame.add_button('+', button_cplus, 25)
label5 = frame.add_label(' ')
buttonB = frame.add_button('-', button_cminus, 25)

label6 = frame.add_label(' ')
label7 = frame.add_label(' ')
labelB = frame.add_label('V Distance Control')
buttonC = frame.add_button('+', button_vplus, 25)
label8 = frame.add_label(' ')
buttonD = frame.add_button('-', button_vminus, 25)

#images
imageR = simplegui.load_image('file:///X:/GIT_ROOT/cluster-bird-formation-sim/images/right_bird.gif')
imageL = simplegui.load_image('file:///X:/GIT_ROOT/cluster-bird-formation-sim/images/left_bird.gif') 
bg = simplegui.load_image('file:///X:/GIT_ROOT/cluster-bird-formation-sim/images/bg.png')


frame.start()

import pygame
import random
import math
from pygame import mixer
#mixer for audio sounds
pygame.init()    #initialization of pygame to use 

#creation of screen and size initialization
screen = pygame.display.set_mode((600,600))

#background
background=pygame.image.load("ocean1.jpg")

mixer.music.load("bgmusic2.mp3")
mixer.music.play(-1)

#title and icon
pygame.display.set_caption("Dogesh war") 

icon = pygame.image.load("OIP.jpeg") #icon pic
pygame.display.set_icon(icon)   #displaying icon implementation



player=pygame.image.load("enemy.png")
player2=pygame.transform.scale(player,(65,65))
xposition=200
yposition=470

change_in_x=0
change_in_y=0

#enemy multiple can be created by appending each enemy multiple time in a list then pass the list
enemy=[]
player3=[]
x_enemy=[]
y_enemy=[]
y_enemy=[]
changex_enemy=[]
changey_enemy=[]
num_enemy=5 #it can be changed later

for i in range(num_enemy):
    
    enemy.append(pygame.image.load("dog.png"))
    player3.append(pygame.transform.scale(enemy[i ],(70,70)))
    x_enemy.append(random.randint(0,519))
    y_enemy.append(random.randint(0,100))
    changex_enemy.append(0.2)
    changey_enemy.append(30)



#bullet
bullet=pygame.image.load("bullet.png")
bullet2=pygame.transform.scale(bullet,(35,35))
xbullet=0
ybullet=480
change_bullet_x=0
change_bullet_y=1
bullet_state="ready"

#font for scoreboard
scoreboard=pygame.font.Font(None,35)

#game over
game_over=pygame.font.Font(None,50)



def win_blit(implem,x,y):
    screen.blit(implem,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    win_blit(bullet2,x+16,y+10)

score=0

def iscollide(x_enemy,y_enemy,xbullet,ybullet):
    sum_square= math.pow(abs(x_enemy-xbullet),2)+math.pow(abs(y_enemy-ybullet),2)
    distance= math.sqrt(sum_square)
    if distance<30:
        return True
    return False

# or we can use a bool condition to return true or false here

#pygame screen will run over the time until exit button is pressed 
run=True
while run:
    screen.fill((255,255,255)) #RGB values for background
    # implementing blit for bg so that it appears as long as the game is being played
    win_blit(background,0,0)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
        if event.type==pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key==pygame.K_LEFT:
                print("Turn left")
                change_in_x=-0.2
            if event.key==pygame.K_RIGHT:
                print("Turn right")
                change_in_x=0.2
            if event.key==pygame.K_SPACE:

                bulletsound=mixer.Sound("weap.mp3")
                bulletsound.play()
                xbullet=xposition

                print("Fire")
                fire_bullet(xbullet,ybullet)

                #for up and down not currently included
            # if event.key==pygame.K_UP:
            #     change_in_y-=0.1
            # if event.key==pygame.K_DOWN:
            #     change_in_y+=0.1 
        if event.type==pygame.KEYUP:
            print("Key released")
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                change_in_x=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                change_in_y=0

       

    xposition=xposition+change_in_x
    # we can add change in y as well as per need
    def position(a):
        if a<=0:
           a=0
        elif a>=520:
           a=520
        return a
    xposition=position(xposition)
    # if xposition<=0:
    #     xposition=0
    # elif xposition>=520:
    #     xposition=520
    
    for i in range(num_enemy):
        # game over contition
        if y_enemy[i]>150:
            for a in range(num_enemy):
                y_enemy[a]=1000
            gameover_text=game_over.render("GAME OVER !!! " + "Score :"+str(score),True,(255,255,255))
            win_blit(gameover_text,130,250)
            break
        x_enemy[i]+=changex_enemy[i]
         #enemy in boundary
        if x_enemy[i]<=0:
            changex_enemy[i]=0.12
            y_enemy[i]+=changey_enemy[i]
        

        elif x_enemy[i]>=530:
            changex_enemy[i]=-0.12
            y_enemy[i]+=changey_enemy[i]
       #bullet going and not disappearing

        #collision
        collision = iscollide(x_enemy[i],y_enemy[i],xbullet,ybullet)
        if collision:
            #sound effect addition
            hit_target=mixer.Sound("hit.mp3")
            hit_target.play()
            print("Hit the target")
            ybullet=470
            bullet_state="ready"
            score+=5
            print(score)
            x_enemy[i]=random.randint(0,519)
            y_enemy[i]=random.randint(0,100)
        win_blit(player3[i],x_enemy[i],y_enemy[i])
    
    if ybullet<=10:
        ybullet=480
        bullet_state="ready"
    
    

    #multiple bullets logic( will be altered as per the need)
    if bullet_state == "fire":
        fire_bullet(xposition,ybullet) 
        ybullet-=change_bullet_y


    
    # convert the score into displayable form
    score_text=scoreboard.render("Score: "+ str(score),True,(255,0,0))
    win_blit(score_text,10,10)
    # passing player,enemy and their position in winblit function to draw images and implement DRY
    win_blit(player2,xposition,yposition)
    
    pygame.display.update()

    
   




import pygame
import random

pygame.init()    #initialization of pygame to use 

#creation of screen and size initialization
screen = pygame.display.set_mode((600,600))

#background
background=pygame.image.load("ocean.jpg")

#title and icon
pygame.display.set_caption("Dogesh war") 

icon = pygame.image.load("R.png") #icon pic
pygame.display.set_icon(icon)   #displaying icon implementation



player=pygame.image.load("OIP.jpeg")
player2=pygame.transform.scale(player,(80,80))
xposition=200
yposition=470

change_in_x=0
change_in_y=0

#enemy

enemy=pygame.image.load("enemy.png")
player3=pygame.transform.scale(enemy,(70,70))
x_enemy=random.randint(0,600)
y_enemy=random.randint(0,100)

changex_enemy=0.25
changey_enemy=30


def win_blit(implem,x,y):
    screen.blit(implem,(x,y))
  

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

                #for up and down not currently included
            # if event.key==pygame.K_UP:
            #     change_in_y-=0.1
            # if event.key==pygame.K_DOWN:
            #     change_in_y+=0.1
        if event.type==pygame.KEYUP:
            print("Key released might be whatever")
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
    
    x_enemy+=changex_enemy
   
    #enemy in boundary
    if x_enemy<=0:
        changex_enemy=0.25
        y_enemy+=changey_enemy

    elif x_enemy>=530:
        changex_enemy=-0.25
        y_enemy+=changey_enemy
    


    
    # passing player,enemy and their position in winblit function to draw images and implement DRY
    win_blit(player2,xposition,yposition)
    win_blit(player3,x_enemy,y_enemy)
    pygame.display.update()

    
   




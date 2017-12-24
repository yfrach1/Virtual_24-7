import pygame
import random

pygame.init()
#----open game console 11
display_width = 900
display_height = 700
gameDisplay = pygame.display.set_mode((display_width,display_height))
player1_width = 30
player1_height = 30
Finish_x_left = 0.116
Finish_x_right = 0.18
Finish_y_left = 0.10
Finish_y_right = 0.166
#--------colors--------
black = (0,0,0)
white = (255,255,255)
grey = (100,100,100)
red = (200,0,0)
green = (0,200,0)
reuven = (0,200,100)
bright_reuven = (0,255,155)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_grey = (155,155,155)
#---------------------
#----Title
pygame.display.set_caption('Team no. 24 - Virtual_24/7')
#----clock for holding
clock = pygame.time.Clock()

boardImg = pygame.image.load("Board.jpg")
Player1 = pygame.image.load("1.jpg")
Player2 = pygame.image.load("2.jpg")
Game1 = pygame.image.load("Game1.jpg")
Game2 = pygame.image.load("Game2.jpg")
CubeImg1 = pygame.image.load("cube1.jpg")
CubeImg2 = pygame.image.load("cube2.jpg")
CubeImg3 = pygame.image.load("cube3.jpg")
CubeImg4 = pygame.image.load("cube4.jpg")
CubeImg5 = pygame.image.load("cube5.jpg")
CubeImg6 = pygame.image.load("cube6.jpg")
ExplainImg = pygame.image.load("explain1.jpg")
CardImg = pygame.image.load("card.jpg")
quest1 = pygame.image.load("quest1.jpg")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects(msg,smallText)
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        textRect.center = ( (x+(w/2)) , (y+(h/2)))
        if click[0] == 1 and action != None:
            if action == "game1":
                game1()
            elif action == "explain1":
                explain1()
            elif action == "game2":
                game2()
            elif action == "intro":
                game_intro()
            elif action == "card":
                card()
            elif action == "quit":
                pygame.quit()
                quit()
                
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        textRect.center = ( (x+(w/2)) , (y+(h/2)) )
 
    textRect.center = ( (x+(w/2)) , (y+(h/2)) )
    gameDisplay.blit(textSurf,textRect)

    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        midText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects("Welcome to Main Menu", largeText)
        TextSurf2, TextRect2 = text_objects("Choose a Game", midText)
        TextRect.center = ((display_width/2.1),(display_height/7))
        TextRect2.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("Ladders and Snakes",100,300,300,200,green,bright_green,"explain1")
        gameDisplay.blit(Game1,(100,250))
        button("Four In Row",500,300,300,200,red,bright_red,"game2")
        gameDisplay.blit(Game2,(500,250))
        button("QUIT",400,600,100,50,grey,bright_grey,"quit")
        
      
        pygame.display.update()
        clock.tick(100)
        
def Board(x,y):
    gameDisplay.blit(boardImg,(x,y))
def Player1_(x,y):
    gameDisplay.blit(Player1,(x,y))
def Player2_(x,y):
    gameDisplay.blit(Player2,(x,y))
def explainImg(x,y):
    gameDisplay.blit(ExplainImg,(x,y))
def Cube(msg):
    x = display_width * 0.80
    y = display_width * 0.22
    if msg == 1:
        gameDisplay.blit(CubeImg1,(x,y))
    elif msg == 2:
        gameDisplay.blit(CubeImg2,(x,y))
    elif msg == 3:
        gameDisplay.blit(CubeImg3,(x,y))
    elif msg == 4:
        gameDisplay.blit(CubeImg4,(x,y))
    elif msg == 5:
        gameDisplay.blit(CubeImg5,(x,y))
    elif msg == 6:
        gameDisplay.blit(CubeImg6,(x,y))

def card():
    cardExit = False

    while not cardExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              cardExit = True
        gameDisplay.fill(white)
        gameDisplay.blit(quest1,(200,100))
        button("1",700,550,100,100,reuven,bright_reuven)
        button("2",500,550,100,100,reuven,bright_reuven)
        button("3",300,550,100,100,reuven,bright_reuven)
        button("4",100,550,100,100,reuven,bright_reuven)
        pygame.display.update()
        clock.tick(100)
    
def explain1():
    expExit = False

    while not expExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              expExit = True
        explainImg(5,20)
        button("START GAME!",600,600,150,50,green,bright_green,"game1")
        button("<- BACK",100,600,150,50,red,bright_red,"intro")
        pygame.display.update()
        clock.tick(100)
def game1():
    #----position Imgs-----0.06  0.78
    Board_x= (display_width * 0.10)
    Board_y= (display_height * 0.10)
    Player1_x= (display_width * 0.08)
    Player1_y= (display_height * 0.78)
    Player2_x= (display_width * 0.06)
    Player2_y= (display_height * 0.75)
    Cube_Number = random.randrange(1,7,1)
    #------------------------
    #----first position without moveing-----
    Player1_x_change = 0
    Player1_y_change = 0
    Player2_x_change = 0
    Player2_y_change = 0
    #------------------------
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              gameExit = True
            
     #------Player 1 movement------             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player1_x_change = -1
                elif event.key == pygame.K_RIGHT:
                    Player1_x_change = 1
                elif event.key == pygame.K_UP:
                    Player1_y_change = -1
                elif event.key == pygame.K_DOWN:
                    Player1_y_change = 1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    Player1_x_change =0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    Player1_y_change =0
     #------------------------------
     #------Player 2 movement------- 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Player2_x_change = -1
                elif event.key == pygame.K_d:
                    Player2_x_change = 1
                elif event.key == pygame.K_w:
                    Player2_y_change = -1
                elif event.key == pygame.K_s:
                    Player2_y_change = 1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    Player2_x_change =0
                elif event.key == pygame.K_s or event.key == pygame.K_w:
                    Player2_y_change =0
    #------Cube Show Random-------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Cube_Number = random.randrange(1,7,1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if Cube_Number == 1:
                        pygame.mixer.music.load('1.mp3')
                        pygame.mixer.music.play()    
                    elif Cube_Number == 2:
                        pygame.mixer.music.load('2.mp3')
                        pygame.mixer.music.play()    
                    elif Cube_Number == 3:
                        pygame.mixer.music.load('3.mp3')
                        pygame.mixer.music.play()    
                    elif Cube_Number == 4:
                        pygame.mixer.music.load('4.mp3')
                        pygame.mixer.music.play()    
                    elif Cube_Number == 5:
                        pygame.mixer.music.load('5.mp3')
                        pygame.mixer.music.play()    
                    elif Cube_Number == 6:
                        pygame.mixer.music.load('6.mp3')
                        pygame.mixer.music.play()
                    Cube(Cube_Number)
            #if Player1_x 
     #------------------------------
                
        Player1_x += Player1_x_change
        Player1_y += Player1_y_change
        Player2_x += Player2_x_change
        Player2_y += Player2_y_change
        gameDisplay.fill(white)
        Board(Board_x,Board_y)
        Player1_(Player1_x,Player1_y)
        Player2_(Player2_x,Player2_y)
        Cube(Cube_Number)
        if Player1_x > display_width - player1_width or Player1_x < 0 + player1_width:
            Player1_x = (display_width * 0.13)
            Player1_y = (display_height * 0.83)
        button("QUIT GAME",10,10,150,50,red,bright_red,"intro")
        button("",720,500,100,150,red,bright_red,"card")
        gameDisplay.blit(CardImg,(650,450))
        pygame.display.update()
        clock.tick(100)
    
game_intro()
pygame.quit()
quit()

#do versions of your game so they actually EXECUTE 
#KAREN HUANG - 2019 - CS SUMMATIVE

from pygame import*
import os 
import random 
#moving screen to top left corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 20)
init()


size = width, height = 1000, 700
#just to be clear vv (notes to myself)
width = 1000
height = 700  #variables are used so it's easier to use with the whole program

screen = display.set_mode(size)

#COLOURS #RGB
BLACK = (0,0,0)
BLUE = (76,112,186)
OTHERBLUE = (34,155,155)
WHITE = (255,255,255)
GRAY = (222,226,232)
OTHERGRAY = (94,94,94)
RED = (209, 71, 82)
OTHERRED = (214,62,59)
ANOTHERRED = (252, 121, 121)
ORANGE = (255, 154, 71)
PURPLE = (215, 186, 239)
YELLOW = (255,234,99)

#FONTS 
mainTitle = font.SysFont("Impact",100)
subTitle = font.SysFont("Impact",45)
bodyText = font.SysFont("Agency FB",27)

#photos 
leftArrow = image.load("leftArrowKaren.png")
rightArrow = image.load("rightArrowKaren.png")
downArrow = image.load("downArrowKaren.png")


#music
#bgMusic = mixer.Sound("bgMusicKaren.wav") #music for the game 

#constant global variables 
myClock = time.Clock() 
backTimer = time.get_ticks() #timer to change the background colour 
backColour = BLUE #the backColour starts off as BLUE, then afterwards, we're able to modify that if needed
scoreCount = 0 #for the points / score
cellSpeed = 2 #speed of the cellphone
playTimer = 0 #the time the game has been running for 

#STATES 
STATEMENU = 1 
STATEGAME = 2
STATEINSTRUCTIONS = 3
STATEGAMEOVER = 4
STATEQUIT = 5


#GAME STATES --> Reference to Appendix 3 Example 3 
KEY_RIGHT = False
KEY_LEFT = False
KEY_DOWN = False 

#these x and y values are for the starting cellphone block  
cellX = 280
cellY = height - 640

def drawFact(): #function to draw a fun fact box
    draw.rect(screen,WHITE,(40,260,200,300))
    
    factString = "Sad Facts!" #fun fact, except they aren't fun, they're sad :(
    factText = subTitle.render(factString,1,BLACK)
    screen.blit(factText, Rect(48,263,100,100))

def drawGame(): #function to draw the game background base 
    screen.fill(backColour)
    draw.rect(screen,BLACK,(width - 980, height - 680, width - 40, height - 40))
    
    draw.rect(screen,GRAY,(260, height - 660, 480, height - 80))
    draw.rect(screen,BLACK,(280, height - 640, 440, height - 120))
    
    
    #score keeping
    scoreString = "Current" 
    scoreText = subTitle.render(scoreString,1,WHITE)
    screen.blit(scoreText, Rect(50,50,400,400))
    
    scoreStringPt2 = "Score:"
    scoreTextPt2 = subTitle.render(scoreStringPt2,1,WHITE)
    screen.blit(scoreTextPt2, Rect(50,100,400,400))
    
    countString = str(scoreCount)
    countText = subTitle.render(countString,1,WHITE)
    screen.blit(countText, Rect(50,150,400,400))
    
    #A title on the side of the screen
    E = "E"
    EText = mainTitle.render(E,1,ANOTHERRED)
    screen.blit(EText, Rect(840,20,100,100)) #first e
    screen.blit(EText, Rect(840,550,100,100)) #last e
    
    dash = "-"
    dashText = mainTitle.render(dash,1,ORANGE)
    screen.blit(dashText, Rect(846,90,100,100))
    
    W = "W"
    WText = mainTitle.render(W,1,YELLOW)
    screen.blit(WText, Rect(820,170,100,100))
    
    A = "A"
    AText = mainTitle.render(A,1,OTHERBLUE)
    screen.blit(AText, Rect(835,265,100,100))
    
    S = "S"
    SText = mainTitle.render(S,1,BLUE)
    screen.blit(SText, Rect(836,360,100,100))
    
    T = "T"
    TText = mainTitle.render(T,1,PURPLE)
    screen.blit(TText, Rect(838,455,100,100))
    

    
    #fun fact box 
    if 0 <= scoreCount <= 1000:
        drawFact() #put in diff facts for diff number of points
        
        factLine1 = "While Americans are"
        factLine1Text = bodyText.render(factLine1,1,BLACK)
        screen.blit(factLine1Text, Rect(48,320,100,100))
        
        factLine2 = "getting new phones"
        factLine2Text = bodyText.render(factLine2,1,BLACK)
        screen.blit(factLine2Text, Rect(48,350,100,100))        
        
        factLine3 = "every 12 to 18 months,"
        factLine3Text = bodyText.render(factLine3,1,BLACK)
        screen.blit(factLine3Text, Rect(48,380,100,100)) 
        
        factLine4 = "only 10% of old ones"
        factLine4Text = bodyText.render(factLine4,1,BLACK)
        screen.blit(factLine4Text, Rect(48,410,100,100))         
        
        factLine5 = "get recycled."
        factLine5Text = bodyText.render(factLine5,1,BLACK)
        screen.blit(factLine5Text, Rect(48,440,100,100)) 
        
    elif 1000 < scoreCount <= 2000:
        drawFact()
        
        fact2Line1 = "If cellphones aren't"
        fact2Line1Text = bodyText.render(fact2Line1,1,BLACK)
        screen.blit(fact2Line1Text, Rect(48,320,100,100))        
        
        fact2Line2 = "properly disposed,"
        fact2Line2Text = bodyText.render(fact2Line2,1,BLACK)
        screen.blit(fact2Line2Text, Rect(48,350,100,100))                
        
        fact2Line3 = "they release toxins,"
        fact2Line3Text = bodyText.render(fact2Line3,1,BLACK)
        screen.blit(fact2Line3Text, Rect(48,380,100,100))
        
        fact2Line4 = "such as mercury, into"
        fact2Line4Text = bodyText.render(fact2Line4,1,BLACK)
        screen.blit(fact2Line4Text, Rect(48,410,100,100)) 
        
        fact2Line5 = "the air and water. This"
        fact2Line5Text = bodyText.render(fact2Line5,1,BLACK)
        screen.blit(fact2Line5Text, Rect(48,440,100,100))  
        
        fact2Line6 = "really hurts the"
        fact2Line6Text = bodyText.render(fact2Line6,1,BLACK)
        screen.blit(fact2Line6Text, Rect(48,470,100,100))        
        
        fact2Line7 = "environment and"
        fact2Line7Text = bodyText.render(fact2Line7,1,BLACK)
        screen.blit(fact2Line7Text, Rect(48,500,100,100))         
        
        fact2Line8 = "the ecosystems."
        fact2Line8Text = bodyText.render(fact2Line8,1,BLACK)
        screen.blit(fact2Line8Text, Rect(48,530,100,100))    
        
    elif 2000 < scoreCount <= 3000:
        drawFact()
        
        fact3Line1 = "Not only are animals"
        fact3Line1Text = bodyText.render(fact3Line1,1,BLACK)
        screen.blit(fact3Line1Text, Rect(48,320,100,100))          
        
        fact3Line2 = "affected, but humans"
        fact3Line2Text = bodyText.render(fact3Line2,1,BLACK)
        screen.blit(fact3Line2Text, Rect(48,350,100,100))        
        
        fact3Line3 = "are too. The"
        fact3Line3Text = bodyText.render(fact3Line3,1,BLACK)
        screen.blit(fact3Line3Text, Rect(48,380,100,100))
                
        
        fact3Line4 = "efficiency and growth"
        fact3Line4Text = bodyText.render(fact3Line4,1,BLACK)
        screen.blit(fact3Line4Text, Rect(48,410,100,100))         
        
        fact3Line5 = "of our body decreases,"
        fact3Line5Text = bodyText.render(fact3Line5,1,BLACK)
        screen.blit(fact3Line5Text, Rect(48,440,100,100))          
        
        fact3Line6 = "which can be very"
        fact3Line6Text = bodyText.render(fact3Line6,1,BLACK)
        screen.blit(fact3Line6Text, Rect(48,470,100,100))         
        
        fact3Line7 = "dangereous -- "
        fact3Line7Text = bodyText.render(fact3Line7,1,BLACK)
        screen.blit(fact3Line7Text, Rect(48,500,100,100))         
                
        fact3Line8 = "especially for babies." 
        fact3Line8Text = bodyText.render(fact3Line8,1,BLACK)
        screen.blit(fact3Line8Text, Rect(48,530,100,100)) 
        
    elif 3000 < scoreCount <= 3100:
        drawFact()
        fact4Line1 = "The production of"
        fact4Line1Text = bodyText.render(fact4Line1,1,BLACK)
        screen.blit(fact4Line1Text, Rect(48,320,100,100))             
        
        fact4Line2 = "phones is very harmful." 
        fact4Line2Text = bodyText.render(fact4Line2,1,BLACK)
        screen.blit(fact4Line2Text, Rect(48,350,100,100))           
        
        fact4Line3 = "They need many"
        fact4Line3Text = bodyText.render(fact4Line3,1,BLACK)
        screen.blit(fact4Line3Text, Rect(48,380,100,100))        
        
        fact4Line4 = "precious metals,"
        fact4Line4Text = bodyText.render(fact4Line4,1,BLACK)
        screen.blit(fact4Line4Text, Rect(48,410,100,100))                 
        
        fact4Line5 = "and they also create"
        fact4Line5Text = bodyText.render(fact4Line5,1,BLACK)
        screen.blit(fact4Line5Text, Rect(48,440,100,100))          
                
        fact4Line6 = "a lot of CO2. Altogether"
        fact4Line6Text = bodyText.render(fact4Line6,1,BLACK)
        screen.blit(fact4Line6Text, Rect(48,470,100,100))          
        
        fact4Line7 ="They add a lot to our"
        fact4Line7Text = bodyText.render(fact4Line7,1,BLACK)
        screen.blit(fact4Line7Text, Rect(48,500,100,100))          
        
        fact4Line8 = "carbon footprint."
        fact4Line8Text = bodyText.render(fact4Line8,1,BLACK)
        screen.blit(fact4Line8Text, Rect(48,530,100,100))     
    else: #just anything above 4000
        drawFact()
        fact5Line1 = "When you use your"
        fact5Line1Text = bodyText.render(fact5Line1,1,BLACK)
        screen.blit(fact5Line1Text, Rect(48,320,100,100))        
    
        fact5Line2 = "phones, info gets"
        fact5Line2Text = bodyText.render(fact5Line2,1,BLACK)
        screen.blit(fact5Line2Text, Rect(48,350,100,100))         
        
        fact5Line3 = "sent to data centers"
        fact5Line3Text = bodyText.render(fact5Line3,1,BLACK)
        screen.blit(fact5Line3Text, Rect(48,380,100,100))        
        
        fact5Line4 = "which require a lot"
        fact5Line4Text = bodyText.render(fact5Line4,1,BLACK)
        screen.blit(fact5Line4Text, Rect(48,410,100,100))          
        
        fact5Line5 = "of energy to operate."
        fact5Line5Text = bodyText.render(fact5Line5,1,BLACK)
        screen.blit(fact5Line5Text, Rect(48,440,100,100))         
        
        fact5Line6 = "Again, a lot of"
        fact5Line6Text = bodyText.render(fact5Line6,1,BLACK)
        screen.blit(fact5Line6Text, Rect(48,470,100,100))               
        
        fact5Line7 = "pollution is"
        fact5Line7Text = bodyText.render(fact5Line7,1,BLACK)
        screen.blit(fact5Line7Text, Rect(48,500,100,100))          
        
        fact5Line8 = "produced."
        fact5Line8Text = bodyText.render(fact5Line8,1,BLACK)
        screen.blit(fact5Line8Text, Rect(48,530,100,100)) 
        
        
        
#this function right below vv is to make sure that new blocks fall /on top of/ old blocks (so they stack)        
def lowestY(x,List): #this was made with the help of Mr. Van Rooyen #this is to make the blocks not go in a spot that's already 'filled' by a preexsiting block
    lowest = 640
    for spot in List: #"List" will be the list with the lists of x and y coordinates of the cellphone 
        if spot[0] == x: #checking if the x value in the list is equal to the x of the new cellphone
            if spot[1] < lowest: #checking if the y value in the list is less than 640
                lowest = spot[1] #if its lower than 640, then the lowest becomes that y value from the list 
                
    return lowest - 60 



def drawScene(screen, curState): #designs for all the diff screens 
    if curState == STATEMENU: #MAIN MENU

        screen.fill(backColour)
        draw.rect(screen,BLACK,(width - 980, height - 680, width - 40, height - 40))
        
        #title 
        draw.rect(screen,WHITE,(width - 900, height - 625, width - 200, height - 550))
        titleString = "E - W A S T E"
        titleText = mainTitle.render(titleString, 1, BLACK)
        screen.blit(titleText, Rect(width - 720, height - 612, width - 200, height - 550))
        
        #game button  
        draw.rect(screen,WHITE,(width - 940, height - 375, width/4, height/4)) #play game button    
        gameString = "Play"
        gameText = subTitle.render(gameString,1,BLACK)
        screen.blit(gameText, Rect(width - 852, height - 324, width/4, height/4))
        
        #instructions button 
        draw.rect(screen,WHITE,(width - 940 + width/4 + 60, height - 375, width/4, height/4)) #instructions button
        instructionsString = "Instructions"
        instructionsText = subTitle.render(instructionsString, 1, BLACK)
        screen.blit(instructionsText, Rect(width - 929 + width/4 + 60, height - 324, width/4, height/4))
        
        #quit button 
        draw.rect(screen,WHITE,(width - 940 + 2*(width/4) + 120, height - 375, width/4, height/4)) #quit button
        quitString = "Quit" 
        quitText = subTitle.render(quitString, 1, BLACK)
        screen.blit(quitText, Rect(width - 855 + 2*(width/4) + 120, height - 324, width/4, height/4))
        
        
    if curState == STATEGAME:
        drawGame() #using the function to draw the game bg 
        
    if curState == STATEINSTRUCTIONS:
        #still using the border from before vv 
        screen.fill(backColour)
        draw.rect(screen,BLACK,(width - 980, height - 680, width - 40, height - 40))    
        
        instrTitleString = "I N S T R U C T I O N S"
        instrTitleText = mainTitle.render(instrTitleString, 1, WHITE)
        screen.blit(instrTitleText, Rect(165,30,100,100))   
        
        #back / exit button
        draw.rect(screen,RED,(55,55,75,75))
        draw.line(screen,WHITE,(65,65),(120,120), 5)
        draw.line(screen,WHITE,(120,65),(65,120), 5)
        
        introY = 180 #the y value of the intro text 
        
        #the actual intructions (+ an intro)
        introString = 'Thank you for opening "E-Waste", a game based on Tetris raising awareness to minimize'
        introText = bodyText.render(introString,1,WHITE)
        screen.blit(introText, Rect(165,150,100,100))
        
        introString2 = 'e-waste. GLHF!'
        introText2 = bodyText.render(introString2,1,WHITE)
        screen.blit(introText2, Rect(165,introY,100,100))

        
        howTitle = "How to play: " + ("- "*20)
        howText = bodyText.render(howTitle,1,WHITE)
        screen.blit(howText, Rect(165,introY+40,100,100))
        
        leftString = "Click this to move your block over one unit to the left."
        leftText = bodyText.render(leftString,1,WHITE)
        screen.blit(leftText, Rect(165,introY+20+50,100,100))        
        
        rightString = "Click this to move your block over one unit to the right."
        rightText = bodyText.render(rightString,1,WHITE)
        screen.blit(rightText, Rect(165,introY+10+100,100,100))         
        
        downString = "Your block will automatically be moving down, but if you wish to go faster,"
        downText = bodyText.render(downString,1,WHITE)
        screen.blit(downText, Rect(165,introY+10+150,100,100))      
        
        downString2 = "click this button to move your block one unit down."
        downText2 = bodyText.render(downString2,1,WHITE)
        screen.blit(downText2, Rect(165,introY+40+150,100,100))           
        
        #photos of arrow keys 
        screen.blit(leftArrow, Rect(600,230,100,100)) #left arrow
        screen.blit(rightArrow, Rect(620,290,100,100)) #right arrow
        screen.blit(downArrow, Rect(770,345,100,100))  #down arrow
        
        #how to lose 
        loseTitle = "How to lose: " + ("- "*20)
        loseText = bodyText.render(loseTitle,1,WHITE)
        screen.blit(loseText, Rect(165,introY+40+200,100,100))   
        
        line1 = "Whenever you complete a row, it will be cleared and the rest of the blocks will move down. "
        line1Text = bodyText.render(line1,1,WHITE)
        screen.blit(line1Text, Rect(165,introY+70+200,100,100))        
   
        line2 = "If you can't fully complete a row, it will not be able to be cleared. If you can't complete"
        line2Text = bodyText.render(line2,1,WHITE)
        screen.blit(line2Text, Rect(165,introY+100+200,100,100))                
        
        line3 = "your rows, the blocks will build up. If a single block hits the top, you lose!"
        line3Text = bodyText.render(line3,1,WHITE)
        screen.blit(line3Text, Rect(165,introY+130+200,100,100))    
        
        line4 = "However, you don't want this to happen! The goal is to clear as many rows as possible, meaning"
        line4Text = bodyText.render(line4,1,WHITE)
        screen.blit(line4Text, Rect(165,introY+160+200,100,100))  
        
        line5 = "you're deleting as much e-waste as you can. Just like in real, life, you want the least"
        line5Text = bodyText.render(line5,1,WHITE)
        screen.blit(line5Text, Rect(165,introY+190+200,100,100))
        
        line6 = "amount of e-waste as possible. So, try your best to clear a lot of rows!"
        line6Text = bodyText.render(line6,1,WHITE)
        screen.blit(line6Text, Rect(165,introY+220+200,100,100))
        
    if curState == STATEGAMEOVER: #game over screen
        screen.fill(BLACK)
        gameOverTitle = "G A M E  O V E R"
        gameOverText = mainTitle.render(gameOverTitle,1,RED)
        screen.blit(gameOverText, Rect(220,200,100,100))
        
        
        draw.rect(screen,WHITE,(321,372,350,70))
        scoreString = "FINAL SCORE: %i" %scoreCount #displaying the final score on the game over screen
        scoreText = subTitle.render(scoreString,1,BLACK) 
        screen.blit(scoreText, Rect(330,380,100,100))
        
        
        draw.rect(screen,WHITE,(418,492,145,70))        
        quitString = "- Quit -"
        quitText = subTitle.render(quitString,1,BLACK)
        screen.blit(quitText, Rect(427,500,100,100))
        
     
     
#a list of all the devices that have hit the bottom (this list is here so that it can be used with the function right below)        
permDevices = [] #a list of lists (each list will have an x and y for devices when they hit the border
                  
def drawCellphone(xValue, yValue): #function to draw a new cellphone
    drawGame() 
    
    draw.rect(screen, WHITE, (xValue, yValue, 40,60))
    draw.rect(screen, OTHERGRAY, (xValue + 5, yValue + 5, 30,45))
    draw.circle(screen, OTHERGRAY, (xValue +20, yValue +55), 3)    
    
    for coordinates in permDevices:
        draw.rect(screen, WHITE, (coordinates[0],coordinates[1], 40,60))
        draw.rect(screen, OTHERGRAY, (coordinates[0] + 5, coordinates[1] + 5, 30,45))
        draw.circle(screen, OTHERGRAY, (coordinates[0] +20, coordinates[1] +55), 3)  
                
    
    display.flip()
    
   
def changeState(but, mousex, mousey, curState): #to change the diff screens 
    if but == 1:
        
        if curState == STATEMENU: #at the main menu
            if 680 <= mousex <= 930: #change these values so they actually work 
                if height-660 <= mousey <= height-375 + height/4:
                    curState = STATEQUIT #quits the program
                    
            if 60 <= mousex <= 310:
                if height-660 <= mousey <= height-375 + height/4:
                    curState = STATEGAME #enters the game 
                    
            if width - 940 + width/4 + 60 <= mousex <= width - 940 + width/4 +310:
                curState = STATEINSTRUCTIONS
                
        if curState == STATEINSTRUCTIONS: 
            if 55 <= mousex <= 130:
                if 55 <= mousey <= 130:
                    curState = STATEMENU                

        if curState == STATEGAMEOVER:                                   
            if 418 <= mousex <= 562:
                if 492 <= mousey <= 562:
                    curState = STATEQUIT #quit the game from the gameover screen 
                    
        
    return curState

state = STATEMENU #first just sets the state as STATEMENU


#lists for the different blocks in the game #originally i was going to have many types of blocks, but I ended up only have the cellphone, so this list only has one thing
devices = [drawCellphone(cellX,cellY)]

scoreCount = 0 #first having an empty score 

while state != STATEQUIT:
    
    #bgMusic.play()

    mx = my = 0
    button = 0
    
    for Event in event.get():             # this is so that the X at the top can be clicked to quit
        if Event.type == QUIT:
            state = STATEQUIT
        if Event.type == MOUSEBUTTONDOWN: # if the mouse is clicked, this assigns values to mx and my and button 
            mx, my = Event.pos          
            button = Event.button
        
    
    if state == STATEMENU: #remember, it's checking /every time/ if the state is STATEMENU
        #vv this is for animating the background 
        
        #border for the screen 
        #makes an animation for the screen border to change colour 
        
        if time.get_ticks() - backTimer > 400:
            if backColour == BLUE:
                backColour = OTHERBLUE
            elif backColour == OTHERBLUE:
                backColour = PURPLE
            elif backColour == PURPLE:
                backColour = OTHERRED 
            elif backColour == OTHERRED:
                backColour = ORANGE
            else: 
                backColour = BLUE
            
                
            backTimer = time.get_ticks() #makes a new 400 time, resets the time so it follows the number from the if time.get_ticks() above ^^
            #time.wait(__) <-- DONT USE WAIT, THAT'LL JUST LAG THE PROGRAM, USE .GET_TICKS 
                        
    
    if state == STATEINSTRUCTIONS:
        #vv this is for animating the background  ^ same thing as before 
        if time.get_ticks() - backTimer > 600:
            if backColour == BLUE:
                backColour = OTHERBLUE
            elif backColour == OTHERBLUE:
                backColour = PURPLE
            elif backColour == PURPLE:
                backColour = OTHERRED 
            elif backColour == OTHERRED:
                backColour = ORANGE
            else: 
                backColour = BLUE
                
            backTimer = time.get_ticks() #makes a new 600 time, resets the time so it follows the number from the if time.get_ticks() above ^^

    while state == STATEGAME: 
        #this is so that the animation works in state game too (it can't be put in the if right above^^ because whenever it's still in STATEGAME, it doesn't leave this while loop to go to the if above
        if time.get_ticks() - backTimer > 500:
            if backColour == BLUE:
                backColour = OTHERBLUE
            elif backColour == OTHERBLUE:
                backColour = PURPLE
            elif backColour == PURPLE:
                backColour = OTHERRED 
            elif backColour == OTHERRED:
                backColour = ORANGE
            else: 
                backColour = BLUE
    
            backTimer = time.get_ticks() #makes a new 500 time, resets the time so it follows the number from the if time.get_ticks() above ^^
            

         
        #clearing a row  
        pairCount = 0 #pairCount must be reset each time to count properly 
        for pair in permDevices:
            if pair[1] == 580: 
                pairCount += 1    
        
            if pairCount == 11:
                #this for loop was made with the help of Mr. Van Rooyen
                for i in range(len(permDevices) -1, -1, -1): #going through the list backwards so the indices don't get messed up
                    if permDevices[i][1] == 580: #to find the first element in the i 
                        del(permDevices[i]) #deleting the list if these ^ conditions are met 
                        
                    else:
                        permDevices[i][1] += 60 #to move down                   
                    
                ##This code was what I used before (that was attempting to clear a row). It only cleared half of the row, and that's because we didn't go backwards when grabbing the elements.    
                #for pair in permDevices:
                    #if pair[1] == 580:
                        #permDevices.remove(pair)
                        #print(pair)
                    #else:
                        #pair[1] += 60 #to move down
                    #print(permDevices)
        
                    
                scoreCount += 100 #adding 100 points when the row is cleared 
            
            if pair[1] == 100 : #the 'top' of the game #if a single block reaches this place, game over
                state = STATEGAMEOVER
                               
                               
        #this is calling the method lowestY to check if a new block is going to stack on an old block or not        
        lowestt = lowestY(cellX,permDevices) #called lowestt because there's already a variable called lowest
        
        if cellY >= lowestt - 20: #if the new block reaches a small part of the space above an old block, it will automatically do the following: vv 
            
            devices[0] #this takes the 0th index in the devices list (which is a cellphone) 
            permDevices.append([cellX,lowestt]) #adding x and y values to the list that has all the x and y values of each cellphone block
                     
            cellX = random.randrange(280,440,40)      #resetting the x y values for the next cellphone #making it random
            cellY = height - 640
            
            scoreCount += 25 #adding 25 whenever the block stops moving (when it hits the bottom / the top of another block)
            
        drawCellphone(cellX,cellY) #uses drawCellphone with the x and y assigned at the top ^^ (the starting values of x and y)
        
        
        
        myClock.tick(100) #the initial speed of the block
        if time.get_ticks() - playTimer > 15000: #after 15 seconds pass... vv 
            cellSpeed += 1 #making the cellSpeed add one each time 15 seconds pass 
            playTimer = time.get_ticks() #resetting the timer
        
        cellY += cellSpeed #makes it so that the block always goes down as long as state is stategame  #'cellY' is the y value for the starting block
        
        for evnt in event.get():
            if evnt.type == QUIT:
                state = STATEQUIT #x button on the top works 
            if evnt.type == MOUSEBUTTONDOWN: # if the mouse is clicked, this assigns values to mx and my and button 
                mx, my = evnt.pos          
                button = evnt.button
        
        
        
      #This is what I had orignally for boundaries 
      
            #if evnt.type == KEYDOWN: #when a key is pressed (this is for the actual game)
                
                #if evnt.key == K_LEFT:
                    #if cellX > 280:     
                        #cellX -= 40 #if the key is pressed, but not held (this was modified from being held to make it move in blocks of units (like in the actual Tetris game))
            
                #if evnt.key == K_RIGHT:
                    #if cellX < 680:
                        #cellX += 40
                        
                        
                        
         #This is what Mr. Van Rooyen coded to help my situation of blocks jumping onto columns when the left or right side is blocked      
         
            if evnt.type == KEYDOWN: #when a key is pressed (this is for the actual game)
    
                if evnt.key == K_LEFT:
                    if cellX > 280:   
                        # VR added a check here
                        if lowestY(cellX-40, permDevices) > cellY:
                            cellX -= 40 #if the key is pressed, but not held (this was modified from being held to make it move in blocks of units (like in the actual Tetris game))
        
                if evnt.key == K_RIGHT:
                    if cellX < 680:
                        # VR added a check here
                        if lowestY(cellX+40, permDevices) > cellY:
                            cellX += 40
                    
                if evnt.key == K_DOWN:
                    cellY += 40
            
                #if evnt.key == K_UP: #but we don't want allow the user to go back up 
                    #KEY_UP = True
                    
                
                #for coordinates in permDevices:
                    #if coordinates[0] + 40 == cellX:
                        #if coordinates[1] + 60 == cellY:
                            #KEYUP = True
                            #cellX = coordinates[0] + 40
                            
                    #if coordinates[0] - 40 == cellX:
                        #if coordinates[1] + 60 == cellY:
                            #KEYUP = True
                            #cellX = coordinates[0] - 40
                            
                    #if coordinates[1] - 60 == cellY:
                        #if coordinates[0] == cellX:
                            #KEYUP = True
                            #cellY = coordinates[1] - 60         
                                     
                
                       
        #boundaries for the bottom vv 
        if 580 < cellY <= 700:
            cellY = 580
            # vv so that the block doesn't move after it hits the bottom 
            KEY_LEFT = False
            KEY_RIGHT = False 
            KEY_DOWN = False
        

    drawScene(screen, state)
    display.flip()
    myClock.tick(60)    
    
    state = changeState(button, mx, my, state)
    


quit()
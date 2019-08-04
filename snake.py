import pygame
import os
from random import randint
import pickle
import time
import sys
sys.path.insert(0, 'lib')
from pygame_functions import *

def showScore():
    global showScoreGame
    hideLabel(showScoreGame)
    showScoreGame = makeLabel("Score: {}".format(score), 30, 400, 630,"red")
    showLabel(showScoreGame)
    updateDisplay()
    
def verify():
    try:
        open("highScore","rb")
    except:
        highScoreStart()

def highScoreStart():
    highScore = 0
    pickle_out = open("highScore","wb")
    pickle.dump(highScore, pickle_out)
    pickle_out.close()
    
def add(x,y):
    ordem.append(makeSprite("square.png"))
    body.append(ordem[len(body)])
    a = (move[-1][0]-x, move[-1][1]-y)
    move.append(a)

def leave():
    hideLabel(showScoreGame)
    pickle_in = open("highScore","rb")
    highScore = pickle.load(pickle_in)
    if highScore > score:
        pass
    else:
        pickle_out = open("highScore","wb")
        pickle.dump(score, pickle_out)
        pickle_out.close()
        highScore = score
    hideAll()
    over = makeLabel("GAME OVER", 60,150,160,"red")
    showScore = makeLabel("Score: {}".format(score),30, 240,320, "red")
    showHighScore = makeLabel("High Score: {}".format(highScore),30, 205,400, "red")
    showLabel(over)
    showLabel(showScore)
    showLabel(showHighScore)
    while True:
        if keyPressed("enter"):
            hideLabel(show_time)
            hideLabel(over)
            hideLabel(showScore)
            hideLabel(showHighScore)
            updateDisplay()
            start()
            break
        updateDisplay()
        
def options():
    global volume
    hideLabel(showScoreGame)
    hideAll()
    updateDisplay()
    musicLabel = makeLabel(" Press Up or Down to change the volume", 40,0,300,"red")
    musicConfirmLabel = makeLabel(" Press ENTER to confirm", 30, 150, 500, "red")
    showLabel(musicConfirmLabel)
    showLabel(musicLabel)
    while True:
        updateDisplay()
        if keyPressed("up"):
            if volume < 1:
                pygame.mixer.music.set_volume(volume + 0.1)
                for x in range(len(sounds)):
                    sounds[x].set_volume(volume + 0.1)
                volume += 0.1
                time.sleep(0.2)
        if keyPressed("down"):
            if volume > 0:
                pygame.mixer.music.set_volume(volume - 0.1)
                for x in range(len(sounds)):
                    sounds[x].set_volume(volume - 0.1)
                volume -= 0.1
                time.sleep(0.2)
        if keyPressed("enter"):
            time.sleep(0.2)
            break
    hideLabel(musicConfirmLabel)
    hideLabel(musicLabel)
    updateDisplay()
    
def see_time(x):
    x1 = x.split(" : ")
    total = ((int(x1[0])*3600 + int(x1[1])*60) + int(x1[2])) #Turn minutes into seconds
    return total

def return_time(x):
    copy = x
    if copy < 60:
        if x < 10:
            copy = "0"+str(copy)
        return "00 : 00 : {}".format(copy)
    elif copy < 3600:
        min_ = 0
        while copy > 0:
            copy -= 60
            min_ += 1
            save = copy
        save += 60
        min_ -= 1
        if min_ < 10:
            min_ = "0"+str(min_)
        if save < 10:
            save = "0"+str(save)
        return "00 : {} : {}".format(min_, save)
    elif copy == 60:
        return "00 : 01 : 00"
    elif copy == 3600:
        return "01 : 00 : 00"
    else:
        hr_ = 0
        while copy > 3600:
            copy -= 3600
            hr_ += 1
            save = copy
        min_ = 0
        while save > 0:
            save -= 60
            min_ += 1
            seg_ = save
        min_ -= 1
        save += 60
        if hr_ < 10:
            hr_ = "0"+str(hr_)
        if min_ < 10:
            min_ = "0"+str(min_)
        if save < 10:
            save = "0"+str(save)
        return "{} : {} : {}".format(hr_,min_, save)

def start():
    global show_time
    global total_time_lost
    global ordem
    global body
    global move
    global score
    first_move = True
    score = 0
    #body of the snake
    ordem = [None] * 3
    i = 0
    while i < 3:
        ordem[i] = makeSprite("square.png")
        i += 1
    body = [ordem[0],ordem[1]]
    #Intro
    while True:
        time.sleep(0.5)
        start = makeSprite("start.png")
        moveSprite(start, 50, 170)
        music = makeMusic("intro.mp3")
        showOptions = makeLabel("Options",50, 450,540, "red")
        playMusic()
        while True:
            showLabel(showOptions)
            if mousePressed() or keyPressed("p"):
                xPos, yPos = pygame.mouse.get_pos()
                if (xPos > 452 and yPos > 553) or keyPressed("p"):
                    hideLabel(showOptions)
                    options()
            if keyPressed("esc"):
                end()
            if keyPressed("enter"):
                break
            showSprite(start)
            updateDisplay()
        hideLabel(showOptions)
        #Countdown
        num = 1
        music = makeMusic("background.mp3")
        playSound(introSound)
        hideAll()
        updateDisplay()
        showNumber = makeLabel("3",300, 250,100, "red")
        showLabel(showNumber)
        updateDisplay()
        time.sleep(1)
        hideLabel(showNumber)
        updateDisplay()
        showNumber = makeLabel("2",300, 250,100, "red")
        showLabel(showNumber)
        updateDisplay()
        time.sleep(1)
        hideLabel(showNumber)
        updateDisplay()
        showNumber = makeLabel("1",300, 250,100, "red")
        showLabel(showNumber)
        updateDisplay()
        time.sleep(1)
        hideLabel(showNumber)
        updateDisplay()
        playMusic()
        pointX = randint(1,29)*20 #X.pos of the point
        pointY = randint(1,29)*20 #Y.pos of the point

        moveSprite(point, pointX, pointY)
        showSprite(point)
        moveSprite(body[0], 300,320)
        moveSprite(body[1], 280,320)
        move = [(300,320),(280,320)]

        pressed = ""
        for x in range(len(body)):
            showSprite(body[x])
        show_time = makeLabel("00 : 00 : 00",50,10,10,"red")
        showLabel(show_time)
        while True:
            showScore()
            if first_move == True:
                time_start = time.strftime("%H : %M : %S")
            time_end = time.strftime("%H : %M : %S")
            real_time = see_time(time_end) - see_time(time_start) - total_time_lost
            hideLabel(show_time)
            show_time = makeLabel(return_time(real_time),30,10,625,"red")
            showLabel(show_time)
            len_b = len(body)
            #Pause
            if keyPressed("p"):
                time_lost_1 = time.strftime("%H : %M : %S")
                options()
                if num/5 == int(num/5):
                    showSprite(big_point)
                    time_lost_2 = time.strftime("%H : %M : %S")
                    total_time_lost += see_time(time_lost_2) - see_time(time_lost_1)
                else:
                    time_lost_2 = time.strftime("%H : %M : %S")
                    if first_move == False:
                        total_time_lost += see_time(time_lost_2) - see_time(time_lost_1)
                    showSprite(point)
            #When music ends
            if see_time(time_end) - see_time(time_start) + total_time_lost == 281:
                stopMusic()
                rewindMusic()
                time_start = time.strftime("%H : %M : %S")
                playMusic()
                
            if pressed == "":
                pass
            
            #Down loop
            elif pressed == "s":
                for x in range(len(body)):
                    if x == 0:
                        move.append((move[x][0], move[x][1]+20))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            #Up loop
            elif pressed == "w":
                for x in range(len(body)):
                    if x == 0:
                        move.append((move[x][0], move[x][1]-20))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            #Right loop
            elif pressed == "d":
                for x in range(len(body)):
                    if x == 0:
                        move.append((move[x][0]+20, move[x][1]))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            #Left loop
            elif pressed == "a":
                for x in range(len(body)):
                    if x == 0:
                        move.append((move[x][0]-20, move[x][1]))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
                    
            #To the snake stay in the screen
            if move[0][0] < 0:
                for x in range(len(body)):
                    if x == 0:
                        move.append((580, move[x][1]))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            if move[0][0] > 580:
                for x in range(len(body)):
                    if x == 0:
                        move.append((0, move[x][1]))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            if move[0][1] > 580:
                for x in range(len(body)):
                    if x == 0:
                        move.append((move[x][0], 0))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            if move[0][1] < 0:
                for x in range(len(body)):
                    if x == 0:
                        move.append((move[x][0], 580))
                    else:
                        move.append((move[x-1][0], move[x-1][1]))
                for y in range(len_b):
                    move.remove(move[0])
            #Down
            elif (keyPressed("s") or keyPressed("down")) and pressed != "w":
                pressed = "s"
                first_move = False
            #Up
            elif (keyPressed("w") or keyPressed("up")) and pressed != "s":
                pressed = "w"
                first_move = False
            #Right
            elif (keyPressed("d") or keyPressed("right")) and pressed != "a":
                pressed = "d"
                first_move = False
            #Left
            elif (keyPressed("a") or keyPressed("left")) and pressed != "d":
                pressed = "a"
                first_move = False
                
            #Cath the point
            if (move[0][0] == pointX and move[0][1] == pointY) or (num/5 == int(num/5) and move[0][0] == pointX-20 and move[0][1] == pointY-20) or (num/5 == int(num/5) and move[0][0] == pointX+20 and move[0][1] == pointY+20):
                playSound(catchSound)
                if num/5 == int(num/5):
                    score += 20
                else:
                    score += 5
                num += 1
                if len(body) < 104: 
                    if pressed == "s":
                        add(0,20)
                    if pressed == "w":
                        add(0,(-20))
                    if pressed == "d":
                        add(20,0)
                    if pressed == "a":
                        add((-20),0)
                while True:
                    goon = True
                    pointX = randint(1,28)*20
                    pointY = randint(1,28)*20
                    for x in range(len(move)):
                        if pointX == move[x][0] and pointY == move[x][1]:
                            goon = False
                    if goon == True:
                        break
                if num/5 == int(num/5):
                    playSound(popSound)
                    hideSprite(point)
                    moveSprite(big_point, pointX, pointY)
                    showSprite(big_point)
                    crono = time.time()
                else:
                    for x in range(len(bar)):
                        hideSprite(bar[x])
                    hideSprite(big_point)
                    moveSprite(point, pointX, pointY)
                    showSprite(point)
                    
            #Time to the big point disappear
            if num/5 == int(num/5):
               crono_end = time.time()
               if round(crono_end-crono,1)- round(total_time_lost,1) >= 4:
                    hideSprite(bar[-1])
                    playSound(disappearSound)
                    num += 1
                    while True:
                        goon = True
                        pointX = randint(1,28)*20
                        pointY = randint(1,28)*20
                        for x in range(len(move)):
                            if pointX == move[x][0] and pointY == move[x][1]:
                                goon = False
                        if goon == True:
                            break
                    hideSprite(big_point)
                    moveSprite(point, pointX, pointY)
                    showSprite(point)
                    total_time_lost = 0
               elif round(crono_end-crono,1) - round(total_time_lost,1) >= 3.5:
                    hideSprite(bar[-2])
                    showSprite(bar[-1])
               elif round(crono_end-crono,1)- round(total_time_lost,1) >= 3:
                    hideSprite(bar[-3])
                    showSprite(bar[-2])
               elif round(crono_end-crono,1)- round(total_time_lost,1) >= 2.5:
                    hideSprite(bar[-4])
                    showSprite(bar[-3])
               elif round(crono_end-crono,1)- round(total_time_lost,1) >= 2:
                    hideSprite(bar[-5])
                    showSprite(bar[-4])
               elif round(crono_end-crono,1)- round(total_time_lost,1) >= 1.5:
                    hideSprite(bar[-6])
                    showSprite(bar[-5])
               elif round(crono_end-crono,1)- round(total_time_lost,1) >= 1:
                    hideSprite(bar[-7])
                    showSprite(bar[-6])
               elif round(crono_end-crono,1)- round(total_time_lost,1) >= 0.5:
                    hideSprite(bar[-8])
                    showSprite(bar[-7])
               else:
                    showSprite(bar[-8])

            #Show the snake (Update)
            for x in range(len_b):
                if move[0] == move[x] and x != 0: #Game over
                    time.sleep(1)
                    music = makeMusic("game_over.mp3")
                    playMusic()
                    leave()
                    continue
                moveSprite(body[x],move[x][0],move[x][1])
                showSprite(body[x])
            updateDisplay()
            tick(11)
    endWait()

#Screen settings
screen = screenSize(600,670)
setAutoUpdate(False)
setBackgroundColour("Black")
#Directory
os.chdir('lib')
#Sounds and Sprites
popSound = makeSound("pop.wav")
introSound = makeSound("introSound.wav")
catchSound = makeSound("cathSound.wav")
disappearSound = makeSound("disappearSound.wav")
big_point = makeSprite("red ball.png")
point = makeSprite("point.png")
sounds = [popSound, introSound, catchSound, disappearSound]
bar = [makeSprite("bar1.png"),makeSprite("bar2.png"),makeSprite("bar3.png"),makeSprite("bar4.png"),makeSprite("bar5.png"),makeSprite("bar6.png"),makeSprite("bar7.png"),makeSprite("bar8.png"),makeSprite("bar9.png")]
for x in range(len(bar)):
    moveSprite(bar[x], 200, 640)
score = 0
showScoreGame = makeLabel("Score: 0", 30, 400, 630,"red")
drawRect(0,620,600,1,"red")
total_time_lost = 0 #Time lost in the options
volume = 1 #Default volume
verify() #See if there is a HighScore
start() 

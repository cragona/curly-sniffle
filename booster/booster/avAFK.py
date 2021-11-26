import pyautogui

leftOrRight = ['left', 'right']

import random
import decimal
import time

#checks for deserter
def findImage(picture):
    holder = pyautogui.locateOnScreen(picture)
    stringHolder = str(holder) #place holder to hold holder as string
    if(stringHolder != "None"):   
        print('image found:', picture)
        return True  
    return False

def doQ(loopCount):
    for x in range(0,loopCount):
        pyautogui.keyDown('y')
        time.sleep(0.25)
        pyautogui.keyUp('y')
        time.sleep(0.25)

        pyautogui.keyDown('j')
        time.sleep(0.25)
        pyautogui.keyUp('j')
        time.sleep(0.25)
    return

def enterAvStart():
    ##enterand stealth
    pyautogui.hotkey('shift', 'x')

    ## straft left
    time.sleep(0.25)
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')

    ##wait for gate open
    time.sleep(3)
    return

def waitForGameStart():
    time.sleep(120)
    return

def runThroughGate():
    time.sleep(0.5)
    pyautogui.keyDown('w')
    time.sleep(30)
    pyautogui.keyUp('w')
    time.sleep(0.5)
    pyautogui.keyDown('w')
    for x in range(0, 19):
        pyautogui.keyDown('d')
        time.sleep(decimal.Decimal(random.randrange(50, 200))/100)
        pyautogui.keyUp('d')
        time.sleep(random.randrange(1,2))
    pyautogui.keyUp('w') 
    return

def moveAroundAV():

    while not findImage('leavebg.png'):
        pyautogui.keyDown('up')
        key = random.choice(leftOrRight)
        pyautogui.keyDown(key)
        time.sleep(decimal.Decimal(random.randrange(1, 100))/100)
        pyautogui.keyUp(key)
        time.sleep(5)
        pyautogui.keyUp('up')

    pyautogui.press('t', presses=5)
    time.sleep(20)
    print('starting new av')
    doQ(6)
  
    return

gamecount = 1

def main():
    global gamecount
    if findImage('qpop.png'):
        print('entering av:', gamecount)
        print('q pop')
        pyautogui.press('h', presses=5)
        time.sleep(30)
        enterAvStart()
        waitForGameStart()
        runThroughGate()
        moveAroundAV()
        gamecount = gamecount + 1     
    return

def runMain():
    global gamecount
    print('starting program')
    time.sleep(5)
    print('starting new av')
    doQ(6)

    while(1):
        main()
    return

runMain()


import pyautogui

countBooster = 0

import random
import time


#function to make a random interval
def setWaitTime(x):
    if x < 1:
        sleepTime = (random.random() * x )
    else:
        sleepTime = (random.random() * x )+ 1
    print('x passed= ', x, 'sleep time is = ', sleepTime)
    time.sleep(sleepTime)
    return


#add counter to booster
def counter():
    countBooster = counterBooster + 1;
    return

#randomize mouse width / height of found box
def rWidth(left, width):
    return random.randint(left-1, left+width) 

def rHeight(top, height): 
    return random.randint(top-1, top+height)

#helper func to move mouse and click shit
def moveSpot(rWidth, rHeight):
    pyautogui.moveTo(rWidth, rHeight, 1)
    return

def clickSpot():
    setWaitTime(1)
    pyautogui.click()
    return

#checks for deserter
def findRes():
    holder = pyautogui.locateOnScreen('res.png')

    stringHolder = str(holder) #place holder to hold holder as string

    #check place holder if none do some shit else pass coords
    if(stringHolder == "None"):
        print("no res found")
        
        return False
    else:
        print('res found')
        return True
    return False



def main():

    pyautogui.press('5')



    time.sleep(1)
        #move around
##        pyautogui.keyDown('a')
##        time.sleep(0.1)
##        pyautogui.keyUp('a')
##        time.sleep(0.1)
##        pyautogui.keyDown('d')
##        time.sleep(0.1)
##        pyautogui.keyUp('d')
##        time.sleep(0.1)
##        pyautogui.keyDown('a')
##        time.sleep(0.1)
##        pyautogui.keyUp('a')
##        time.sleep(0.1)
##        pyautogui.keyDown('d')
##        time.sleep(0.1)
##        pyautogui.keyUp('d')

    if findRes():
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.keyDown('w')
        time.sleep(0.3)
        pyautogui.keyUp('w')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('t')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.press('4')
        
    return

def runMain():
    time.sleep(5)
    print('starting...')
     
    while(1):
        main()
    return

runMain()


#little bloat bot made by chuck

import pyautogui
import time
pyautogui.FAILSAFE = True

def toggle():
    time.sleep(0.4)
    pyautogui.keyDown('alt')
    time.sleep(.1)
    pyautogui.keyDown('`')
    time.sleep(.25)
    pyautogui.keyUp('alt')
    time.sleep(.1)
    pyautogui.keyUp('`')
    time.sleep(0.4)
    
def move_me(direction, t, p):
    time.sleep(.5)
    print(p)
    pyautogui.keyDown(direction)
    time.sleep(t)
    pyautogui.keyUp(direction)

def mulgore():
    move_me('s', 27, 'back 27')
    wait_jump()
    move_me('q', 6, 'left 6')
    wait_jump()
    move_me('s', 8, 'back 8')
    wait_jump()
    move_me('q', 13.5, 'left 13.5')
    wait_jump()
    move_me('s', 10, 'back 10')
    wait_jump()
    move_me('q', 14, 'left 14')
    wait_jump()
    move_me('w', 3, 'forward 3')
    wait_jump()
    move_me('q', 3, 'left 3')
    wait_jump()
    move_me('w', 1, 'forward 1')
    wait_jump()
    move_me('q', 4, 'left 4')
    wait_jump()
    move_me('w', 2, 'forward 2')
    wait_jump()
    move_me('q', 9, 'left 9')
    wait_jump()
    move_me('w', 3, 'forward 3')
    wait_jump()
    move_me('q', 15, 'left 15')

def move_through_hole():
    time.sleep(.5)
    pyautogui.keyDown('up')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.keyUp('up')
    time.sleep(.5)

def move_up_hill():
    move_me('left', .4, 'jump up hill')
    time.sleep(.5)
    pyautogui.keyDown('up')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.keyUp('up')
    time.sleep(.5)

def type_something(item, speed):
    pyautogui.press('enter')
    pyautogui.write(item, interval=speed)
    pyautogui.press('enter')
    
def delete_hearthstone():
    type_something('/run for b=0,4 do for s=1,36 do n=GetContainerItemLink(b,s);if n and string.find(n,"Hearthstone") then PickupContainerItem(b,s);DeleteCursorItem();end;end;end;', .01)

def unstuck():
    type_something('/click HelpFrameCharacterStuckStuck', 0.01)

def res():
    type_something('/run RepopMe()',0.01)

def pvp():
    type_something('/pvp',0.01)


def razorhill1():
    focus1()
    delete_hearthstone()
    unstuck()
    
def razorhill2():
    focus2()
    delete_hearthstone()
    unstuck()
    
def razorhill3():
    focus3()
    delete_hearthstone()
    unstuck()
    
def razorhill4():
    focus4()
    delete_hearthstone()
    unstuck()

def razorhill5():
    focus5()
    delete_hearthstone()
    unstuck()

def razorhill6():
    focus6()
    delete_hearthstone()
    unstuck()

def after_log():
    toggle() #off
    razorhill1()
    razorhill2()
    razorhill3()
    razorhill4()
    razorhill5()
    razorhill6()
    time.sleep(12)

def take_res():
    move_me('up', .75, 'move towards res sickness')
    time.sleep(.25)
    type_something('/tar spirit',0.01)
    time.sleep(.25)
    pyautogui.press('t')
    time.sleep(.25)
    type_something('/script SelectGossipOption(1)',0.01)
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    time.sleep(1)

def dores1():
    focus1()
    res()
    time.sleep(1)
    
def dores2():
    focus2()
    res()
    time.sleep(1)

def dores3():
    focus3()
    res()
    time.sleep(1)

def dores4():
    focus4()
    res()
    time.sleep(1)

def dores5():
    focus5()
    res()
    time.sleep(1)

def dores6():
    focus6()
    res()
    time.sleep(1)

def ressick1():
    focus1()
    pvp()
    take_res()
    time.sleep(1)
    
def ressick2():
    focus2()
    pvp()
    take_res()
    time.sleep(1)
    
def ressick3():
    focus3()
    pvp()
    take_res()
    time.sleep(1)
    
def ressick4():
    focus4()
    pvp()
    take_res()
    time.sleep(1)

def ressick5():
    focus5()
    pvp()
    take_res()
    time.sleep(1)
    
def ressick6():
    focus6()
    pvp()
    take_res()
    focus1()
    time.sleep(1)
    
def rescycle():
    dores1()
    dores2()
    dores3()
    dores4()
    dores5()
    dores6()
    time.sleep(1)
    ressick1()
    ressick2()
    ressick3()
    ressick4()
    ressick5()
    ressick6()
    
def say_inv():
    time.sleep(1)
    type_something('/s welcome',.25)
    time.sleep(1)

def party1():
    time.sleep(.5)
    focus1()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 1')
    time.sleep(.5)

def party2():
    time.sleep(.5)
    focus2()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 2')
    time.sleep(.5)

def party3():
    time.sleep(.5)
    focus3()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 3')
    time.sleep(.5)

def party4():
    time.sleep(.5)
    focus4()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 4')
    time.sleep(.5)

def party5():
    time.sleep(.5)
    focus5()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 5')
    time.sleep(.5)

def party6():
    time.sleep(.5)
    focus6()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 6')
    time.sleep(.5)

def partyall():
    party1()
    party2()
    party3()
    party4()
    party5()
    party6()

def wait_jump():
    time.sleep(.5)
    pyautogui.press('space')
    time.sleep(.5)
    
def from_start():
    move_me('e', 3, 'turn slight right from start')
    wait_jump()
    move_me('up', 16, 'move forward to first strafe point')
    wait_jump()
    move_me('q', 3, 'move left')
    wait_jump()
    move_me('up', 4, 'move up')
    wait_jump()
    move_me('q', 7, 'move left')
    wait_jump()
    move_me('up', 6, 'move up')
    wait_jump()
    move_me('q', 18, 'move left')
    wait_jump()
    move_me('up', 9, 'move up')
    wait_jump()
    move_me('q', 9, 'move left')
    wait_jump()

def create1():
    time.sleep(.5)
    pyautogui.click(x=391, y=283)#focus
    print('focus wow1')
    time.sleep(.5)
    pyautogui.click(x=671, y=513)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=137, y=243) #orc
    pyautogui.click(x=137, y=243) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=411, y=602) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=411, y=602) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=363, y=574) #random
    print('click random 3, just to be safe')
    time.sleep(2)

def focus1():
    time.sleep(.5)
    pyautogui.click(x=391, y=283)#focus
    print('focus wow1')
    
def create2():
    time.sleep(.5)
    pyautogui.click(x=937, y=172)#focus
    print('focus wow2')
    time.sleep(.5)
    pyautogui.click(x=1463, y=513)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=937, y=242) #orc
    pyautogui.click(x=937, y=242) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1206, y=599) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1206, y=599) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1206, y=599) #random
    print('click random 3, just to be safe')
    time.sleep(2) 

def focus2():
    time.sleep(.5)
    pyautogui.click(x=937, y=172)#focus
    print('focus wow2')

def create3():
    time.sleep(.5)
    pyautogui.click(x=1641, y=96)#focus
    print('focus wow3')
    time.sleep(.5)
    pyautogui.click(x=1793, y=512)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=1262, y=242) #orc
    pyautogui.click(x=1262, y=242) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1524, y=599) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1524, y=599) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1524, y=599) #random
    print('click random 3, just to be safe')
    time.sleep(2)

def focus3():
    time.sleep(.5)
    pyautogui.click(x=1641, y=96)#focus
    print('focus wow4')
    
def create4():
    time.sleep(.5)
    pyautogui.click(x=91, y=736)#focus
    print('focus wow4')
    time.sleep(.5)
    pyautogui.click(x=682, y=920)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=130, y=650) #orc
    pyautogui.click(x=130, y=650) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=400, y=1007) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=400, y=1007) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=400, y=1007) #random
    print('click random 3, just to be safe')
    time.sleep(2)
    
def focus4():
    time.sleep(.5)
    pyautogui.click(x=91, y=736)#focus
    print('focus wow4')
    
def create5():
    time.sleep(.5)
    pyautogui.click(x=954, y=818)#focus
    print('focus wow4')
    time.sleep(.5)
    pyautogui.click(x=1470, y=921)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=928, y=647) #orc
    pyautogui.click(x=928, y=647) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1200, y=1006) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1200, y=1006) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1200, y=1006) #random
    print('click random 3, just to be safe')
    time.sleep(2)
    
def focus5():
    time.sleep(.5)
    pyautogui.click(x=954, y=818)#focus
    print('focus wow4')

def create6():
    time.sleep(.5)
    pyautogui.click(x=1872, y=733)#focus
    print('focus wow4')
    time.sleep(.5)
    pyautogui.click(x=1800, y=918)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=1258, y=646) #orc
    pyautogui.click(x=1258, y=646) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1528, y=1006) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1528, y=1006) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1528, y=1006) #random
    print('click random 3, just to be safe')
    time.sleep(2)
    
def focus6():
    time.sleep(.5)
    pyautogui.click(x=1872, y=733)#focus
    print('focus wow4')
    
def leavevid1():
    focus1()
    time.sleep(.5)
    pyautogui.click(x=345, y=345)#vid
    time.sleep(.5)
    print('close vid 1')

def leavevid2():
    focus2()
    time.sleep(.5)
    pyautogui.click(x=1109, y=345)#vid
    time.sleep(.5)
    print('close vid 2')
    
def leavevid3():
    focus3()
    time.sleep(.5)
    pyautogui.click(x=1465, y=345)#vid
    time.sleep(.5)
    print('close vid 3')
    
def leavevid4():
    focus4()
    time.sleep(.5)
    pyautogui.click(x=340, y=750)#vid
    time.sleep(.5)  
    print('close vid 4')

def leavevid5():
    focus5()
    time.sleep(.5)
    pyautogui.click(x=1106, y=748)#vid
    time.sleep(.5)  
    print('close vid 5')

def leavevid6():
    focus6()
    time.sleep(.5)
    pyautogui.click(x=1466, y=749)#vid
    time.sleep(.5)  
    print('close vid 6') 
   
def create_char():
    time.sleep(.5)
    create1()
    create2()
    create3()
    create4()
    create5()
    create6()
    time.sleep(2)
    pyautogui.press('enter')
    print('press enter')
    time.sleep(1)
    pyautogui.press('enter')
    print('press enter again to enter world')
    print('wait 12 seconds...')
    time.sleep(1)
    print('12...')
    time.sleep(1)
    print('11...')
    time.sleep(1)
    print('10...')
    time.sleep(1)
    print('9...')
    time.sleep(1)
    print('8...')
    time.sleep(1)
    print('7...')
    time.sleep(1)
    print('6...')
    time.sleep(1)
    print('5...')
    time.sleep(1)
    print('4...')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('press escape to leave video')
    pyautogui.press('escape')
    time.sleep(.25)
    print('click yes to skip')
    leavevid1()
    leavevid2()
    leavevid3()
    leavevid4()
    leavevid5()
    leavevid6()
    time.sleep(5)

def hk1():
    holder = pyautogui.locateOnScreen('stophk1.png', region=(200, 150, 150, 150))
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        
        return True
    
    return False

def hk2():
    holder = pyautogui.locateOnScreen('stophk2.png', region=(900, 150, 150, 150))
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        
        return True
    
    return False

def hk3():
    holder = pyautogui.locateOnScreen('stophk3.png', region=(1650, 150, 150, 150))
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        
        return True
    
    return False

def hk4():
    holder = pyautogui.locateOnScreen('stophk4.png', region=(2020, 150, 150, 150))
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        
        return True
    
    return False

def hk5():
    holder = pyautogui.locateOnScreen('stophk5.png', region=(200, 600, 150, 150))
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        
        return True
    
    return False

def hk6():
    holder = pyautogui.locateOnScreen('stophk6.png', region=(900, 600, 150, 150))
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        
        return True
    
    return False

def checkhk():
    holder = pyautogui.locateOnScreen('stophk5.png')
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        print('17 hks reached')
        return True
    
    return False
    

def attack():
    time.sleep(0.5)
    pyautogui.press('1')
    pyautogui.press('2')

def kill():
    #lets go for 15
    count = 0
    pyautogui.press('h')
    while not checkhk():
        attack()

def logout():
    time.sleep(1)
    print('logging out')
    type_something('/logout',0.25)
    time.sleep(25)

def delete1():
    time.sleep(1)
    print('deleting char1')
    focus1()
    time.sleep(.5)
    pyautogui.click(x=629, y=597) #delete
    pyautogui.click(x=629, y=597) #delete
    time.sleep(.5)
    
def delete2():
    time.sleep(1)
    print('deleting char2')
    focus2()
    time.sleep(.5)
    pyautogui.click(x=1422, y=597) #delete
    pyautogui.click(x=1422, y=597) #delete
    time.sleep(.5)

def delete3():
    time.sleep(1)
    print('deleting char3')
    focus3()
    time.sleep(.5)
    pyautogui.click(x=1745, y=600) #delete
    pyautogui.click(x=1745, y=600) #delete
    time.sleep(.5)
  
def delete4():
    time.sleep(1)
    print('deleting char4')
    focus4()
    time.sleep(.5)
    pyautogui.click(x=622, y=1002) #delete
    pyautogui.click(x=622, y=1002) #delete
    time.sleep(.5)

def delete5():
    time.sleep(1)
    print('deleting char5')
    focus5()
    time.sleep(.5)
    pyautogui.click(x=1417, y=1002) #delete
    pyautogui.click(x=1417, y=1002) #delete
    time.sleep(.5)
    
def delete6():
    time.sleep(1)
    print('deleting char6')
    focus6()
    time.sleep(.5)
    pyautogui.click(x=1748, y=1002) #delete
    pyautogui.click(x=1748, y=1002) #delete
    time.sleep(.5)
       
def delete():
    delete1()
    delete2()
    delete3()
    delete4()
    delete5()
    delete6()
    type_something('delete', .25)
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(1)

def join_counter():
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    type_something('/s kirtonos',.25)
    time.sleep(1)
   
def main():
    count = 1
    print('starting in 3...')
    time.sleep(1)
    print('starting in 2...')
    time.sleep(1)
    print('starting in 1...')
    time.sleep(1)
    print('welcome...')
    while True:
        print('Character #: ', count)
        time.sleep(1)
        create_char()
        time.sleep(50)
        say_inv()
        partyall()
        say_inv()
        partyall()
        focus1()
        mulgore()
        after_log()
        rescycle()
        toggle() #turn on
        focus5()
##        join_counter() #added until starter removed
##        partyall() #add unti start removed
##        join_counter() #added until starter removed
##        partyall() #add unti start removed
        kill()
        logout()
        delete()
        count = count + 1
    

main()


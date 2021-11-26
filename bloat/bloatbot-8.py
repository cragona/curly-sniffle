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

def razorhill7():
    focus7()
    delete_hearthstone()
    unstuck()

def razorhill8():
    focus8()
    delete_hearthstone()
    unstuck()

def after_log():
    move_through_hole()
    move_up_hill()
    toggle() #off
    razorhill1()
    razorhill2()
    razorhill3()
    razorhill4()
    razorhill5()
    razorhill6()
    razorhill7()
    razorhill8()
    time.sleep(16)

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

def dores7():
    focus7()
    res()
    time.sleep(1)

def dores8():
    focus8()
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
    time.sleep(1)

def ressick7():
    focus7()
    pvp()
    take_res()
    time.sleep(1)

def ressick8():
    focus8()
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
    dores7()
    dores8()
    time.sleep(1)
    ressick1()
    ressick2()
    ressick3()
    ressick4()
    ressick5()
    ressick6()
    ressick7()
    ressick8()
    
def say_inv():
    time.sleep(1)
    type_something('/s welcome',.25)
    time.sleep(1)

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

def party7():
    time.sleep(.5)
    focus7()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 7')
    time.sleep(.5)

def party8():
    time.sleep(.5)
    focus8()
    time.sleep(.25)
    type_something('/click StaticPopup1Button1',0.01)
    print('accept party 8')
    time.sleep(.5)


def partyall():
    party2()
    party3()
    party4()
    party5()
    party6()
    party7()
    party8()

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
    pyautogui.click(x=335, y=295)#focus
    print('focus wow1')
    time.sleep(.5)
    pyautogui.click(x=604, y=495)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=137, y=153) #orc
    pyautogui.click(x=137, y=153) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=363, y=574) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=363, y=574) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=363, y=574) #random
    print('click random 3, just to be safe')
    time.sleep(1)

def focus1():
    time.sleep(.5)
    pyautogui.click(x=335, y=295)#focus
    print('focus wow1')
    
def create2():
    time.sleep(.5)
    pyautogui.click(x=1059, y=295)#focus
    print('focus wow2')
    time.sleep(.5)
    pyautogui.click(x=1277, y=490)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=854, y=152) #orc
    pyautogui.click(x=854, y=152) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1080, y=575) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1080, y=575) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1080, y=575) #random
    print('click random 3, just to be safe')
    time.sleep(1) 

def focus2():
    time.sleep(.5)
    pyautogui.click(x=1059, y=295)#focus
    print('focus wow2')

def create3():
    time.sleep(.5)
    pyautogui.click(x=1734, y=267)#focus
    print('focus wow3')
    time.sleep(.5)
    pyautogui.click(x=1998, y=488)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=1578, y=154) #orc
    pyautogui.click(x=1578, y=154) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1811, y=575) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1811, y=575) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1811, y=575) #random
    print('click random 3, just to be safe')
    time.sleep(1)

def focus3():
    time.sleep(.5)
    pyautogui.click(x=1734, y=267)#focus
    print('focus wow4')
    
def create4():
    time.sleep(.5)
    pyautogui.click(x=2199, y=296)#focus
    print('focus wow4')
    time.sleep(.5)
    pyautogui.click(x=2440, y=492)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=1979, y=153) #orc
    pyautogui.click(x=1979, y=153) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=2186, y=575) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=2186, y=575) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=2186, y=575) #random
    print('click random 3, just to be safe')
    time.sleep(1)
    
def focus4():
    time.sleep(.5)
    pyautogui.click(x=2199, y=296)#focus
    print('focus wow4')
    
def create5():
    time.sleep(.5)
    pyautogui.click(x=265, y=806)#focus
    print('focus wow5')
    time.sleep(.5)
    pyautogui.click(x=579, y=928)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=136, y=597) #orc
    pyautogui.click(x=136, y=597) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=367, y=1010) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=367, y=1010) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=367, y=1010) #random
    print('click random 3, just to be safe')
    time.sleep(1)
    
def focus5():
    time.sleep(.5)
    pyautogui.click(x=265, y=806)#focus
    print('focus wow5')

def create6():
    time.sleep(.5)
    pyautogui.click(x=1066, y=838)#focus
    print('focus wow6')
    time.sleep(.5)
    pyautogui.click(x=1321, y=937)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=858, y=582) #orc
    pyautogui.click(x=858, y=582) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1080, y=1012) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1080, y=1012) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1080, y=1012) #random
    print('click random 3, just to be safe')
    time.sleep(1)
    
def focus6():
    time.sleep(.5)
    pyautogui.click(x=1066, y=838)#focus
    print('focus wow6')

def create7():
    time.sleep(.5)
    pyautogui.click(x=1769, y=699)#focus
    print('focus wow7')
    time.sleep(.5)
    pyautogui.click(x=2037, y=926)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=1577, y=581) #orc
    pyautogui.click(x=1577, y=581) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=1812, y=1006) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=1812, y=1006) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=1812, y=1006) #random
    print('click random 3, just to be safe')
    time.sleep(1)
    
def focus7():
    time.sleep(.5)
    pyautogui.click(x=1769, y=699)#focus
    print('focus wow7')

def create8():
    time.sleep(.5)
    pyautogui.click(x=2181, y=761)#focus
    print('focus wow8')
    time.sleep(.5)
    pyautogui.click(x=2454, y=929)#create
    print('click create')
    time.sleep(.5)
    pyautogui.click(x=1977, y=590) #orc
    pyautogui.click(x=1977, y=590) #orc
    print('click orc')
    time.sleep(1)
    pyautogui.click(x=2204, y=1005) #random
    print('click random 1')
    time.sleep(1)
    pyautogui.click(x=2204, y=1005) #random
    print('click random 2')
    time.sleep(1)
    pyautogui.click(x=2204, y=1005) #random
    print('click random 3, just to be safe')
    time.sleep(1)
    
def focus8():
    time.sleep(.5)
    pyautogui.click(x=2181, y=761)#focus
    print('focus wow8')

def leavevid1():
    time.sleep(.5)
    pyautogui.click(x=303, y=331)#vid
    time.sleep(.5)
    print('close vid 1')

def leavevid2():
    time.sleep(.5)
    pyautogui.click(x=1021, y=332)#vid
    time.sleep(.5)
    print('close vid 2')
    
def leavevid3():
    time.sleep(.5)
    pyautogui.click(x=1748, y=332)#vid
    time.sleep(.5)
    print('close vid 3')
    
def leavevid4():
    time.sleep(.5)
    pyautogui.click(x=2175, y=332)#vid
    time.sleep(.5)  
    print('close vid 4')

def leavevid5():
    time.sleep(.5)
    pyautogui.click(x=319, y=767)#vid
    time.sleep(.5)  
    print('close vid 5')

def leavevid6():
    time.sleep(.5)
    pyautogui.click(x=1014, y=764)#vid
    time.sleep(.5)  
    print('close vid 6')

def leavevid7():
    time.sleep(.5)
    pyautogui.click(x=1761, y=762)#vid
    time.sleep(.5)  
    print('close vid 7')
    
def leavevid8():
    time.sleep(.5)
    pyautogui.click(x=2181, y=761)#vid
    time.sleep(.5)  
    print('close vid 8') 
   
def create_char():
    time.sleep(.5)
    create1()
    create2()
    create3()
    create4()
    create5()
    create6()
    create7()
    create8()
    time.sleep(1)
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
    leavevid7()
    leavevid8()
    time.sleep(5)

def checkhk():
    holder = pyautogui.locateOnScreen('stophk.png')
    stringHolder = str(holder)
    if(stringHolder == "None"):
        return False
    else:
        print('15 hks reached')
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
    pyautogui.click(x=558, y=573) #delete
    pyautogui.click(x=558, y=573) #delete
    time.sleep(.5)
    
def delete2():
    time.sleep(1)
    print('deleting char2')
    focus2()
    time.sleep(.5)
    pyautogui.click(x=1278, y=574) #delete
    pyautogui.click(x=1278, y=574) #delete
    time.sleep(.5)

def delete3():
    time.sleep(1)
    print('deleting char3')
    focus3()
    time.sleep(.5)
    pyautogui.click(x=1992, y=572) #delete
    pyautogui.click(x=1992, y=572) #delete
    time.sleep(.5)
  
def delete4():
    time.sleep(1)
    print('deleting char4')
    focus4()
    time.sleep(.5)
    pyautogui.click(x=2404, y=571) #delete
    pyautogui.click(x=2404, y=571) #delete
    time.sleep(.5)

def delete5():
    time.sleep(1)
    print('deleting char5')
    focus5()
    time.sleep(.5)
    pyautogui.click(x=558, y=1009) #delete
    pyautogui.click(x=558, y=1009) #delete
    time.sleep(.5)
    
def delete6():
    time.sleep(1)
    print('deleting char6')
    focus6()
    time.sleep(.5)
    pyautogui.click(x=1274, y=1008) #delete
    pyautogui.click(x=1274, y=1008) #delete
    time.sleep(.5)

def delete7():
    time.sleep(1)
    print('deleting char7')
    focus7()
    time.sleep(.5)
    pyautogui.click(x=2000, y=1006) #delete
    pyautogui.click(x=2000, y=1006) #delete
    time.sleep(.5)

def delete8():
    time.sleep(1)
    print('deleting char8')
    focus8()
    time.sleep(.5)
    pyautogui.click(x=2405, y=1004) #delete
    pyautogui.click(x=2405, y=1004) #delete
    time.sleep(.5)
       
def delete():
    delete1()
    delete2()
    delete3()
    delete4()
    delete5()
    delete6()
    delete7()
    delete8()
    type_something('delete', .25)
    time.sleep(.5)
    pyautogui.press('enter')
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
        say_inv()
        partyall()
        say_inv()
        partyall()
        focus1()
        from_start()
        after_log()
        rescycle()
        toggle() #turn on
        focus1()
        kill()
        logout()
        delete()
        count = count + 1
    

main()


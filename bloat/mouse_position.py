import pyautogui

def main():
    count = 0
    while True:
        count = count + 1
        if count % 100 == 0:
             print(pyautogui.position())
        
    
main()

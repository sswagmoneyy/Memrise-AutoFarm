import time
import pyautogui
pyautogui.PAUSE = 0.05 # ←Change this to change the ammount of delay in the script (u can use this so ur system can catch up with the script)

sleep = time.sleep
pyClick = pyautogui.click
pyMove = pyautogui.moveTo
pyPress = pyautogui.press
kDown = pyautogui.keyDown
kUp = pyautogui.keyUp
pyPause = pyautogui.PAUSE

while True:
    pyClick(780, 392)
    sleep(0.15)
    
    # This is how many tabs the script will open
    for i in range(30):
        pyautogui.middleClick(820, 430)
    sleep(15)
    
   # This is the ammount of times u control tab (must be the same value as pyautogui.middleClick)
    for i in range(30):
        kDown('ctrl')
        pyPress('tab')
        sleep
        pyPress('v')
        pyPress('enter')
        kUp('ctrl')

    for i in range(30):
        kDown('ctrl')
        pyPress('w')
        kUp('ctrl')
    pyClick(685, 330)

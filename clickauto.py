from pynput.mouse import Button, Controller
import time
mouse = Controller()

def click(key):
    i= True
    x = key.char 
    if x == "n":
        i == False
        mouse.release(Button.left)
    elif x == "0" and i == True:
        mouse.press(Button.left)
    
         
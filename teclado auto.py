
import time
from pynput import keyboard
import clickauto as ca


while True:  
    keyboard = keyboard
    cont = 0
    def on_press(key):   
        try:
            x = key.char
            if x == "0":
                ca.click(key)
        except:
            print("aqui")
            exit()

    

    with keyboard.Listener(
            on_press=on_press,
            ) as listener:
        listener.join()
print("aaaaaaa")
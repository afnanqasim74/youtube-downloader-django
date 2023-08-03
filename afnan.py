import pyautogui #imports pyautogui
import keyboard #imports keyboard


def autoclicker(): #declares the function
    while True: #makes a infinite loop
        pyautogui. click() #makes your mouse click
        if keyboard.is_pressed('b'): #detects if b is pressed
            break #if b is detected it breaks the loop


autoclicker()
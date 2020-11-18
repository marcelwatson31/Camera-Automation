# This is a camra application that takes a picture of you 
# Might make it on repeat and take multiple photos then upload them and do something like edit them with text or something

import subprocess
import time
import pyautogui


def take_the_pic():
    pictures_taken = int(input("How many pictures do you want taken?"))
    picture_taken_interval = int(input("What is the interval time between pictures do you want?"))
    for i in range(pictures_taken):
        time.sleep(picture_taken_interval)
        take_a_photo = pyautogui.press('enter')

    subprocess.run('start microsoft.windows.camera:', shell=True)
    time.sleep(3)

facebook = "facebook.com"

def upload_photo():

    subprocess.run('start chrome.exe', shell=True)
    time.sleep(3)
    pyautogui.write(facebook)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press("tab", presses = 41, interval=.05)
    pyautogui.press("enter")
    time.sleep(1.7)
    pyautogui.press("tab", presses=11, interval=.2)
    time.sleep(.1)
    pyautogui.press("down", presses=4, interval=.08)
    time.sleep(.1)
    pyautogui.press("enter")
    time.sleep(.3)
    pyautogui.press("tab", presses=1)
    time.sleep(.1)
    pyautogui.press("enter")

    #is not consistent and needs you to be already logged in to facebook and have the same amount of groups as me when tabbing also doesnt tab to last camera roll folder

    
take_the_pic()
close_app = pyautogui.hotkey('alt', 'f4')

upload_photo()









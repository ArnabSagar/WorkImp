import pyautogui
import time  # for timer


def invertMouse(seconds, minutes):
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo

def toFirstTab(seconds, minutes):  # This returns you to your first tab on chrome
    pyautogui.hotkey('ctrl', '1')
    exit();

def alertMessages(seconds, minutes):  # Opens two popups
    time.sleep(1)
    seconds += 1
    if seconds == 5:
        seconds = 0
        minutes += 1
    pyautogui.alert(text='So it looks like someone is slacking off still. Get back to work', title='Really? Again?', button='Sorry :(')
    pyautogui.alert(text='Do you promise?', title='Hmmm are you sure...?', button='I promise')

class MainScript:

    def __init__(self):
        tabbedTimer = 'true' # timer while not studying
        seconds = 0
        minutes = 0
        while tabbedTimer:  # Generic timer
            time.sleep(1)
            seconds+= 1
            if seconds == 5:
                seconds = 0
                minutes += 1
            if minutes == 1:  # If they are tabbed for 1 minute
                invertMouse(seconds, minutes)
            if minutes == 2:  # If they are tabbed for 3 minutes
                invertMouse(seconds, minutes)
                alertMessages(seconds, minutes)
            if minutes == 3:
                toFirstTab(seconds, minutes)







test1 = MainScript()







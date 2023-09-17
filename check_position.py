import pyautogui
import pyttsx3
import time

engine = pyttsx3.init()
# for i in range(8,0,-1):
#     engine.say(i)
time.sleep(5)
x,y = pyautogui.position()
print(x,y)
engine.say("Done")
engine.runAndWait()
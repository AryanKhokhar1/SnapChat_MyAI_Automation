import pyautogui
import time
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyperclip

url = "https://web.snapchat.com/?ref=snapchat_dot_com_login_cta"
webbrowser.open_new_tab(url)
time.sleep(7)
pyautogui.moveTo(141,384)
pyautogui.leftClick()
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech (words per minute)
engine.setProperty("volume", 1) 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
time.sleep(3)
def pushinput(query):
    pyautogui.moveTo(540,967)
    pyautogui.leftClick()
    pyautogui.write(query,0.01)
    time.sleep(1)
    pyautogui.moveTo(1748,969)
    pyautogui.leftClick()
    time.sleep(1)

def getoutput():
    time.sleep(0.5)
    pyautogui.moveTo(502,849)
    pyautogui.rightClick()
    pyautogui.moveTo(679,843)
    pyautogui.leftClick()
    return pyperclip.paste()

engine.say("Hii, Aaryan")
engine.runAndWait()
while(True):
    time.sleep(1)
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

# Perform speech recognition
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("You said:", recognized_text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        engine.say("Sorry, I couldn't understand. Please try again")
        engine.runAndWait()
        continue
    except sr.RequestError as e:
        print(f"Error making the request; {e}")
        engine.say("Sorry, I couldn't understand. Please try again")
        engine.runAndWait()
        continue
    pushinput(recognized_text)
    time.sleep(1)
    answer = getoutput()
    time.sleep(1)
    engine.say(answer)
    engine.runAndWait()
    time.sleep(1)
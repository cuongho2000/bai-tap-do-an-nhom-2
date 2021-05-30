import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
r=sr.Recognizer()
def speak(text):
    tts = gTTS(text=text,lang='vi')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
while True:
    with sr.Microphone() as source:
        audio_data=r.record(source, duration=5)
        # print("Recognizing....")
        try:
            text=r.recognize_google(audio_data, language='vi')
        except:
            text = ''
        print(text)
        if text == '':
            robot_brain = 'Xin mời bạn nói...'
            print(robot_brain)
            speak(robot_brain)
        elif 'Xin chào' in text:
            robot_brain = 'Xin chào! Bạn cần tôi giúp gì'
            print(robot_brain)
            speak(robot_brain)
        elif 'Tôi cần bạn đưa ra câu trả lời' in text:
            robot_brain = 'Mời bạn nói'
            print(robot_brain)
            speak(robot_brain)
        elif 'Bạn thấy tôi như thế nào' in text:
            robot_brain = 'Bạn rất đẹp trai'
            print(robot_brain)
            speak(robot_brain)
        elif 'Thế thằng bạn tôi có đẹp trai không' in text:
            robot_brain = 'Tất nhiên là không, Dương không đẹp trai'
            print(robot_brain)
            speak(robot_brain)
        else:
            robot_brain = 'Bạn đang nói gì vậy'
            speak(robot_brain)
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files

r = sr.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:
def record_audio(ask= False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            rana_speak(ask)
        audio = r.listen(source) # listen for the audio via source
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            rana_speak('I did not get that')
        except sr.RequestError:
            rana_speak('Sorry, the service is down') # error: recognizer is not connected
        print(f"You: {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def rana_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Rana: {audio_string}") # print what app said
    os.remove(audio_file)  # remove audio file

def respond(voice_data):
    # 1: name
    if 'what is your name' in voice_data:
        rana_speak('My name is Rana')

    # 2: time
    if 'what time is it' in voice_data:
        rana_speak(ctime())
    
    # 3: Google Search
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        rana_speak('Here is what i found for ' + search)

    # 4: Location
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        rana_speak('Here is the the location of ' + location)
    if 'exit' in voice_data:
        rana_speak("going offline")
        exit()
    
time.sleep(1)

rana_speak('How can i help you')
while 1:
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
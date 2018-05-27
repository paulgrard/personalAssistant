import snowboydecoder
# try:
#     from urllib.parse import urlparse
# except ImportError:
#      from urlparse import urlparse
from google_speech import Speech



def detected_callback():
    print("hotword detected")
    # engine = pyttsx3.init();
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', '26')  # changes the voice
    # engine.say('Bonjour, ceci est un test.')
    # engine.runAndWait() ;
    # say "Hello World"
    text = "Bonjour monsieur. Comment allez-vous ?"
    lang = "fr"
    speech = Speech(text, lang)
    speech.play()
detector = snowboydecoder.HotwordDetector("voices/jarvis.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)


# import speech_recognition as sr
#
# # Record Audio
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
# # Speech recognition using Google Speech Recognition
# try:
#     print("You said: " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

import snowboydecoder
from google_speech import Speech

def detected_callback():
    print("hotword detected")
    text = "Bonjour monsieur. Comment allez-vous ?"
    lang = "fr"
    speech = Speech(text, lang)
    sox_effects = ("speed", "1.1")
    speech.play(sox_effects)
    
detector = snowboydecoder.HotwordDetector("voices/jarvis.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
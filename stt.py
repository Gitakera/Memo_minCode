# pip install SpeechRecognition
# sudo apt-get install portaudio19-dev
# pip install PyAudio
# use to run if error : LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python stt.py
# more examples at https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now:")
    audio = recognizer.listen(source)
    
text = recognizer.recognize_google(audio)
print(f"Transcript: {text}")


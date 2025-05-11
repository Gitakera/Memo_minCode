# pip install gtts
# sudo apt install ffmpeg


import os
from gtts import gTTS

tts = gTTS(text="Hello world, comment ça va Mamitiahnà ? Votre maman est là ?", lang="fr")
tts.save("hello.mp3")
os.system("ffplay -nodisp -autoexit hello.mp3")

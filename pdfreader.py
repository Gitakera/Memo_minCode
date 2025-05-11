# pip install PyPDF2
# pip install playsound
# importing the modules 
import PyPDF2 
import playsound
from gtts import gTTS
  
# path of the PDF file 
path = open('fichier.pdf', 'rb') 
  
# creating a PdfFileReader object 
pdfReader = PyPDF2.PdfReader(path) 
  
# the page with which you want to start 
# this will read the page of 25th page. 
from_page = pdfReader.pages[5]
  
# extracting the text from the PDF 
text = from_page.extract_text() 

print(text) 
tts = gTTS(text=text, lang="fr")

tts.save("reading.mp3")
playsound.playsound("reading.mp3", True)

import multiprocessing
from playsound import playsound

# p = multiprocessing.Process(target=playsound, args=("file.mp3",))
# p.start()
# p.join() // add the line before terminate
# p.terminate()
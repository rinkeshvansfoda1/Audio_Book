import pyttsx3
import PyPDF2
from google_trans_new import google_translator

#address of audiobook.
book=open('D://audiobook//book1.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)

#it will read book total number of pages.
pages=pdfReader.numPages
print('Number of pages in pdf are:',pages)

#it will ask where from where to start read. and also take note that if page number is 5 then you will have to type 4, because it starts from 0 not from 1.
lines=int(input("Enter the page where you want to start:"))
page=pdfReader.getPage(lines)
text=page.extractText()

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',100)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#translator = Translator()
translator = google_translator()  
translate_text = translator.translate('สวัสดีจีน',lang_tgt='hi')  
print(translate_text)
#translation=translator.translate("Hello", dest='hi')

#text = translator.translate(text, dest='hi')
engine.say(translate_text)
engine.runAndWait()
translator = google_translator()  
translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')  
print(translate_text)
#output: Hello china
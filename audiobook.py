import pyttsx3
import PyPDF2

#address of audiobook.
book=open('D://audiobook//book.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)

#it will read book total number of pages.
pages=pdfReader.numPages
print('Number of pages in pdf are:',pages)

#it will ask where from where to start read. and also take note that if page number is 5 then you will have to type 4, because it starts from 0 not from 1.
lines=int(input("Enter the page where you want to start:"))
page=pdfReader.getPage(lines)
text=page.extractText()

engine=pyttsx3.init('sapi5')
#rate is the at what speed we want to listen.
engine.setProperty('rate',100)
voices = engine.getProperty('voices')
#1 is for female voice and 0 is for male voice
engine.setProperty('voice', voices[1].id) 
#we can also print the text which he/she is speaking like print(text).
engine.say(text)
engine.runAndWait()
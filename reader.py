# Credit https://github.com/DhairyaShah-Programmer
import PyPDF2 as pdf
import pyttsx3 as tts

pdfFileObj = open('Python.pdf', 'rb') 

pdfReader = pdf.PdfFileReader(pdfFileObj)

print("Welcome to PyReader\n")
page = int(input("Enter page number of the page of the PDF from you have to start: "))
pageObj = pdfReader.getPage(page)


pdfText = pageObj.extractText()

print(pdfText)
engine = tts.init()
engine.say(pdfText)
engine.runAndWait()
# print(pdfReader.numPages)

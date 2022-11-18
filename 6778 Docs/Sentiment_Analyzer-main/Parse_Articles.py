# importing required modules
import PyPDF2
#Now give the pdf name
pdfFileObj = open(r'filepath', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages) # will give total number of pages in pdf


text=(pdfFileObj.extractText())
text=text.split(",")
text

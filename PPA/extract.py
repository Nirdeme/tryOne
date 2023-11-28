
import pypdf2

# creating a pdf file object 
pdfFileObj = open('F:\\ECSGLO-P00006-04.09.2023.pdf', 'rb') 
 
# creating a pdf reader object 
pdfReader = pypdf2.PdfReader(pdfFileObj) 
 
# printing number of pages in pdf file 
#print(len(pdfReader.pages)) 
 
# creating a page object 
pageObj = pdfReader.pages[0] 
 
# extracting text from page 
print(pageObj.extract_text()) 
 
 
 
 
# closing the pdf file object 
#pdfFileObj.close()
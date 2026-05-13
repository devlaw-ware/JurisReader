import fitz # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    text = "" #Initialize a empty variable , that will store all the text from the pdf file

    for page in doc:
        text += page.get_text()

    return text

#Fitz is a lib of python, that we use tdo extract text from pdf files
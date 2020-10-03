from PyPDF2 import PdfFileReader, PdfFileWriter
from tqdm import trange
from os import listdir

#didn't make a module for function because it is just one
def is_pdf(file):
    if file[-4::].lower() == ".pdf":
        return True
    else:
        return False

def split(pdf_path):
    reader = PdfFileReader(pdf_path)

    
    for page in trange(reader.getNumPages()):
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(page))
        with open(f"{pdf_path}_{page+1}.pdf", "wb") as fq:
            writer.write(fq)


def split_all():
    for pdf in listdir():
        if is_pdf(pdf):
            split(pdf)


split_all()

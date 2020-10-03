
"""
Important note!!!
This Script merges all .pdf files in the directory it is executed.
The files will be merged according to theis alphabetic order!!!
"""
import PyPDF2 as pdf
from tqdm import trange
import os


class Merge():

    def append_to_merge(self):
        for pdf in trange(len(self.pdfs_path)):
            self.merged.append(open(self.pdfs_path[pdf], "rb"))


    def write_changes(self):
        self.merged.write(open(self.write_to, "wb"))


    def __init__(self, write_to, pdfs_path):
        self.write_to = write_to
        self.pdfs_path = pdfs_path
        self.merged = pdf.PdfFileMerger()
        self.append_to_merge()
        self.write_changes()


def is_pdf(file):
    if file[-4::].lower() == ".pdf":
        return True
    else:
        return False


#Uncomment the line bellow
#Merge(input("Enter new files' name:\n"), [file for file in os.listdir() if is_pdf(file)])






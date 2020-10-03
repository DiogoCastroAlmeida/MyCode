from PyPDF2 import PdfFileWriter, PdfFileReader

class Rotate():
    writer = PdfFileWriter()

    def rotate_page(self, path, page_index): #pyton index starts with 0
        reader = PdfFileReader(path)

        page = reader.getPage(int(page_index)).rotateClockwise(90)
        Rotate.writer.addPage(page)


    def rotate_all_pages(self, path):
        for page in range(PdfFileReader(path).getNumPages()):
            self.rotate_page(path, page)


#Uncomment the lines bellow
#Rotate().rotate_page("ENTERPATHHERE", int("ENTERPAGEINDEXHERE"))
#Rotate().rotate_all_pages("ENTERPATHHERE")
with open(input("Enter name for new files' name\n"), "wb") as fh:
    Rotate.writer.write(fh)

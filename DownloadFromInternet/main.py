import requests
import getpass

def redundant_input(input_text, redundancy): #in case input lengh is zero, return the original file's name
    to_return = input(input_text)
    if len(to_return) == 0:
        return to_return
    else:
        return redundancy.split("/")[-1]

class Download():


    def __init__(self, url):
        try:
            self.r = requests.get(url)
            print ("Content downloaded")
        except:
            print("Invalid URL")


    def download(self, path):
        with open(path, "wb") as file:
            file.write(self.r.content)
            print ("Wrote to file.\nDownload Completed")

url = input("Enter Url: ")
username = getpass.getuser()
download_path = f"C:/Users/{username}/Downloads/{redundant_input('Enter new file name(with extension): ', url)}"
dw = Download(url)
dw.download(download_path)


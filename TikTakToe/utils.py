import pickle
import os

def reverse_list(lst):
    return lst[::-1]

def picklle(path, object):
    with open(path, "wb") as file:
        pickle.dump(object, file)
        
def unpicklle(path):
    with open(path, "rb") as file:
        return pickle.load(file)

def file_exits(path_to_file):
    #designed for Windows only
    #put a dot if refering to a file in the working directory
    paths = path_to_file.split(r"\\")
    #print(paths)
    #print(os.listdir(paths[0]))
    if paths[-1] in os.listdir(paths[0]):
        return True
    else:
        return False  

#print(file_exits(r".\\README.md"))

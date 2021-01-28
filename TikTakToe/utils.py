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
    # designed for Windows only
    # put a dot if refering to a file in the working directory
    paths = path_to_file.split(r"\\")
    # print(paths)
    # print(os.listdir(paths[0]))
    if paths[-1] in os.listdir(paths[0]):
        return True
    else:
        return False  


def is_odd(number):
    if number%2 == 1:
        return True
    else:
        return False


def subtract_one_to_all_elements_in_a_list(to_add):
    list_to_return = []
    for item in to_add:
        list_to_return.append(item-1)
    return list_to_return


def int_a_list(object_):
    inted_list = []
    for element in object_:
        inted_list.append(int(element))
    return inted_list

def is_int(object_):
    try:
        int(object_)
    except :
        return False
    else:
        return True
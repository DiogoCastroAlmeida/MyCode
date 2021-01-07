#Utilities module

#This module serves as a place to store functions to use in other modules that aren't relatted with the purpose of the programm



def is_list_empty(list):
    if list == []:
        return True
    elif list != []:
        return False
    else:
        return None


def convert_empty_list_to_none(list):
    if is_list_empty(list):
        return None
    else:
        return list


def print_extra_line(string):
    print(string)
    print()

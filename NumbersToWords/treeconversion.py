#this module has a keys role in making the translation/convertion
#once it converts each tree numbers

#dictionaries to make the translation
# numbers 1-19
numbers_dict = {
    '1': 'one',
    '2': 'two',
    '3': 'tree',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8':'eight',
    '9': 'nine',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thiteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

#numbers 10 - 90
numbers_ten = {
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8':'eighty',
    '9': 'ninety'
}

#We need to do this operation to make sure that the programm doesn't crash if it is given a number like 01 or 056
def remove_front_zeros(number_object):
    
    while True:
        if number_object[0] == '0':
            number_object = number_object[1:]
        else:
            break
    
    return number_object


#converts numbers with one character
def number_1(number_to_be_converted):
    return numbers_dict.get(number_to_be_converted)

#converts numbers with two characters
def number_2(number_to_be_converted):
    to_return=''    #the variable to_return is a temporary variable that will be used to store the value to return
   
    #we need to check if the number is in numbers_dict (in case it is between 11-19 (11 and 19 included))
    #if it doesn't, it means we will need to put together the words correponding
    #to the first and second character of the number
    
    try:    #the .get() method cannot be used because it is necessary to exist an error in case the number_to_be_converted is not between 11-19(11 and 19 included)
        to_return = numbers_dict[number_to_be_converted]
    except:
        to_return += numbers_ten.get(number_to_be_converted[0], '')
        to_return  += ' '
        to_return += numbers_dict.get(number_to_be_converted[1], '')

    return to_return

#converts numbers with 3 characters
def number_3(number_to_be_converted):
    to_return = ''  #the variable to_return is a temporary variable that will be used to store the value to return

    #to convert the numbers it is necessary to add the  translation of the first character plus hundred (ex: 3 -> tree hundred + rest)
    #then it is necessary to add the translation of the remaning two last numbers

    #there is an exception though: if the last two numbers are 01 - 09 (01 and 09 included), the programm will need to translate only the last character (ex: 01 -> one)

    to_return += f'{numbers_dict.get(number_to_be_converted[0],)} hundred '

    if len(remove_front_zeros(number_to_be_converted[1:])) == 1:
        to_return += f'and {number_1(number_to_be_converted[-1])}'
    else:
        to_return += f'and {number_2(number_to_be_converted[1:])}'

    return to_return

#removes the front zeros and decides witch translationis it going to make (number_1(), number_2(), number_3()), according to the lenght of the number
def convert3(number):
    try:
        number = remove_front_zeros(number)
    except:
        return 'zero'
    if len(number) == 1:
        return number_1(number)
    elif len(number) == 2:
        return number_2(number)
    elif len(number) == 3:
        return number_3(number)



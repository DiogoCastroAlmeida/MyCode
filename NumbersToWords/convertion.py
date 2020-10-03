from treeconversion import convert3


class Convert():
    #the idea here is to devide each 3 characters of the number, starting from the end (ex: 23456 -> 23, 456) and then convert each of these individual numbers

    junk_characters = [' ', ',', '.']
    powers = [ 'thousand', 'milion','bilion', 'trilion', 'quadrilion']
    separation_character = ','


    def __init__(self, user_input):
        self.user_input = user_input
        self.list = []
        self.converted_list = []

    #This function has the purposse of removing all junk characters that might interfeer with the process of translating/converting
    #sometimes the user may input some characters to faciltate the reading (spaces, commas, dots...)


    def remove_junk(self):
        for element in self.junk_characters:
            self.user_input = self.user_input.replace(element, '')


    #It is necessary to check if the user_input is indeed a number
    def is_valid(self):
        try:
            int(self.user_input)
        except:
            return False
        else:
            return True

    #It is necessary to check if the user_input has the right lengh
    def right_lengh(self):
        if len(self.user_input) <= len(self.powers)*3+3:
            return True
        else:
            return False

    #to devide the number into individual, smaller numbers, spaces will be added (ex 23767 -> 23 767) and then a list will be made with all the smaller numbers
    #each smaller number will be converted, the words in the variable powers will be added to the list and a string will be made with the final convertion!

    def add_spaces(self):
        self.user_input = self.user_input[::-1]
        self.user_input = ' '.join(self.user_input[i: i+3] for i in range(0, len(self.user_input), 3))
        self.user_input = self.user_input[::-1]


    def make_list(self):
        self.list = self.user_input.split(' ')


    def convert_list(self):
        self.converted_list = list(map(convert3, self.list))

    def add_powers(self):
        self.converted_list.reverse()
        a=1
        for x in range(0, len(self.converted_list)-1):
            self.converted_list.insert(x+a, f'{self.powers[x]}{self.separation_character}')
            a+=1
        self.converted_list.reverse()


    def create_final_string(self):
        return ' '.join(self.converted_list).capitalize()

#puts everything together
def make_convertion(number):
    to_convert = Convert(number)
    to_convert.remove_junk()
    #in case the number is not valid
    if to_convert.is_valid() and to_convert.right_lengh():
        pass
    else:
        return 'Invalid Input/Number to big'
    to_convert.add_spaces()
    to_convert.make_list()
    to_convert.convert_list()
    to_convert.add_powers()
    return to_convert.create_final_string()

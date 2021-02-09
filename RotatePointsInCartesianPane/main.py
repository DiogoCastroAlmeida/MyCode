import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)


def is_type(item, type_example):
    if type(item) == type(type_example):
        return True
    else:
        return False


class Point():

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.check_type()

    def check_type(self):
        if len(self.coordinates) != 2:
            raise TypeError(f"Only two axis, got {len(self.coordinates)}")
        for element in self.coordinates:
            if not is_type(element, 1) and not is_type(element, 3.4):
                raise TypeError("Not an integer or a float")
    
    def rotate_180(self):
        """Returns the coordinates of a rotated point by 180º"""
        return (-self.coordinates[0], -self.coordinates[1])
    
    def rotate_90_cw(self):
        """Returns the coordinates of a rotated point by 90º clock wise"""
        return (-self.coordinates[1], self.coordinates[0])

    def rotate_90_ccw(self):
        """Returns the coordinates of a rotated point by 90º counter clock wise"""
        return (self.coordinates[1], -self.coordinates[0])


# a = Point((2,3))
# print(a.rotate_90_cw())
class UI():

    def __init__(self):
        self.rotation_types = {
            1: "180",
            2: "90 clockwise",
            3: "90 counter clockwise",
        }
        
    def print_hello_message(self):
        self.hello_message = "Let's rotate some points in a castesian pane!!!"
        print(self.hello_message)

    def ask_for_axis(self, axis):
        return input(f"{Fore.GREEN}Enter {axis}: {Style.RESET_ALL}")

    def construct_coordinates(self):
        while True:
            try:
                x = self.ask_for_axis("x")
                y = self.ask_for_axis("y")
                x,y = float(x), float(y)
                # here we use a loop so that the program keeps askinf for valid input if the user doesn't give a valid number
                # it gets out of the loop if the conversion to float (line above) was indeed successfull by executing the break statement (line below)
                break
            except ValueError:
                print(f"{Fore.RED}Invalid Input")
        # print(x); print(y)
        self.point = Point((x,y))
    
    def print_rotations_menu(self):
        menu = "What type of rotation do you want to do?"
        print(menu, end="\n\n")
        index = 1
        for rotation_type in self.rotation_types.values():
            print(f"{index}: {Fore.GREEN}{rotation_type}")
            index += 1
    
    def check_if_rotation_mode_is_in_range(self):
        if self.rotation not in self.rotation_types.keys():
            print(f"{Fore.RED}Invalid Input")
            self.ask_what_rotation_to_do()
    
    def transform_self_dot_rotation_to_int(self):
        try:
            self.rotation = int(self.rotation)
        except ValueError:
            print(f"{Fore.RED}Invalid Input")
            self.ask_what_rotation_to_do()

    def ask_what_rotation_to_do(self):
        self.print_rotations_menu()
        self.rotation = input(f"{Fore.BLUE}Enter number: {Style.RESET_ALL}")
        self.transform_self_dot_rotation_to_int()
        self.check_if_rotation_mode_is_in_range()
    
    def do_rotation(self):
        if self.rotation == 1:
            print(self.point.rotate_180())
        elif self.rotation == 2:
            print(self.point.rotate_90_cw())
        else:
            print(self.point.rotate_90_ccw())
    
    def run(self):
        try:
            self.print_hello_message()
            self.construct_coordinates()
            self.ask_what_rotation_to_do()
            self.do_rotation()
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW}QUITING Thanks for using this app!")


program = UI()
program.run()
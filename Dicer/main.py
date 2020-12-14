from profiles import ManageProfiles
from dice_simulator import RollDices



class Session():
    def __init__(self, profile_name):
        self.profile_name=profile_name


    def roll(self):
        print(ManageProfiles.roll_profile(self.profile_name))
    

    def delete(self):
        ManageProfiles.del_profile(self.profile_name)
        print("Profile successfully deleted")
    
    ####Prompt Part###
    def session_prompt(self):
        self.prompt = input(f"~{self.profile_name}~>")
        self.decide_operation()
    
    def decide_operation(self):
        pass

    

class UI ():

####MANUAL####
    @staticmethod
    def manual():
        manual = f"""
Welcome to Dicer Manual!

How dicer works:
    In dicer you have modes:
        - Main mode, where you can create profile (a profile is basically a\
            dice) and view your current profiles
        - Session mode, where you can roll and delete profiles.


Commands:

1. Create a profile
    {UI.commands[0]}

2. View profiles
    {UI.commands[2]}

3. Enter session mode
    {UI.commands[3]}

"""
        print(manual)
####MANUAL####
    
    
    commands = [
        "create",
        "view",
        "session",
    ]


    @staticmethod
    def prompt():
        to_return = input(">")
        return to_return.lower().replace(" ", "")

    @staticmethod
    def decide_operation(input_from_user):
        #try:
        if input_from_user == UI.commands[0]:
            UI.ExecuteCommands.create_profile()
        elif input_from_user == UI.commands[1]:
            print(ManageProfiles.view_profiles())
        else:
            print(f"No command named '{input_from_user}' ")
        #except:
         #   print("Invalid!!!")
    


    class ExecuteCommands():


        @staticmethod
        def create_profile():
            print("Create profile...")
            ManageProfiles.make_profile(profile_name=input("Enter profile name: "),
             number_of_faces=int(input("Enter number of faces for the dice: ")),
             number_of_dices=int(input("Enter number of dices: ")))
            print("Profile created")

        @staticmethod
        def view_profiles():
            print(ManageProfiles.view_profiles())
        

        def enter_session():
            name_profile = input("Enter name of the profile:")
            ses = Session(name_profile)






def run_dicer():
    while True:
        UI.decide_operation(UI.prompt())


run_dicer()



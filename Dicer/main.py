from profiles import ManageProfiles
from dice_simulator import RollDices


class UI ():
    commands = [
    "create",
    "delete",
    "view",
    "roll",
    "dice"
    ]


    @staticmethod
    def make_menu():
        menu = f"""
Welcome to the Dicer!!!

Commands:
1. Create a profile
    {UI.commands[0]}
2. Delete a profile
    {UI.commands[1]}
3. View profiles
    {UI.commands[2]}
4. Roll a profile(dice)
    {UI.commands[3]}
5. Roll a dice(without a profile)
    {UI.commands[4]}
"""
        print(menu)


    @staticmethod
    def get_input():
        to_return = input(": ")
        return to_return.lower().replace(" ", "")

    @staticmethod
    def decide_operation(input_from_user):
        #try:
        if input_from_user == UI.commands[0]:
            UI.ExecuteCommands.create_profile()
        elif input_from_user == UI.commands[1]:
            UI.ExecuteCommands.delete_profile()
        elif input_from_user == UI.commands[2]:
            print(ManageProfiles.view_profiles())
        elif input_from_user == UI.commands[3]:
            UI.ExecuteCommands.roll_profile()
        elif input_from_user == UI.commands[4]:
            UI.ExecuteCommands.roll_dice()
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
        def delete_profile():
            ManageProfiles.del_profile(input("Enter profile name: "))
            print("Profile deleted")


        @staticmethod
        def roll_profile():
            print(ManageProfiles.roll_profile(input("Enter profile name: ")))


        @staticmethod
        def roll_dice():
            print(RollDices.roll_dices(number_of_faces=int(input("Enter number of faces for the dice: ")),
             number_of_dices=int(input("Enter number of dices: "))))





def run_dicer():
    UI.make_menu()
    while True:
        UI.decide_operation(UI.get_input())


run_dicer()

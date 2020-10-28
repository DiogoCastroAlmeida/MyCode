import random

def roll_dice(number_of_faces):
    try:
        return random.randint(1, number_of_faces)
    except:
        return 0


class RollDices():
    @staticmethod
    def show_total(rolled_dice_list):
        return f"{rolled_dice_list} -> {sum(rolled_dice_list)}"


    @staticmethod
    def roll_dices(number_of_faces, number_of_dices):
        rolled_dice_list = [roll_dice(number_of_faces) for x in range(number_of_dices)]
        return RollDices.show_total(rolled_dice_list)

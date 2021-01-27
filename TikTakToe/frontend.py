from engine import backend
from TikTakToe.engine.utils.further_utils import utils
from prettytable import PrettyTable

class App():
    def __init__(self):
        self.default_mode = 1
        self.default_ratio = 3
        self.modes = {
            1: backend.QuickGame,
            2: backend.Game,
        }
        self.login_screen()
        self.create_board()

    def login_screen(self):
        login = \
""" 
Welcome to this tik tak toe game

    First, you will be prompted to choose if you want to play a Normal game, where you'll choose and create the players (you can have multiple players) and a Quick mode, where you will only choose the amount of players and not their names.
    
    Then a board will appear and you ill choose the coordinates you will want to play.
    Note: The first square has the coordinates (1,1) 
    
    In the board, the spaces filled will be marked with the player number. (a list of the number of each player will appear with the board)
    
When a player wins, you will be prompted and the game will stop"""
        print(login)

    def print_modes(self):
        num = 1
        for mode in self.modes.values():
            print(f"{num}: {mode.mode}")
            num += 1

    def choose_mode(self):
        self.print_modes()
        while True:
            print("Chose a mode")
            mode = input(f"(Default: {self.defaul_mode}): ")
            if mode == "":
                return self.defaul_mode
            elif mode not in self.modes.keys():
                print("[ERROR] Not a mode")
            else:
                return int(mode)

    def choose_board_ratio(self):
        while True:
            raw_ratio = input("Choose board ratio (only odd numbers are available)(default: 3)")
            if raw_ratio == "":
                return self.defaul_ratio
            else:
                ratio = int(raw_ratio)
                if utils.is_odd(ratio) and ratio != 1:
                    return ratio
                else:
                    print("Not an odd number.")

    def create_board(self):
        mode_number = self.choose_mode()
        ratio = self.choose_board_ratio()
        self.game = self.modes[mode_number](ratio, ratio)
        # Note: The default behaviour is to make a board with the same height and width

    def print_board(self):
        table = PrettyTable()
        table.add_row()

    def decide_simbol(self):
        pass


app = App()

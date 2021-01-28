import backend
import utils
from table import print_table
import random

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
        self.create_players()
        self.print_board()
        self.play()

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
            print(f"{num}: {mode.mode_name}")
            num += 1

    def choose_mode(self):
        self.print_modes()
        while True:
            print("Chose a mode")
            mode = input(f"(Default: {self.default_mode}): ")
            if mode == "":
                return self.default_mode
            elif int(mode) not in self.modes.keys():
                print("[ERROR] Not a mode")
            else:
                try:
                    return int(mode)
                except:
                    print("Invalid!")

    def choose_board_ratio(self):
        while True:
            raw_ratio = input("Choose board ratio (only odd numbers are available)(default: 3)")
            if raw_ratio == "":
                return self.default_ratio
            else:
                ratio = int(raw_ratio)
                if utils.is_odd(ratio) and ratio != 1:
                    return ratio
                else:
                    print("Not an odd number.")

    def create_board(self):
        mode_number = self.choose_mode()
        self.mode = self.modes[mode_number]
        # the self.mode attribute is for latter use
        #self.mode = self.modes[mode_number]
        self.ratio = self.choose_board_ratio()
        self.game = self.mode(self.ratio, self.ratio)

    
    def get_number_of_players(self):
        self.max_number_of_players = self.ratio
        while True:
            self.number_of_players = int(input("Number of players: "))
            if self.number_of_players <= self.max_number_of_players:
                break
            elif self.number_of_players > self.max_number_of_players:
                print("[ERROR] Too many players.")
                print("")
    
    def create_players_quick_mode(self):
        print("You have choosen quick mode")
        print("Choose number of players.")
        self.get_number_of_players()
        self.game.gen_players(self.number_of_players)

    def create_players_normal_mode(self):
        print("You have chosen normal mode")
        print("Choose number of players.")
        self.get_number_of_players()
        print(f"You have choosen to create {self.number_of_players} players")
        for player in range(self.number_of_players):
            player_number = player+1
            print(f"Create Player number {player_number}")
            player_name = input("Name: ")
            self.game.create_player(player_name)

    def print_players(self):
        for player in self.game.players:
            print(player)

    
    def create_players(self):
        if self.game.mode_name == self.modes[1].mode_name:
            self.create_players_quick_mode()
        elif self.game.mode_name == self.modes[2].mode_name:
            self.create_players_normal_mode()
        print("Players")
        self.print_players()

    def get_simbols(self):
        self.symbols = []
        for row in self.game.board:
            to_append = []
            for space in row:
                to_append.append(space.owner.id)
            self.symbols.append(to_append)

    def print_board(self):
        self.get_simbols()
        print_table(self.symbols)
    
    def sort_players_randomly(self):
        self.game.shuffle_players()
        print("Choosing playing order...")

    @staticmethod
    def clean_coordinates(to_clean):
        def int_a_list(object_):
            inted_list = []
            for element in object_:
                inted_list.append(int(element))
            return inted_list
        coordinates = to_clean.replace(" ", "")
        coordinates = to_clean.split(",")
        coordinates = int_a_list(coordinates)
        return coordinates[0], coordinates[1]
    
    def play(self):
        print(self.game.players[0])
        self.is_game_finished = False
        while not self.is_game_finished:
            for player in self.game.players:
                print(f"It is {player.name} time:")
                print("Example: '1,2'")
                coordinates = input("Enter the coordinates you want to play in:")
                coordinates = App.clean_coordinates(coordinates)
                self.game.fill_space(coordinates, player.id)
                #self.game.check_winner()
                self.print_board()
                is_game_won = self.game.check_winner()
                if is_game_won[0]:
                    print("End of the game!!!")
                    print(f"{is_game_won[1].name} won the game")
                    break
            self.is_game_finished == True
                


app = App()

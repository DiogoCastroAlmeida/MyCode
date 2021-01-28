import backend
import utils
from table import print_table
import random
import os
import colorama
from colorama import Fore, Style
import sys

colorama.init(autoreset=True)

class App():
    def __init__(self):
        self.default_mode = 1
        self.default_ratio = 3
        self.modes = {
            1: backend.QuickGame,
            2: backend.Game,
        }
        self.ERROR = f"{Fore.RED}[ERROR]{Style.RESET_ALL}"
        self.login_screen()
        self.create_board()
        self.create_players()
        self.print_board()
        self.play()

    def login_screen(self):
        login = \
f""" 
Welcome to this tik tak toe game

    {Fore.GREEN}First, you will be prompted to choose if you want to play a Normal game, where you'll choose and create the players (you can have multiple players) and a Quick mode, where you will only choose the amount of players and not their names.
    
    Then a board will appear and you ill choose the coordinates you will want to play.
    Note: The first square has the coordinates (1,1) 
    
    In the board, the spaces filled will be marked with the player number. (a list of the number of each player will appear with the board)
    
When a player wins, you will be prompted and the game will stop"""
        print(login)

    def print_modes(self):
        num = 1
        for mode in self.modes.values():
            print(f"{Fore.GREEN}{num}{Style.RESET_ALL}: {mode.mode_name}")
            num += 1

    def choose_mode(self):
        self.print_modes()
        error_message = f"{self.ERROR} Not a mode"
        while True:
            print("Chose a mode")
            mode = input(f"(Default: {self.default_mode}): ")
            if mode == "":
                return self.default_mode
            elif not utils.is_int(mode):
                print(error_message)
            elif int(mode) not in self.modes.keys():
                print(error_message)
            else:
                try:
                    return int(mode)
                except:
                    print(error_message)

    def choose_board_ratio(self):
        error_message = f"{self.ERROR} Not an odd number."
        while True:
            raw_ratio = input("Choose board ratio (only odd numbers are available)(default: 3)")
            if raw_ratio == "":
                return self.default_ratio
            elif not utils.is_int(raw_ratio):
                print(f"{self.ERROR} Not a number.")
            else:
                ratio = int(raw_ratio)
                if utils.is_odd(ratio) and ratio != 1:
                    return ratio
                else:
                    print(error_message)

    def create_board(self):
        mode_number = self.choose_mode()
        self.mode = self.modes[mode_number]
        self.ratio = self.choose_board_ratio()
        self.game = self.mode(self.ratio, self.ratio)

    
    def get_number_of_players(self):
        self.max_number_of_players = self.ratio
        while True:
            self.number_of_players = input("Number of players(Default: 2): ")
            if self.number_of_players == "":
                self.number_of_players = 2
                break
            else:
                self.number_of_players = int(self.number_of_players)
                if self.number_of_players > self.max_number_of_players:
                    print(f"{self.ERROR} Too many players.")
                elif self.number_of_players < 2:
                    print(f"{self.ERROR} Can't have less than 2 players. Two is minimum.")
                else:
                    break
    
    def create_players_quick_mode(self):
        print("You have choosen quick mode")
        print("Choose number of players.")
        self.get_number_of_players()
        print(self.number_of_players)
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
            print(f"{Fore.YELLOW}{player}")

    
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
        coordinates = to_clean.replace(" ", "")
        coordinates = coordinates.split(",")
        coordinates = utils.int_a_list(coordinates)
        coordinates = utils.subtract_one_to_all_elements_in_a_list(coordinates)
        return coordinates

    def check_if_game_is_won(self):
        is_game_won = self.game.check_winner()
        if is_game_won[0]:
            print(f"{Fore.GREEN}{is_game_won[1].name} won the game")
            self.print_board()
            print(f"{Fore.RED}END OF GAME")
            sys.exit()

    def player_moves(self):
        for player in self.game.players:
            print(f"It is {Fore.GREEN}{player.name} turn!")
            while True:
                coordinates = input(f"{Fore.BLUE}Enter the coordinates you want to play in (Row, Column): {Style.RESET_ALL}")
                try:
                    coordinates = App.clean_coordinates(coordinates)
                    self.game.fill_space(coordinates, player.id)
                except ValueError:
                    print(f"{self.ERROR} Wrong input.")
                except  IndexError:
                    print(f"{self.ERROR} Wrong input.")                    
                else:
                    break
            self.check_if_game_is_won()
            self.print_board()

    def play(self):
        self.sort_players_randomly()
        while True:
           self.player_moves()
                


app = App()

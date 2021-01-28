import base, ai
import random


class Game():
    mode_name = "normal"

    def __init__(self, rows, collumns):
        self.players = []
        self.board = base.gen_board(rows, collumns)
        # note: the board is just a list with Space objects
        self.fill_spaces_with_rubbish()

    def create_player(self, player_name):
        self.players.append(base.Player(player_name))

    def del_player(self, player_id):
        for player in self.players:
            if player.id == player_id:
                self.players.remove(player)
                break
            else:
                continue
        else:
            raise Exception("No player with that id.")

    # Note: to list players, just print the self.players attribute

    def fill_spaces_with_rubbish(self):
        # to not cause error, we will need to fill every space with a None user with
        # user id equal to 0
        num_player = base.Player("None")
        num_player.id = 0
        for row in self.board:
            for space in row:
                space.fill(num_player)

    def fill_space(self, coordinates, player_id):
        # coordinates must be a tuple with the proper coordinates
        # starts counting on 0, just like python indexing
        for player in self.players:
            if player.id == player_id:
                self.board[coordinates[0]][coordinates[1]].fill(player)
            else:
                continue
    
    def shuffle_players(self):
        random.shuffle(self.players)


    def check_winner(self):
        checker = ai.CheckWinner(self.board)
        result = checker.parse()
        return result



class QuickGame(Game):
    mode_name = "quick"

    def __init__(self, rows, collumns):
        Game.__init__(self, rows, collumns)

    def gen_players(self, number_of_players):
        for player_number in range(number_of_players):
            self.players.append(base.Player(f"Player {player_number+1}"))


# game = Game(3,3)
#print(game.board)
#print(game.players)
#game.create_player("Diogo")
#game.fill_space((0,0), 1)
#print(game.board[0][0].owner)

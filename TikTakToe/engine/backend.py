from TikTakToe.engine.utils import base, ai


class Game():
    mode = "normal"

    def __init__(self, rows, collumns):
        self.players = []
        self.board = base.gen_board(rows, collumns)
        # note: the board is just a list with Space objects

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

    def fill_space(self, coordinates, player_id):
        # coordinates must be a tuple with the proper coordinates
        # starts counting on 0, just like python indexing
        for player in self.players:
            if player.id == player_id:
                self.board[coordinates[0]][coordinates[1]].fill(player)
            else:
                continue


    def check_winner(self):
        checker = ai.CheckWinner(self.board)
        result = checker.parse()

    def play(self):
        pass


class QuickGame(Game):
    mode = "quick"

    def __init__(self, rows, collumns):
        Game.__init__(rows, collumns)

    def gen_players(self, number_of_players):
        for player_number in number_of_players:
            self.players.append(f"Player {player_number + 1}")


# game = Game(3,3)
#print(game.board)
#print(game.players)
#game.create_player("Diogo")
#game.fill_space((0,0), 1)
#print(game.board[0][0].owner)

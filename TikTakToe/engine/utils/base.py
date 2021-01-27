# This is the module where the building bolcks are. There is a player and Board class that will be used to make the game 

import random


class Player():

    next_id = 0
    
    @classmethod
    def gen_player_id(cls):
        cls.next_id +=1     # this way there will be no igual players id
        return cls.next_id

    def __init__(self, name):
        self.name = name
        self.id = self.gen_player_id()

    def __str__(self):
        to_return = {
            "name": self.name,
            "id": self.id,
        }
        return str(to_return)

# person = Player("Diogo")
# print(person)


class Space():

    def __init__ (self, filled=False, owner=None):
        self.filled = filled
        self.owner = owner

    def __str__(self):
        to_return = {
            "filled": self.filled,
            "owner": self.owner,
        }
        return str(to_return)

    def fill(self, player):
        if self.filled:
            raise Exception("Space is already filled.")
        else:
            self.filled = True
            self.owner = player




def gen_board( rows, collumns):
    board = []
    for y in range(collumns) :
        board.append( [Space() for x in range(rows)])
    return board


#board = gen_board(6,3)
#print(board)
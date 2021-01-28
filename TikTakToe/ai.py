import utils


class CheckWinner():
    # how this is going to be done: we will make a list of the Space() objects inside the self.board atribute that we need to compare and check if they have the same owner.
    # If they do have the same owner, then it is returned a True boolean value

    def __init__(self, board):
        self.board = board
    
    # this method expects a single list to parse.
    @staticmethod
    def all_have_same_owner(to_parse):
        player_ids = []
        for item in to_parse:
            player_ids.append(item.owner.id)
        # now to check if the players id are all the same
        # print(player_ids)
        for times in range(len(player_ids)-1):
            if player_ids[times] == player_ids[times+1]:
                continue
            else:
                return False
        return True, to_parse[-1].owner

    def get_collumns(self):
        self.collumns = []
        for y in range(len(self.board[1])):
            axis = []
            for x in range(len(self.board[0])):
                axis.append(self.board[x][y])
            self.collumns.append(axis)
    
    def get_rows(self):
        self.rows = self.board #this is just to not confund the variables
    
    def get_diagonals(self):
        board_len = len(self.board)
        self.diagonals = []
        for time in range(2): # there are only 2 diagonals
            diagonal = []
            if time == 0: 
                for position in range(board_len):
                    diagonal.append(self.board[position][position])
                self.diagonals.append(diagonal)
            if time == 1:
                reversed_board = utils.reverse_list(self.board) 
                for position in range(board_len):
                    diagonal.append(reversed_board[position][position])
                self.diagonals.append(diagonal)
    
    def merge_lists(self):
        self.merged = []
        list_to_merge = [self.diagonals, self.rows, self.collumns] 
        for liste in list_to_merge:
            for item in liste:
                self.merged.append(item)

    def parse(self):
        self.get_collumns()
        self.get_rows()
        self.get_diagonals()
        self.merge_lists()
        for item in self.merged:
            try:
                result = self.all_have_same_owner(item)
                if result[0]:
                    return True, result[-1]
            except:
                pass
        return False


        



#liste = [
#    [1,2],
#    [2, 3],
#    [3,4 ]
#]
#check = CheckWinner(liste)
#print(check.get_collumns())
#check.get_diagonals()
#print(check.collumns)
#print(check.diagonals)


import building_blocks as bb
import ai


player1 = bb.Player("Diogo")
player2 = bb.Player("Anfrade")
player3 = bb.Player("vfbsabv")


board = bb.gen_board(3,3)

board[0][0].fill(player2)
board[0][1].fill(player2)
board[0][2].fill(player2)

board[1][0].fill(player1)
board[1][1].fill(player1)
board[1][2].fill(player1)


#print(
#    c.diagonals,
#    c.collumns,
#    c.rows
#)

a = ai.CheckWinner(board)
print(a.parse())
print(a.merged)

print()
#print(a)



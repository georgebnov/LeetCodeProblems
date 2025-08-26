'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

ex.:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
'''
moves1 = [[0,0],[2,0],[1,1],[2,1],[2,2]] #row, column
moves = [[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]] #Failed this one on submission as I forgot breaks in the winningCondition i loop

def tictactoe(moves): #My Solution (0ms | Beats = 100%, 12.33MB | Beats 81.82%)
    board = [[9,9,9],[9,9,9],[9,9,9]]
    for i in range(len(moves)):
        if i % 2 == 0: #A moves
            board[moves[i][0]][moves[i][1]] = "A"
            print(board)
        else: #B moves
            board[moves[i][0]][moves[i][1]] = "B"
            print(board)

    return winningCondition(board)

def winningCondition(board):
    i = 0
    k = 0
    condition = "Draw"

    #check for opened Spots:
    while k < 3:
        if 9 in board[k]:
            condition = "Pending"
            break
        else:
            k += 1
    
    #check Straights
    while i < 3:
        if board[i][0] == board[i][1] == board[i][2] != 9:
            condition = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i] != 9:
            condition = board[0][i]
            break
        else:
            i += 1

    #Check Diagonals
    if board[0][0] == board[1][1] == board[2][2] != 9:
        condition = str(board[0][0])
    if board[0][2] == board[1][1] == board[2][0] != 9:
        condition = board[0][2]

    return condition

print(tictactoe(moves))


'''
What did I learn:
I didn't learn anythign new, I'm just dissapointed in how big the code is. It seems to be not optimal... I think there is a way to make it better, just don't how.
'''
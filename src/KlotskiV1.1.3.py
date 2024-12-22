# Hua rong dao (or Klotski) engine
from random import randint
from collections import deque
import time as tm

# dimensions
ROWS = 4
COLS = 3

# empty board to make custom postions
# create your own starting position with this template

# 1 -> vertical rectangle
# 2 -> general
# 4 -> 1 x 1 square
# 5 -> horizontal rectangle

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# some other starting positions
board = [ [4, 0, 5, 0],[0, 1, 2, 0],[0, 0, 0, 0],[5, 1, 5, 0],[5, 0, 4, 0] ]
board = [ [1, 1, 0, 0],[0, 0, 5, 0],[4, 2, 0, 4],[4, 0, 0, 4],[5, 0, 5, 0] ]
board = [ [2, 0, 1, 0],[0, 0, 0, 4],[5, 0, 5, 0],[4, 0, 1, 0],[5, 0, 0, 0] ]
board = [ [1, 4, 4, 4],[0, 1, 2, 0],[1, 0, 0, 0],[0, 5, 0, 4],[0, 0, 5, 0] ]
board = [ [4, 2, 0, 4],[1, 0, 0, 1],[0, 1, 0, 0],[4, 0, 0, 4],[5, 0, 5, 0] ]
board = [ [0, 2, 0, 0],[1, 0, 0, 1],[0, 4, 4, 0],[4, 5, 0, 4],[5, 0, 5, 0] ]
board = [ [4, 2, 0, 4],[4, 0, 0, 4],[1, 4, 4, 1],[0, 4, 4, 0],[4, 0, 0, 4] ]
board = [ [0, 2, 0, 0],[0, 0, 0, 0],[5, 0, 5, 0],[4, 5, 0, 4],[5, 0, 5, 0] ]
board = [ [2, 0, 1, 0],[0, 0, 0, 0],[4, 1, 5, 0],[1, 0, 4, 1],[0, 4, 4, 0] ]

board = [
    [4, 2, 0, 4],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [4, 0, 0, 4],
    [5, 0, 5, 0]
]
# supposedly the longest theoretical position
# ( has the longest sequence of moves )

# default position
board = [ [1, 2, 0, 1],[0, 0, 0, 0],[1, 5, 0, 1],[0, 4, 4, 0],[4, 0, 0, 4] ]

# unicode characters
pieces = [
    [
        "┌–┐",
        "| |",
        "| |",
        "└–┘",
    ],
    [
        "┌––––┐",
        "|    |",
        "|    |",
        "└––––┘",
    ],
    [
        "┌–┐",
        "└–┘",
    ],
    [
        "┌––––┐",
        "└––––┘"
    ],
    [
        "   ",
        "   "
    ]
]

# change indicies on the board to piece type
indicies = { 0 : 4, 1 : 0,1 : 0,2 : 1,3 : 0,4 : 2,5 : 3,6 : 0,7 : 0,8 : 2,9 : 2,10 : 2 }

# hashing the board, since lists are unhashable in python
# unless they contain constants
def hash(board: list) -> tuple:
    return tuple(tuple(row) for row in board)

# reverse the hashing, turn from a tuple back to a list
def unhash(board : tuple) -> list:
    return [list(map(int, row)) for row in board]

# deepcopy the board
def deepcopy(board : list) -> list:
    return [i.copy() for i in board]

# print the game board
def printGB(board : list) -> None:
    # seperate the board
    print()
    # create the board of characters
    # that will be filled out
    newBoard = [[" "] * 12 for _ in range(10)]
    # for each row and column
    for rows in range(ROWS+1):
        for cols in range(COLS+1):
            # of there is an object at the index
            if board[rows][cols]>0:
                # for each character in the ascii representation
                for row, item in enumerate(pieces[indicies[board[rows][cols]]]):
                    for col, character in enumerate(item):
                        # assign the character to the new board
                        newBoard[rows*2+row][cols*3+col] = character
    # join the list into a string and print it
    for i in newBoard: print("".join(i))
    # add a new line for padding
    print()

# generate all the legal moves
def legal_moves(position: list) -> list:
    # draw the 'shadow' of the pieces
    position = drawShadow(position)
    # create a new empty list to store legal moves
    legalMoves = []
    # for each row in the board
    for row, i in enumerate(position):
        # for each column in the row
        for col, j in enumerate(i):
            # if the item is a piece and isn't negative
            if j > -1:
                pieceType = indicies[j]
                if pieceType == 0:
                    # if the piece is a vertical rectangle
                    # check the squares to determine if the move is legal
                    if col != COLS:
                        if (position[row+1][col+1] == 0 and position[row][col+1] == 0): legalMoves.append([(row, col), (row, col+1)]) # if the right spot is free
                    if col != 0:
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) # if the left spot is free
                    if row != ROWS-1:
                        if (position[row+2][col] == 0): legalMoves.append([(row, col), (row+1, col)]) # if the cell below is free
                    if row != 0:
                        if (position[row-1][col] == 0): legalMoves.append([(row, col), (row-1, col)]) # if the cell above is free
                elif pieceType == 1:
                    # if the piece is the general
                    if col != COLS-1:
                        if (position[row+1][col+2] == 0 and position[row][col+2] == 0): legalMoves.append([(row, col), (row, col+1)]) # if the right spot is free
                    if col != 0:
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) # if the left spot is free
                    if row != ROWS-1:
                        if (position[row+2][col] == 0 and position[row+2][col+1] == 0): legalMoves.append([(row, col), (row+1, col)]) # if the cell below is free
                    if row != 0:
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0): legalMoves.append([(row, col), (row-1, col)]) # if the cell above is free
                elif pieceType == 2:
                    # single 1 x 1 square
                    if (col != COLS):
                        if (position[row][col+1] == 0): legalMoves.append([(row, col), (row, col+1)]) # if the spot right is free
                    if (col != 0):
                        if (position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) # if the spot left is free
                    if (row != ROWS):
                        if (position[row+1][col] == 0): legalMoves.append([(row, col), (row+1, col)]) # if the spot below is free
                    if (row != 0):
                        if (position[row-1][col] == 0): legalMoves.append([(row, col), (row-1, col)]) # if the spot above is free
                elif pieceType == 3:
                    # if the piece is the horizontal rectangle
                    if col != COLS-1:
                        if (position[row][col+2] == 0): legalMoves.append([(row, col), (row, col+1)]) # if the spot right is free
                    if col != 0:
                        if (position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) # if the spot left is free
                    if row != ROWS:
                        if (position[row+1][col] == 0 and position[row+1][col+1] == 0): legalMoves.append([(row, col), (row+1, col)]) # if the cell below is free
                    if row != 0:
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0): legalMoves.append([(row, col), (row-1, col)]) # if the cell above is free
    # return the list of legal moves
    return legalMoves

# play the move on the board
def playMove(board: list, move: list) -> list:
    # assign the new position the piece from the old position
    board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
    # assign the old position to empty (zero)
    board[move[0][0]][move[0][1]] = 0
    # redraw all the shadows
    board = drawShadow(board)
    # return the new board
    return board

# draw the 'shadow' for the pieces on the board
def drawShadow(board: list):
    # TODO can optimize this in the future, remove shadows entirely
    # and handle all the pieces in the legal_moves function

    # copy the board
    for i in range(len(board)):
        # set all the old shadows ( the negative values ) to zero
        board[i] = list(map(lambda x: x if x > 0 else 0, board[i]))

    # for each row and column etc etc.
    for row, i in enumerate(board):
        for col, j in enumerate(i):
            # if the item is a piece
            if j > 0:
                # draw the correct shadow
                pt = indicies[j]
                # the shadow is the negative value of the piece number
                negative = -board[row][col]
                # there are only three pieces with a shadow,
                # the vertical rectangle, the general, and the horizontal rectangle

                # if the piece is a horizontal rectangle
                if pt == 0:
                    board[row+1][col] = negative
                # if the piece is the general
                if pt == 1:
                    board[row+1][col] = negative
                    board[row][col+1] = negative
                    board[row+1][col+1] = negative
                # if the piece is a vertical rectangle
                if pt == 3:
                    board[row][col+1] = negative
    # return the board
    return board

# check if the game is won
# by checking if the general
# is at the end
def isWon(b: list) -> bool:
    return b[3][1] == 2

# BFS algorithm searches through all possbile moves
def BFS() -> list | None:
    # create a deque to store the moves
    # from collections, allows for faster (O(1))
    # appends and pops from the front
    deck = deque([[(board, 0, [(0, 0), (0, 0)])]])
    # create a new set to ensure we dont get stuck in a loop
    # we only search moves that leads us to a position we haven't seen before
    visited = set()
    # add the current board to the set
    visited.add(hash(board))

    # while there are still legal moves to make
    while deck:
        currentMoveList = deck.popleft()
        # unhash the board
        current_board = unhash(currentMoveList[-1][0])
        # get the depth aka the number of moves it took to reach this position
        depth = currentMoveList[-1][1]

        # if we win, then we return the list of moves
        if isWon(current_board):
            return currentMoveList

        # otherwise we check all the legal moves for this position
        for move in legal_moves(current_board):
            # play the move
            new_board = playMove(deepcopy(current_board), move)
            # generate a hash for the board -> list
            board_hash = hash(new_board)
            if not visited.__contains__(board_hash):
                # add the position to the set, to mark as visited
                visited.add(board_hash)
                # add the legal move to the deque
                deck.append(currentMoveList + [(board_hash, depth + 1, move)])
    # we've exhausted all the legal moves and haven't found a solution
    # return -1 to indicate there is no answer to the position
    return -1

# function that prints the solution
def findSolution() -> None:
    global board
    board = drawShadow(board)
    print("\n\nINITIAL POSITION")
    # print the board
    printGB(board)

    # take note of the start time
    t1 = tm.perf_counter()
    # call the BFS function
    this = BFS()
    # if there is no solution
    if this == -1:
        # print no solution and return
        print("No solution found"); return
    # otherwise we get the number of moves,
    # same as the depth we found the solution
    depth = this[-1][1]
    # print it out to console
    print("Shortest path length:", depth)
    # print the time taken in milliseconds
    print(f"Time Taken: {(tm.perf_counter() - t1)*1000:0.2f} ms")

    for i in this:
        input("Press Enter for next move:\n")
        # pritn the game board
        printGB(i[0])
        # print the move
        print(f"Move: {i[2]}")
        # wait for user input

    # play the game yourself
    def play():
        global moves, board
        board = drawShadow(board)
        printGB(board)
        while not isWon(board):
            moves += 1
            print("Move number:", moves)
            print("Legal moves:")
            lmoves = legal_moves(board)
            for i in lmoves:
                print(i)
            print("Enter the move you want to make:")
            move = lmoves[int(input()) - 1]
            board = playMove(board, move)
            printGB(board)
        print("You won in", moves, "moves")

def generateRandomPosition(board):
    brd = board.copy()
    RANDOMNESS = 100000
    for _ in range(RANDOMNESS):
        lm = legal_moves(brd)
        brd = playMove(brd, lm[randint(0, len(lm)-1)])
    return brd

# main function
if __name__ == "__main__":
    # board = generateRandomPosition(board)
    findSolution()
    # play()

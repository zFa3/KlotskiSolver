# Hua rong dao (or Klotski) engine
from random import randint
from collections import deque
import time as tm

# dimensions
ROWS = 4
COLS = 3

# empty board to make custom postions
# create your own starting position with this template

# (0) 0 -> empty cell
# (1) 1 -> vertical rectangle
# (2) 2 -> general
# (3) 3 -> 1 x 1 square
# (4) 4 -> horizontal rectangle

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# some other starting positions
board = [ [0, 3, 4, 0],[0, 1, 2, 0],[0, 0, 0, 0],[4, 1, 4, 0],[4, 0, 3, 0] ]
board = [ [1, 1, 0, 0],[0, 0, 4, 0],[3, 2, 0, 3],[3, 0, 0, 3],[4, 0, 4, 0] ]
board = [ [2, 0, 1, 0],[0, 0, 0, 3],[4, 0, 4, 0],[3, 0, 1, 0],[4, 0, 0, 0] ]
board = [ [3, 2, 0, 3],[1, 0, 0, 1],[0, 1, 0, 0],[3, 0, 0, 3],[4, 0, 4, 0] ]
board = [ [0, 2, 0, 0],[1, 0, 0, 1],[0, 3, 3, 0],[3, 4, 0, 3],[4, 0, 4, 0] ]
board = [ [3, 2, 0, 3],[3, 0, 0, 3],[1, 3, 3, 1],[0, 3, 3, 0],[3, 0, 0, 3] ]
board = [ [0, 2, 0, 0],[0, 0, 0, 0],[4, 0, 4, 0],[3, 4, 0, 3],[4, 0, 4, 0] ]
board = [ [2, 0, 1, 0],[0, 0, 0, 0],[3, 1, 4, 0],[1, 0, 3, 1],[0, 3, 3, 0] ]
board = [ [1, 3, 3, 3],[0, 1, 2, 0],[1, 0, 0, 0],[0, 4, 0, 3],[0, 0, 4, 0] ]

# default position
board = [ [1, 2, 0, 1],[0, 0, 0, 0],[1, 4, 0, 1],[0, 3, 3, 0],[3, 0, 0, 3] ]

# unicode characters
pieces = [
    [
        "   ",
        "   "
    ],
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
]

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
                for row, item in enumerate(pieces[board[rows][cols]]):
                    for col, character in enumerate(item):
                        # assign the character to the new board
                        newBoard[rows*2+row][cols*3+col] = character
    # join the list into a string and print it
    for i in newBoard: print("".join(i))
    # add a new line for padding
    print()

# generate all the legal moves
def legal_moves(position: list) -> list:
    # printGB2(position)
    # create a new empty list to store legal moves
    legalMoves = []
    # for each row in the board
    for row, i in enumerate(position):
        # for each column in the row
        for col, pieceType in enumerate(i):
            if pieceType > 0: # if the item is a piece and isn't negative
                if pieceType == 1:
                    # if the piece is a vertical rectangle
                    # check the squares to determine if the move is legal
                    if col != COLS: # if the right spot is free and we are not at the edge
                        if (position[row+1][col+1] == 0 and position[row][col+1] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if col != 0: # if the left spot is free and we are not at the edge
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if row != ROWS-1: # if the cell below is free and we are not at the edge
                        if (position[row+2][col] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if row != 0: # if the cell above is free and we are not at the edge
                        if (position[row-1][col] == 0): legalMoves.append([(row, col), (row-1, col)]) 
                elif pieceType == 2:
                    # if the piece is the general
                    if col != COLS-1: # if the right spot is free and we are not at the edge
                        if (position[row+1][col+2] == 0 and position[row][col+2] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if col != 0: # if the left spot is free and we are not at the edge
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if row != ROWS-1: # if the cell below is free and we are not at the edge
                        if (position[row+2][col] == 0 and position[row+2][col+1] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if row != 0: # if the cell above is free and we are not at the edge
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0): legalMoves.append([(row, col), (row-1, col)]) 
                elif pieceType == 3:
                    # single 1 x 1 square
                    if (col != COLS): # if the spot right is free and we are not at the edge
                        if (position[row][col+1] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if (col != 0): # if the spot left is free and we are not at the edge
                        if (position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if (row != ROWS): # if the spot below is free and we are not at the edge
                        if (position[row+1][col] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if (row != 0): # if the spot above is free and we are not at the edge
                        if (position[row-1][col] == 0): legalMoves.append([(row, col), (row-1, col)]) 
                elif pieceType == 4:
                    # if the piece is the horizontal rectangle
                    if col != COLS-1: # if the spot right is free and we are not at the edge
                        if (position[row][col+2] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if col != 0: # if the spot left is free and we are not at the edge
                        if (position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if row != ROWS: # if the cell below is free and we are not at the edge
                        if (position[row+1][col] == 0 and position[row+1][col+1] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if row != 0: # if the cell above is free and we are not at the edge
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0): legalMoves.append([(row, col), (row-1, col)])
    # return the list of legal moves
    return legalMoves

# play the move on the board
def playMove(board: list, move: list) -> list:
    pieceType = board[move[0][0]][move[0][1]]
    # move is represented as [ [x1, y1], [x2, y2] ]
    ydelta = (move[1][0] - move[0][0])
    xdelta = (move[1][1] - move[0][1])
    board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
    board[move[0][0]][move[0][1]] = 0
    # create the shadows here instead of calling the
    # drawShadow function
    if pieceType == 1:
        # if the piece is a vertical rectangle
        if ydelta == 1:
            board[move[0][0]][move[0][1]] = 0
            board[move[1][0]+1][move[1][1]] = -1
        elif ydelta == -1:
            board[move[0][0]+1][move[0][1]] = 0
            board[move[0][0]][move[0][1]] = -1
        elif xdelta == 1:
            board[move[1][0]+1][move[1][1]] = -1
            board[move[0][0]+1][move[0][1]] = 0
        elif xdelta == -1:
            board[move[1][0]+1][move[1][1]] = -1
            board[move[0][0]+1][move[0][1]] = 0
    elif pieceType == 2:
        if ydelta == 1:
            board[move[0][0]][move[0][1]] = 0
            board[move[0][0]][move[0][1]+1] = 0
            board[move[1][0]+1][move[1][1]] = -2
            board[move[1][0]+1][move[1][1]+1] = -2
        elif ydelta == -1:
            board[move[0][0]+1][move[0][1]] = 0
            board[move[0][0]+1][move[0][1]+1] = 0
            board[move[0][0]][move[0][1]] = -2
            board[move[0][0]][move[0][1]+1] = -2
            board[move[1][0]][move[1][1]+1] = -2
        # if the piece is the general
        elif xdelta == 1:
            board[move[0][0]][move[0][1]] = 0
            board[move[1][0]][move[1][1]+1] = -2
            board[move[0][0]+1][move[0][1]] = 0
            board[move[1][0]+1][move[1][1]+1] = -2
        elif xdelta == -1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[0][0]][move[0][1]] = -2
            board[move[0][0]+1][move[0][1]+1] = 0
            board[move[0][0]+1][move[0][1]] = -2
            board[move[1][0]+1][move[1][1]] = -2
    elif pieceType == 4:
        # if the piece is the horizontal rectangle
        if xdelta == 1:
            board[move[0][0]][move[0][1]] = 0
            board[move[1][0]][move[1][1]+1] = -4
        elif xdelta == -1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[0][0]][move[0][1]] = -4
        elif ydelta == 1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[1][0]][move[1][1]+1] = -4
        elif ydelta == -1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[1][0]][move[1][1]+1] = -4
    # return the new board
    return board

# draw the 'shadow' for the pieces on the board
def drawShadow(board: list):
    # copy the board
    for i in range(len(board)):
        # set all the old shadows ( the negative values ) to zero
        board[i] = list(map(lambda x: x if x > 0 else 0, board[i]))

    # for each row and column etc etc.
    for row, i in enumerate(board):
        for col, pt in enumerate(i):
            # if the item is a piece
            if pt > 0:
                # the shadow is the negative value of the piece number
                negative = -board[row][col]
                # there are only three pieces with a shadow,
                # the vertical rectangle, the general, and the horizontal rectangle

                # if the piece is a vertical rectangle
                if pt == 1:
                    board[row+1][col] = negative
                # if the piece is the general
                elif pt == 2:
                    board[row+1][col] = negative
                    board[row][col+1] = negative
                    board[row+1][col+1] = negative
                # if the piece is a horizontal rectangle
                elif pt == 4:
                    board[row][col+1] = negative
    # return the board
    return board

# check if the game is won
# by checking if the general
# is at the end
def isWon(b: list) -> bool:
    return b[3][1] == 2

# BFS algorithm searches through all possbile moves
def BFS() -> list | int:
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
    # prepare the board
    board = drawShadow(board)
    # print the initial position
    printGB(board)
    # while we did not win the game
    while not isWon(board):
        # increase the number of moves by one
        moves += 1
        # print the number of moves
        print("Move number:", moves)
        print("Legal moves:")
        # generate the legal moves
        lmoves = legal_moves(board)
        # print the legal moves
        for i in lmoves:
            print(i)
        # choose the move
        print("Enter the move you want to make:")
        # enter the move
        move = lmoves[int(input()) - 1]
        # play the move
        board = playMove(board, move)
        # print the new board
        printGB(board)
    # if they won, then print the number of moves
    # it took to win
    print("You won in", moves, "moves")

# generate a random position
# by making random moves
def generateRandomPosition(board):
    # copy the board
    brd = board.copy()
    # make {RANDOMNESS} random moves
    RANDOMNESS = 100000
    for _ in range(RANDOMNESS):
        lm = legal_moves(brd)
        brd = playMove(brd, lm[randint(0, len(lm)-1)])
    #return the board
    return brd

# main function
if __name__ == "__main__":
    # board = generateRandomPosition(board)
    findSolution()
    # play()
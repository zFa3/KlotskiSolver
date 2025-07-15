#!/usr/bin/env python3
# Hua rong dao (or Klotski) engine
# written in Python3 by zFa3
from random import randint
from collections import deque
import time as tm

# dimensions (zero indexed)
ROWS = 4
COLS = 3

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
    print()
    # create the board of characters
    newBoard = [[" "] * ((3 * (COLS + 1))) for _ in range(2 * (ROWS + 1))]
    for rows in range(ROWS+1):
        for cols in range(COLS+1):
            if board[rows][cols]>0:
                for row, item in enumerate(pieces[board[rows][cols]]):
                    for col, character in enumerate(item):
                        newBoard[rows*2+row][cols*3+col] = character
    for i in newBoard: print("".join(i))
    print()

# generate all the legal moves
def legal_moves(position: list) -> list:
    legalMoves = []
    for row, i in enumerate(position):
        for col, pieceType in enumerate(i):
            if pieceType > 0:
                if pieceType == 1:
                    # vertical 2x1 rectangle
                    if col != COLS:
                        if (position[row+1][col+1] == 0 and position[row][col+1] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if col != 0:
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if row != ROWS-1:
                        if (position[row+2][col] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if row != 0:
                        if (position[row-1][col] == 0): legalMoves.append([(row, col), (row-1, col)]) 
                elif pieceType == 2:
                    # 2x2 block (general)
                    if col != COLS-1:
                        if (position[row+1][col+2] == 0 and position[row][col+2] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if col != 0:
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if row != ROWS-1:
                        if (position[row+2][col] == 0 and position[row+2][col+1] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if row != 0:
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0): legalMoves.append([(row, col), (row-1, col)]) 
                elif pieceType == 3:
                    # single 1x1 square
                    if (col != COLS):
                        if (position[row][col+1] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if (col != 0):
                        if (position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if (row != ROWS):
                        if (position[row+1][col] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if (row != 0):
                        if (position[row-1][col] == 0): legalMoves.append([(row, col), (row-1, col)]) 
                elif pieceType == 4:
                    # horizontal 1x2 rectangle
                    if col != COLS-1:
                        if (position[row][col+2] == 0): legalMoves.append([(row, col), (row, col+1)]) 
                    if col != 0:
                        if (position[row][col-1] == 0): legalMoves.append([(row, col), (row, col-1)]) 
                    if row != ROWS:
                        if (position[row+1][col] == 0 and position[row+1][col+1] == 0): legalMoves.append([(row, col), (row+1, col)]) 
                    if row != 0:
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0): legalMoves.append([(row, col), (row-1, col)])
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
        # vertical 2x1 rectangle
        if ydelta == 1:
            board[move[0][0]][move[0][1]] = 0
            board[move[1][0]+1][move[1][1]] = -1
        elif ydelta == -1:
            board[move[0][0]+1][move[0][1]] = 0
            board[move[0][0]][move[0][1]] = -1
        if xdelta == 1:
            board[move[1][0]+1][move[1][1]] = -1
            board[move[0][0]+1][move[0][1]] = 0
        elif xdelta == -1:
            board[move[1][0]+1][move[1][1]] = -1
            board[move[0][0]+1][move[0][1]] = 0
    elif pieceType == 2:
        # 2x2 block (general)
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
        if xdelta == 1:
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
        # horizontal 1x2 rectangle
        if xdelta == 1:
            board[move[0][0]][move[0][1]] = 0
            board[move[1][0]][move[1][1]+1] = -4
        elif xdelta == -1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[0][0]][move[0][1]] = -4
        if ydelta == 1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[1][0]][move[1][1]+1] = -4
        elif ydelta == -1:
            board[move[0][0]][move[0][1]+1] = 0
            board[move[1][0]][move[1][1]+1] = -4
    return board

# draw the 'shadow' for the pieces on the board
def drawShadow(board: list):
    # set all the old shadows (negative values) to zero
    for i in range(len(board)):
        board[i] = list(map(lambda x: x if x > 0 else 0, board[i]))

    for row, i in enumerate(board):
        for col, pt in enumerate(i):
            if pt > 0:
                negative = -board[row][col]
                # only vertical rectangle, general, and horizontal rectangle have shadows
                if pt == 1:
                    board[row+1][col] = negative
                elif pt == 2:
                    board[row+1][col] = negative
                    board[row][col+1] = negative
                    board[row+1][col+1] = negative
                elif pt == 4:
                    board[row][col+1] = negative
    return board

# check if the game is won
# by checking if the general
# is at the bottom center
def isWon(b: list) -> bool:
    # the location (x, y) is:
    # COLS // 2, ROWS - 1 (bottom center)
    return b[ROWS - 1][COLS // 2] == 2

# BFS algorithm searches through all possible moves
def BFS() -> list | int:
    # deck stores paths as lists of (board, depth, move)
    deck = deque([[(board, 0, [(0, 0), (0, 0)])]])
    visited = set()
    visited.add(hash(board))

    while deck:
        currentMoveList = deck.popleft()
        current_board = unhash(currentMoveList[-1][0])
        depth = currentMoveList[-1][1]

        if isWon(current_board):
            return currentMoveList

        for move in legal_moves(current_board):
            new_board = playMove(deepcopy(current_board), move)
            board_hash = hash(new_board)
            if not visited.__contains__(board_hash):
                visited.add(board_hash)
                deck.append(currentMoveList + [(board_hash, depth + 1, move)])
    return -1

# function that prints the solution
def findSolution() -> None:
    global board
    board = drawShadow(board)
    print("\n\nINITIAL POSITION")
    printGB(board)

    t1 = tm.perf_counter()
    this = BFS()
    if this == -1:
        print("No solution found"); return
    depth = this[-1][1]
    print("Shortest path length:", depth)
    print(f"Time Taken: {(tm.perf_counter() - t1)*1000:0.2f} ms")

    for i in this:
        input("Press Enter for next move:\n")
        printGB(i[0])
        print(f"Move: {i[2]}")

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

# generate a random position
# by making random moves
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

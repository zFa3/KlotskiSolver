# Hua rong dao (or Klotski) engine
from collections import deque
import time as tm

# dimensions
ROWS = 4
COLS = 3

# the board
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
board = [
    [1, 2, 0, 1],
    [0, 0, 0, 0],
    [1, 5, 0, 1],
    [0, 4, 4, 0],
    [4, 0, 0, 4],
]
board = [
    [1, 4, 4, 4],
    [0, 1, 2, 0],
    [1, 0, 0, 0],
    [0, 5, 0, 4],
    [0, 0, 5, 0],
]
board = [
    [4, 2, 0, 4],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [4, 0, 0, 4],
    [5, 0, 5, 0],
]
'''
board = [
    [0, 2, 0, 0],
    [1, 0, 0, 1],
    [0, 4, 4, 0],
    [4, 5, 0, 4],
    [5, 0, 5, 0]
]
board = [
    [4, 2, 0, 4],
    [4, 0, 0, 4],
    [1, 4, 4, 1],
    [0, 4, 4, 0],
    [4, 0, 0, 4]
]
board = [
    [0, 2, 0, 0],
    [0, 0, 0, 0],
    [5, 0, 5, 0],
    [4, 5, 0, 4],
    [5, 0, 5, 0]
]
'''

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

def hash(board):
    return tuple(tuple(row) for row in board)

def unhash(board):
    return [list(map(int, row)) for row in board]

def deepcopy(board):
    return [i.copy() for i in board]

def printGB(board):
    print()
    newBoard = [[" "] * 12 for _ in range(10)]
    for rows in range(5):
        for cols in range(4):
            if board[rows][cols]>0:
                for row, item in enumerate(pieces[indicies[board[rows][cols]]]):
                    for col, character in enumerate(item):
                        newBoard[rows*2+row][cols*3+col] = character
    for i in newBoard: print("".join(i))
    print()

# generate all the legal moves
def legal_moves(position):
    position = drawShadow(position)
    legalMoves = []
    for row, i in enumerate(position):
        for col, j in enumerate(i):
            if j > -1:
                pieceType = indicies[j]
                if pieceType == 0:
                    # if the piece is a vertical rectangle
                    if col != COLS:
                        if (position[row+1][col+1] == 0 and position[row][col+1] == 0):
                            legalMoves.append([(row, col), (row, col+1)]) # if the right spot is free
                    if col != 0:
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0):
                            legalMoves.append([(row, col), (row, col-1)]) # if the left spot is free
                    if row != ROWS-1:
                        if (position[row+2][col] == 0):
                            legalMoves.append([(row, col), (row+1, col)]) # if the cell below is free
                    if row != 0:
                        if (position[row-1][col] == 0):
                            legalMoves.append([(row, col), (row-1, col)]) # if the cell above is free
                elif pieceType == 1:
                    # if the piece is the general
                    if col != COLS-1:
                        if (position[row+1][col+2] == 0 and position[row][col+2] == 0):
                            legalMoves.append([(row, col), (row, col+1)]) # if the right spot is free
                    if col != 0:
                        if (position[row+1][col-1] == 0 and position[row][col-1] == 0):
                            legalMoves.append([(row, col), (row, col-1)]) # if the left spot is free
                    if row != ROWS-1:
                        if (position[row+2][col] == 0 and position[row+2][col+1] == 0):
                            legalMoves.append([(row, col), (row+1, col)]) # if the cell below is free
                    if row != 0:
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0):
                            legalMoves.append([(row, col), (row-1, col)]) # if the cell above is free
                elif pieceType == 2:
                    # single 1 x 1 square
                    if (col != COLS):
                        if (position[row][col+1] == 0):
                            legalMoves.append([(row, col), (row, col+1)]) # if the spot right is free
                    if (col != 0):
                        if (position[row][col-1] == 0):
                            legalMoves.append([(row, col), (row, col-1)]) # if the spot left is free
                    if (row != ROWS):
                        if (position[row+1][col] == 0):
                            legalMoves.append([(row, col), (row+1, col)]) # if the spot below is free
                    if (row != 0):
                        if (position[row-1][col] == 0):
                            legalMoves.append([(row, col), (row-1, col)]) # if the spot above is free
                elif pieceType == 3:
                    # if the piece is the horizontal rectangle
                    if col != COLS-1:
                        if (position[row][col+2] == 0):
                            legalMoves.append([(row, col), (row, col+1)]) # if the spot right is free
                    if col != 0:
                        if (position[row][col-1] == 0):
                            legalMoves.append([(row, col), (row, col-1)]) # if the spot left is free
                    if row != ROWS:
                        if (position[row+1][col] == 0 and position[row+1][col+1] == 0):
                            legalMoves.append([(row, col), (row+1, col)]) # if the cell below is free
                    if row != 0:
                        if (position[row-1][col] == 0 and position[row-1][col+1] == 0):
                            legalMoves.append([(row, col), (row-1, col)]) # if the cell above is free
    return legalMoves

def playMove(br, move):
    board = br.copy()
    board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
    board[move[0][0]][move[0][1]] = 0
    board = drawShadow(board)
    return board

def drawShadow(brd: list):
    board = list(brd)
    for i in range(len(board)):
        board[i] = list(map(lambda x: x if x > 0 else 0, board[i]))

    for row, i in enumerate(board):
        for col, j in enumerate(i):
            if j > 0:
                pt = indicies[j]
                negative = -board[row][col]
                if pt == 0:
                    board[row+1][col] = negative
                if pt == 1:
                    board[row+1][col] = negative
                    board[row][col+1] = negative
                    board[row+1][col+1] = negative
                if pt == 3:
                    board[row][col+1] = negative
    return board

def isWon(b):
    return b[3][1] == 2

def BFS():
    queue = deque([[(board, 0)]])
    visited = set()
    visited.add(hash(board))

    while queue:
        currentMoveList = queue.popleft()
        current_board = unhash(currentMoveList[-1][0])
        depth = currentMoveList[-1][1]

        if isWon(current_board):
            return currentMoveList

        for move in legal_moves(current_board):
            new_board = playMove(deepcopy(current_board), move)
            board_hash = hash(new_board)
            if not visited.__contains__(board_hash):
                visited.add(board_hash)
                queue.append(currentMoveList + [(board_hash, depth + 1)])
    return -1

def findSolution():
    global board
    board = drawShadow(board)
    printGB(board)

    t1 = tm.perf_counter()
    this = BFS()
    if this == -1:
        print("No solution found")
        return
    depth = this[-1][-1]
    print("Shortest path length:", depth)
    print(f"Time Taken: {(tm.perf_counter() - t1)*1000:0.2f} ms")

    for i in this:
        printGB(i[0])
        input()

findSolution()
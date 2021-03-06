#sudoku problem
SudokuBoard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def printSudokuBoard(board):

    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("----------------------") #to draw horizantal line b/w every 3 rows

        for j in range(len(board[0])):
            if j%3 == 0 and j != 0 :
                #to draw vertical line b/w every 3 element
                print("|",end="") # end mean stay in the same line
            if j == 8:
                print(board[i][j]) #so that next row prints in next line
            else:
                print(str(board[i][j])+ " ",end="") 


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


def validation(board, num, pos):
    #checking row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num  and pos[1] != i:
            return False

    #checking column
    for i in range(len(board)):
        if board[i][pos[1]] == num  and pos[0] != i:
            return False
    
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_x * 3):
        for j in range(box_x * 3, box_y * 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(board):
    ToFind = find_empty(board)
    # print(ToFind)
    if not ToFind:
        return True
    else:
        row,col = ToFind
    
    for i in range(1,10):
        if validation(board,i,(row,col)):
            board[row][col] = i

            if solve(board): #recursion
                return True
            
            board[row][col] = 0
    return False

solve(SudokuBoard)

printSudokuBoard(SudokuBoard)
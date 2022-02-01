'''

[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

'''

def isValidSudoku(board) -> bool:
    '''
    board => 9x9
    '''
    # firstly, check each row
    for i in range(9):
        filled_row = [cell for cell in board[i] if cell!='.']
        if len(filled_row) != len(set(filled_row)):
            return False
    # then check each column
    for i in range(9):
        filled_column = []
        for j in range(9):
            if board[j][i] != '.':
                filled_column.append(board[j][i])
        if len(filled_column) != len(set(filled_column)):
            return False
    # now, check each 3x3:
    for i in range(0, 9, 3):
        rowx3 = board[i:i+3]            
        for j in range(0, 9, 3):
            square = [cell for row in rowx3 for cell in row[j:j+3] if cell!='.']
            if len(square) != len(set(square)):
                return False
    return True
'''
    Pascal triangle:
    1 
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    ...
'''

def packal_triangle(rowIndex):
    '''
    rowIndex (0 -> n)
    returns list of row at the given rowIndex
    '''
    if rowIndex == 0:
        return [1]
    lastRow = [1,1]
    size = 2
    while size <= rowIndex:
        row = [1]                                   # every row starts with 1
        for i in range(len(lastRow)-1):
            row.append(lastRow[i] + lastRow[i+1])   # every element is sum of above two elements in last row
        row.append(1)                               # every row ends with 1
        lastRow = row                               # update last row with newly generated row
        size += 1                                   # or size = len(lastRow)
    return lastRow
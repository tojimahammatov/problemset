'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Ex. input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 ==> 
Ex. output: True
'''

def searchMatrix(matrix, target: int) -> bool:
    start, end = 0, len(matrix[0])
    for row in matrix:
        if row[len(row)-1] >= target:
            while start<end:
                middle = (start+end)//2
                if target == row[middle]:
                    return True
                elif target > row[middle]:
                    start = middle+1
                else:
                    end = middle
            return False
    return False
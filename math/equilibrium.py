'''
    Problem:    Find an equilibrium index of a given list
    
    Note: an equilibrium index is an index which divides list into two halves such that those sub-lists' sums are equal.
            the element at the equilibrium index itself is not calculated.
            0 and (n-1) can also be equilibrium indexes. ( for 0: sum of sub-list on the left is 0, the same for (n-1) )
    if there is no any such index, return -1
'''

# O(n) complexity
def find_equilibrium(A):
    _sum = sum(A)
    n = len(A)
    sum_left = 0
    for i in range(n):
        sum_right = _sum - sum_left - A[i]
        if sum_left == sum_right:
            return i
        sum_left += A[i]
    return -1

print(find_equilibrium([1, -4, 5, 2, 2]))      # which prints index 3 dividing the list as => [1, -4, 5] vs [2]
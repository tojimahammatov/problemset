'''
    Problem:    Find the smallest positive integer which does not occur in the given list
'''

# O(n)~O(nlogn) complexity
def non_existing_integer(A):
    # convert list to set, since existance verification of set is almost O(1)
    nums = set(A)
    result = 1  # start from the smallest positive integer
    while result in nums:
        result+=1
    return result

# example
print(non_existing_integer([1, 2, 3, 5, 7, 0, -1]))                             # prints 4
print(non_existing_integer([x for x in range(100001)] + [100001, 100002]))      # prints 100003

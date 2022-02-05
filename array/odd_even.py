'''
    given is a list containing integer numbers,
    a task is to make evens/odds as left/right side of (new) list.
'''

def solve(nums):
    '''
    nums: list
    rtype: list[int]
    '''
    result = [x for x in nums if x%2==0]
    result += [x for x in nums if x%2==1]
    return result
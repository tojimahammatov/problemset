'''
    given is a list whose every element occurs three times except one (once).
    task is to find the element occuring once. 
'''

def missing_number(nums):
    '''
    nums: list[int]
    rtype: int
    '''
    s = set(nums)
    # math: [3*(a+b+c) - (3*a + 3*b + c)] / 2 = c
    return (3*sum(s) - sum(nums))//2
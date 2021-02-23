'''
    given a list, need to find missing number between [0, len(list)]
'''

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sums = 0
    n = len(nums)
    # seems sum(nums) is less than iterating a list and calculate summation
    for num in nums:
        sums+=num
    return n*(n+1)/2 - sums

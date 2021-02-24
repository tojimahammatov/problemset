'''
    Given is a list of integers whose elements' occurence is 2 except one,
    need to find a number whose occurence is 1
'''

def single_number_v1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for num in nums:
        d[num] = True if num in d else False
    for num in nums:
        if not d[num]:
            return num
    return -1

def single_number_v2(nums):
    # math trick
    return 2*(sum(set(nums))) - sum(nums)
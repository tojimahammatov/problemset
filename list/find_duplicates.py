'''
    Given is a list of integers, 
    need to find duplicates.
'''

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []        
    d = {}
    for num in nums:
        if num in d:
            res.append(num)
        else:
            d[num] = True
    return res
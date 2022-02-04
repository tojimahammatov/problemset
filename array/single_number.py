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


def single_number_v3(nums):
    '''
        so far the best option,
            - O(n) time complexity,
            - O(1) space complexity,
        bitwise trick
    '''
    number = 0
    for i in range(len(nums)):      # faster than:  ```for num in nums:```
        number ^= nums[i]
    return number
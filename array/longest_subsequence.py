'''
    Given is a list containing numbers and difference of arithmetic progression.
    Return the length of the longest subsequence with difference provided that some elements can be removed.
'''

def longest_subsequence(nums, difference):
    '''
    len(nums) >= 1
    '''
    candidates = {}
    max_subseq = 0
    candidates[nums[0]] = 1
    for n in nums:
        if n in candidates:
            prev = candidates[n]
            candidates[n+difference] = prev + 1
            if prev > max_subseq:
                max_subseq = prev
        else:
            candidates[n+difference] = 1
    return max_subseq
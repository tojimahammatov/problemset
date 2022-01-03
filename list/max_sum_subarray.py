'''
    given is a list containing both positive and negative integers
    a task is to find a subarray which has largest sum
'''

# There are two (reasonable) ways: Kanade's algorithm & Divide and Conquer method

# Kanade's algo

def max_sub_array(nums):
    # max_so_far = INT_MIN
    max_so_far = -1000000001    # should be the smallest value within a scenario
    max_ending_here = 0         # to control where the positive contiguous sum of subarray
    for n in nums:
        max_ending_here += n    
        if max_so_far < max_ending_here:    # if max is less than a new candidate
            max_so_far = max_ending_here    # update max value
        if max_ending_here < 0:         # if subarray sum till here is negative 
            max_ending_here = 0         # set 0 to consider further subs 
    return max_so_far       # return max value
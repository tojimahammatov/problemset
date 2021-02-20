'''
    given is a list containing numbers,
    task: to find majority element appearing more than floor(n/2), assume number always exists
'''

def majority_element(nums):
    '''
        nums: list[int]
        rtype: int
    '''
    d = {}
    max_occur = 1
    for x in nums:
        if x in d:
            d[x] = d[x] + 1
            if d[x] > max_occur:
                max_occur, majority_elem = d[x], x
        else:
            d[x] = 1
    if max_occur > 1:
        return majority_elem
    else:
        return nums[0]

# yet I found more efficient code as well:
def majority_element_v2(nums):
    count = 0
    x = None
    for num in nums:
        if count == 0:
            x = num
        if num == x:
            count+=1
        else:
            count-=1
    return x
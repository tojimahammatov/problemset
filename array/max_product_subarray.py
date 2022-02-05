'''
    given is a list of numbers
    to find such three numbers so that their product is the greatest
'''

# there are two ways and in both ways we need to find max 3 values and min 2 values;
# because max product lies among (max1*max2*max3, max1*min1*min2)

# first sort and just access those mins and maxs. Complexity is O(nlogn) due to sorting
def max_product_1(nums):
    nums.sort()
    n = len(nums) - 1   # index to the greatest value
    return max(nums[n]*nums[n-1]*nums[n-2], nums[0]*nums[1]*nums[n])

# second way is more easier, we are still interested in finding only those mins and maxs,
#           but we do it linearly with O(n) time complexity 
def max_product_2(nums):
    max1 = max2 = max3 = -1000000001
    min1 = min2 = 1000000001
    for n in nums:
        if max1 < n:
            max1, max2, max3 = n, max1, max2
        elif max2 < n:
            max2, max3 = n, max2
        elif max3 < n:
            max3 = n
        
        if min1 > n:
            min1, min2 = n, min1
        elif min2 > n:
            min2 = n
    return max(max1*max2*max3, min1*min2*max1)
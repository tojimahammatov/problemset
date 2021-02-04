# a function to remove duplicates elements in place

def removeDuplicates(nums):
    i=0
    while i<len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i+1]   # seems nums.remove(nums[i]) is slower than del nums[i]
        else:
            i+=1
    return nums
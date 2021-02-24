# verify whether the given number is a power of 3

def isPowerOfThree(n):
    # interesting fact is that the highest power of 3 (<2^31-1) should be divisible 
    #                               by all numbers which are power of 3. 
    if n<1:
        return False
    return 1162261467%n==0
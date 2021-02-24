# verify whether the given number is a power of 2

def isPowerOfTwo(n):
    # how about the following:
    #   return n>=1 and n&(n-1)==0
    if n<1:
        return False
    return n&(n-1)==0
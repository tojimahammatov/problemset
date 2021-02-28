'''
    Given is a list containing durations of songs (in seconds),
    task is to find a number of pairs whose total duration is divisible by 60.

    (LeetCode Rumours: online assessment problem at Amazon)
'''

def numPairsDivisibleBy60(time):
    """
    :type time: List[int]
    :rtype: int
    """
    d = {}
    for i in range(60):
        d[i] = 0
    for i in range(len(time)):      # we need only mods of all durations
        mod = time[i] % 60
        d[mod] = d[mod] + 1

    res = d[0]*(d[0]-1)//2          # mod 0s also create n*(n-1)/2 pairs
    for i in range(1, 30):
        res += (d[i]*d[60-i])
    res += (d[30]*(d[30]-1)//2)     # mod 30s make n*(n-1)/2 pairs
    return res

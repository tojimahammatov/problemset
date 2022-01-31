'''
    Given is a string s, find the index of the first non-repeating character.
'''

def first_unique_char(s):
    '''
    1 <= s.length <= 10**5
    '''
    n = len(s)
    memo = {}       # to store unique chars along with their indices
    duplicates = set()    # to keep track of duplicates after being removed from memo (since they might be added later wrongly again)
    for i in range(n):
        if s[i] in memo:
            duplicates.add(s[i])
        else:
            if s[i] not in duplicates:
                memo[s[i]] = i

    if len(memo.values()) == 0:
        return -1
    return min(memo.values())
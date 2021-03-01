'''
    given a string and list indices,
    task is to shuffle string such that the character at the i th position
        moves to indices[i] in the new string.
'''

def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    st = [0] * len(s)
    for i in range(len(s)):
        st[indices[i]] = s[i]
    return ''.join(st)
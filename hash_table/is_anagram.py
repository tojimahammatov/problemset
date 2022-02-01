'''
    Given two strings, s and t. Find whether t is an anagram of s.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.
'''

from collections import Counter


def is_anagram(s, t):
    '''
    1 <= s.length, t.length <= 5 * 104
    '''
    return Counter(s) == Counter(t)
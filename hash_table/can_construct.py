'''
    Given two strings (ransomNote and magazine).
    Find whether ransomNote can be constructed from magazine. 
'''

from collections import Counter


def can_construct(ransom_note, magazine):
    '''
    1 <= ransom_note.length, magazine.length <= 105
    '''
    ransom_dict = Counter(ransom_note)
    magazine_dict = Counter(magazine)
    for k, v in ransom_dict.items():
        if k not in magazine_dict:
            return False
        if v > magazine_dict[k]:
            return False
    return True

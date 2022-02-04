'''
    Find the intersection of two lists.
    Ex: [1,2,2,1] vs [2,2] => [2,2]
'''

from collections import Counter


def intersect(nums1, nums2):
    dict1 = Counter(nums1)
    dict2 = Counter(nums2)
    res = []
    for k, v in dict1.items():
        if k in dict2:
            freq = v if v <= dict2[k] else dict2[k]
            res.extend([k] * freq)
    return res
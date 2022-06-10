'''
Category : Hard (in leetcode)
'''

def findMedianSortedArrays(nums1, nums2) -> float:
    m, n = len(nums1), len(nums2)
    res = []
    p, q = 0, 0
    while p < m and q < n:
        if nums1[p] <= nums2[q]:
            res.append(nums1[p])
            p += 1
        else:
            res.append(nums2[q])
            q += 1
    if p < m:
        res += nums1[p:]
    if q < n:
        res += nums2[q:]
    if (m+n) % 2 == 1:
        return res[(m+n)//2]
    else:
        p, q = (m + n) // 2, (m + n - 1) // 2
        return (res[p] + res[q]) / 2
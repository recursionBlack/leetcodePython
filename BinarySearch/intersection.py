from typing import List

# 349. 两个数组的交集
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = list(set(nums1))
        unique_nums2 = list(set(nums2))
        unique_nums1.sort()
        unique_nums2.sort()

        if len(unique_nums1) > len(unique_nums2):
            tmp = unique_nums2[:]
            unique_nums2 = unique_nums1[:]
            unique_nums1 = tmp[:]

        ans = []

        for num in unique_nums1:
            left = 0
            right = len(unique_nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                if unique_nums2[mid] == num:
                    ans.append(num)
                    unique_nums2.remove(num)
                    break
                elif unique_nums2[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return ans

"""
这个问题，超简单的，用两个hashset取交集就完事了，但因为被算入了二分法里，所以就复杂了，时间也更慢了
"""
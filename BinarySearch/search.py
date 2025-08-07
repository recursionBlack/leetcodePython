from typing import List

# 33. 搜索旋转排序数组
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 先使用153题的查找旋转排序数组中的最小值位置
        def findMin(nums: List[int]) -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return left

        lowest = findMin(nums)
        # 用目标值与最后位置的一个值进行比较，看看target落在了哪个区间里？
        # [0, lowest] or [lowest, len(nums) - 1]
        left = 0
        right = len(nums) - 1
        if target == nums[-1]:
            return right
        elif target > nums[-1]:
            right = lowest - 1
        else:
            left = lowest

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

"""
该问题难点并不在于，本问题，而在于，如何快速找到最低点的序号
"""
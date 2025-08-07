from typing import List

# 34. 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left  = 0
        right = n - 1
        res = []
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # 找到一个就行，然后就可以根据nums是有序的，
                # 往左右各扩展到边界
                ans = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if ans == -1:
            return [-1, -1]
        # 先往左找
        left = ans
        while left > 0 and nums[left-1] == nums[left]:
            left -= 1
        res.append(left)
        right = ans
        while right < n - 1 and nums[right+1] == nums[right]:
            right += 1
        res.append(right)

        return res
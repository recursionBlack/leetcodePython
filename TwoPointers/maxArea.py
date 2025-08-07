from typing import List

# 11. 盛最多水的容器
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

"""
一次过，但该题主要是为了给43题，接雨水，这个题提供一些启发，算是开胃菜
"""
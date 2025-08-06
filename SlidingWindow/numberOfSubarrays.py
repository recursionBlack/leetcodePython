from typing import List

# 1248. 统计「优美子数组」
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ans = 0
        cnt1 = cnt2 = 0
        left1 = left2 = 0

        for right, num in enumerate(nums):
            if num % 2 == 1:
                cnt1 += 1
            while left1 <= right and cnt1 > k:
                if nums[left1] % 2 == 1:
                    cnt1 -= 1
                left1 += 1
            if num % 2 == 1:
                cnt2 += 1
            while left2 <= right and cnt2 >= k:
                if nums[left2] % 2 == 1:
                    cnt2 -= 1
                left2 += 1
            ans += left2 - left1

        return ans

"""
经典的恰好型滑动窗口模板，一次性过了
"""
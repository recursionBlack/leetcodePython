from typing import List
from collections import defaultdict

# 1004. 最大连续1的个数 III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = left = 0
        cnt = defaultdict(int)

        for right, in_ in enumerate(nums):
            cnt[in_] += 1
            while left <= right and cnt[0] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans

"""
一次过，但为啥速度那么慢啊？只超过5%？？？
看灵茶山艾府的答案，原来人家没用字典，直接用一个常量来统计0和1
的数量，难怪快很多。但我这个方法可以解决更多问题，就不改了
"""
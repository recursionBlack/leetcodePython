from typing import List
from collections import defaultdict

# 992. K 个不同整数的子数组
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        ans = 0
        left1, left2 = 0, 0
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)

        for right, in_ in enumerate(nums):
            cnt1[in_] += 1
            while left1 <= right and len(cnt1) > k:
                cnt1[nums[left1]] -= 1
                if cnt1[nums[left1]] == 0:
                    del cnt1[nums[left1]]
                left1 += 1
            cnt2[in_] += 1
            while left2 <= right and len(cnt2) >= k:
                cnt2[nums[left2]] -= 1
                if cnt2[nums[left2]] == 0:
                    del cnt2[nums[left2]]
                left2 += 1
            ans += left2 - left1

        return ans

"""
第一个做出来的困难，哈哈哈！参考的930题，恰好型滑动窗口
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,1,2,3]
    k = 2
    print("测试用例1输入nums = {}, k = {}:".format(nums, k))
    print("测试用例1输出:", solution.subarraysWithKDistinct(nums, k))
    # 预期输出: 8
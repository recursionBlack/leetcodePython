from typing import List
from collections import defaultdict

# 560. 和为 K 的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        cnt = defaultdict(int)
        ans = 0
        for i in prefix_sum:
            ans += cnt[i - k]
            cnt[i] += 1

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,1,1]
    k = 2
    print("测试用例1输入 = {}, = {}:".format(nums, k))
    print("测试用例1输出:", solution.subarraySum(nums, k))
    # 预期输出: 2

    # 测试用例1：基础案例
    nums = [1,2,3]
    k = 3
    print("测试用例1输入 = {}, = {}:".format(nums, k))
    print("测试用例1输出:", solution.subarraySum(nums, k))
    # 预期输出: 2
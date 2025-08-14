from typing import List
from collections import defaultdict

# 974. 和可被 K 整除的子数组
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0

        for i in range(n):
            total += nums[i]
            mod = total % k
            if mod in cnt:
                ans += cnt[mod]
                cnt[mod] += 1
            else:
                cnt[mod] = 1

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    nums = [4,5,0,-2,-3,1]
    k = 5
    # 测试用例1：基础案例
    print("测试用例1输入 = {}, = {}:".format(nums, k))
    print("测试用例1输出:", solution.subarraysDivByK(nums, k))
    # 预期输出:7
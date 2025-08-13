from typing import List
from collections import defaultdict

# 525. 连续数组
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 当前1的数量和0的数量的差值
        cnt = 0
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        hashmap = defaultdict(int)
        hashmap[0] = -1     # 该处的定义，是为了解决，i = n - 1的补充

        ans = 0
        for i, num in enumerate(nums):
            if num == 1:
                cnt += 1
            if num == 0:
                cnt -= 1
            # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等
            if cnt in hashmap:
                ans = max(ans, i - hashmap[cnt])
            else:
                hashmap[cnt] = i

        return ans


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [0,1]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.findMaxLength(nums))
    # 预期输出: 2

    # 测试用例1：基础案例
    nums = [0,1,1,1,1,1,0,0,0]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.findMaxLength(nums))
    # 预期输出: 6
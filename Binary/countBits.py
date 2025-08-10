from typing import List

# 338. 比特位计数
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = []
#         for i in range(n + 1):
#             cnt = 0
#             while i > 0:
#                 if i & 1:
#                     cnt += 1
#                 i >>= 1
#             ans.append(cnt)
#
#         return ans

"""
暴力位运算，但其实还有一种，动态规划的算法
因为该题比较简单，所以可以自己手写一下，练习动态规划
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

"""
可以用动态规划的基础在于：
第i个数，他的二进制数上1的个数，是他除以2的个数，加上最后一位是否是1
比如说，7 = 3 + 7&1

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # n = 2
    # print("测试用例1输入nums = {}:".format(n))
    # print("测试用例1输出:", solution.countBits(n))
    # # 预期输出: [0,1,1]

    # 测试用例1：基础案例
    n = 5
    print("测试用例1输入nums = {}:".format(n))
    print("测试用例1输出:", solution.countBits(n))
    # 预期输出: [0,1,1,2,1,2]
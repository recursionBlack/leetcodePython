from myLeetcodeUtils import bit_length

# 201. 数字范围按位与
# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         left2 = left
#         cnt = 0
#         while left2 > 0:
#             left2 >>= 1
#             cnt += 1
#
#         if right >= (1 << cnt):
#             return 0
#
#         ans = (1 << cnt) - 1
#         for i in range(left, right + 1):
#             ans &= i
#
#         return ans

"""
自己的做法，有点思路，但终究是错误的，有些太长的就通过不了了
所以，看灵神的答案如下：
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 找到从left到right中，开始不同的位长，低位的0~m-1位是不同的
        m = bit_length(left ^ right)

        # 将这些低位，全改为0， 2**m - 1就是m个11111的二进制数
        # ~就是除了这m个低位，其余高位全改为1
        # 将left与之相与，就是left与right相同的高位
        return left & ~((1 << m) - 1)

"""
灵神题解：
将left和right之间的数，都换成二进制数
可以看到，left和right在前面，是有一些相同的位的，那这些位的数，相与后，还是相同的，
但从后面开始，一些位上的数字开始发生变化了，那这些位上，有0有1，最终结果一定是0
那么，最终的结果，就是，前那些相同的位，保留，后面再接上m-1个0，就是从left到right的所有数字相与的结果
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    left = 5
    right = 7
    print("测试用例1输入left = {}, right ={}:".format(left, right))
    print("测试用例1输出:", solution.rangeBitwiseAnd(left, right))
    # 预期输出: 4
from typing import List

# 137. 只出现一次的数字 II
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        # ~(res ^ 0xffffffff)还是本身，但是在32位上截断了
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

"""
又是krahets神的解题思路:
完全是寸步难行啊！
将每个数，转为二进制数，然后，统计数组中所有数字的二进制 在 i 位上 是 1 的个数
以[7,7,7,9]为例，7的二进制数，是0111，9是1001，那么全部统计完成后，
counts在第3位上的1的个数，是1个，在第二位上的1的个数，是3个，在第1位上的1的个数，是3个
在第0位上的1的个数，是4个
然后对每一位上，取3的模，就会只剩下个1001了，再转换回整型即可
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # nums = [0,1,0,1,0,1,99]
    # print("测试用例1输入nums = {}:".format(nums))
    # print("测试用例1输出:", solution. singleNumber(nums))
    # # 预期输出: 99

    # 测试用例1：基础案例
    nums = [7,7,7,9]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution.singleNumber(nums))
    # 预期输出: 9
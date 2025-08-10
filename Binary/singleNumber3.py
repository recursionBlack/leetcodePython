from typing import List

# 260. 只出现一次的数字 III
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for num in nums:
            total ^= num

        # 最终结果，是两个只出现一次的异或，
        # 找到该值最右侧的1,两个数在这个位上，一定不相同，分别是0或1
        rightMostOne = 1
        while (total & 1) == 0:
            total >>= 1
            rightMostOne <<= 1

        # 以此，根据该位，分别将数字分为两组,这两个数，会分别落入到这两个组里
        # 对两个组分别异或，就是要找的两个唯一的数
        a, b = 0, 0
        for num in nums:
            if num & rightMostOne:
                a ^= num
            else:
                b ^= num

        return [a, b]

"""
三道找唯一数字的题，都用了位运算的特殊效果，分别是：
两个相同的数字，异或为0；
统计各个位数上的数量；
还有两个不同的数，异或的结果，最右位的1一定是两个在这个位上的不同的；
如果没有见过类似的问题，第一次遇到，让人怎么想的出来？？？这些隐藏的特性呢？？？
希望面试官给点提示吧。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,1,3,2,5]
    print("测试用例1输入nums = {}:".format(nums))
    print("测试用例1输出:", solution. singleNumber(nums))
    # 预期输出: [3,5]
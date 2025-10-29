"""
加入差值绝对值，直到数组长度固定
给定一个非负数组，计算任何两个数差值的绝对值,如果arr中没有，则将其加入到arr一次
然后对于新的arr，继续重复上述行为，直到数组长度不再增加，返回arr的最终长度

来自真实大厂笔试，没有在线测试，对数器验证
"""

"""
解题思路，必须掌握最大公约数的计算，最终结果必然包含，从最大公约数，到最大值的，中间所有最大公约数的倍数
比如其实有[5,20],那么最终结果就必然是[5, 10,15, 20]最大公约数是5，中间新增的10和15都是从5到20之间，缺失的5的倍数
"""
from typing import List
from collections import defaultdict

class Solution:
    @classmethod
    def gcd(cls, m: int, n: int) -> int:
        return m if n == 0 else cls.gcd(n, m % n)

    def absDiffArray(self, arr: List[int]) -> int:
        # 找到数组中的最大值
        maxElem = 0
        # 找到数组中任意一个非0值
        gcd = 0
        for num in arr:
            maxElem = max(maxElem, num)
            if num != 0:
                gcd = num

        # 说明数组中，全是0，直接返回数组长度即可
        if gcd == 0:
            return len(arr)

        # 用来统计数组中，各个元素出现的次数
        cnts = defaultdict(int)
        # 计算整个数组的，最大公约数
        for num in arr:
            if num != 0:
                gcd = self.gcd(gcd, num)
            cnts[num] += 1

        # 所有该出现数的总数量
        ans = maxElem // gcd
        # 用来计算0的数量的变量
        maxCnt = 0
        # 如果某些该出现的数，本来就在arr里，刚开始就在arr里，不需要后加进来
        # 且这些数的数量不小于1，则补上arr里原有的这些数，
        # 比如，如果，10，应该出现在最终的结果数组里，但初始arr里已经有3个10了，就需要在结果里，补上这两个10
        for key in cnts.keys():
            if key != 0:
                ans += cnts[key] - 1
                maxCnt = max(maxCnt, cnts[key])

        # 0比较特殊，全程不会影响公约数，如果arr里原来就有0，则最终结果将初始0的数量加上
        # 如果初始数组里没有0，但有重复的数，那重复的数互相减，会使最终数组里有一个0
        if cnts[0] > 0:
            ans += cnts[0]
        elif maxCnt > 1:
            ans += 1

        return ans


"""
该题需要掌握，辗转相除法，求解最大公约数，以及，最终结果的数组是，
从最大公约数，到最大值之间，所有最大公约数的倍数
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    arr = [3,4,7]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.absDiffArray(arr))
    # 预期输出: 7  [1,2,3,4,5,6,7]

    # # 测试用例1：基础案例
    arr = [5, 20]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.absDiffArray(arr))
    # 预期输出: 4  [5, 10, 15 ,20]
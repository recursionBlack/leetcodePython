"""
370 区间加法（会员专属题）
假设你有一个长为n的数组，初始情况下，所有数字均为0，你将会被给出k个更新的操作，
其中，每个操作会被表示为一个三元组，【startIndex, endIndex, inc】,你需要将子数组
A【startIndex, endIndex】增加inc
请你返回k次操作后的数组
"""
from typing import List
from myLeetcodeUtils import Difference

class Solution:
    def getModifyArray(self,  length: int, updates: List[List[int]]) -> int:
        nums = [0] * length
        # 构造差分解法类
        diff = Difference(nums)

        for startIndex, endIndex, val in updates:
            diff.increment(startIndex, endIndex, val)

        return diff.result()

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    length = 5
    updates = [[1,3,2],[2,4,3],[0,2,-2]]
    print("测试用例1输入 = {},  = {}:".format(length, updates))
    print("测试用例1输出:", solution.getModifyArray(length, updates))
    # 预期输出: [-2,0,3,5,3]
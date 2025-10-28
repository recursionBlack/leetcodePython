from typing import List
from functools import cmp_to_key

# 1029. 两地调度
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        sums = 0
        arr = []
        for a, b in costs:
            arr.append(b-a)
            sums += a
        arr.sort()
        m = n // 2
        for i in range(m):
            sums += arr[i]

        return sums


"""
该题需要理解，先全都去a，再从a掉一半人去b，挑其中转去一半人，挑选出这较大的一半人，
就好写了。代码本身并不难。难在，想出，为啥这么做。
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    costs = [[10,20],[30,200],[400,50],[30,20]]
    print("测试用例1输入 = {}:".format(costs))
    print("测试用例1输出:", solution.twoCitySchedCost(costs))
    # 预期输出:110
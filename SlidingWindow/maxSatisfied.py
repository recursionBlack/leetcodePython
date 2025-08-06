from typing import List

# 1052. 爱生气的书店老板
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 计算不生气时，满意的顾客总数
        sum_ = 0
        for i, x in enumerate(customers):
            if grumpy[i] == 0:
                sum_ += x

        windSat = 0
        winMax = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                windSat += customers[i]
        winMax = max(winMax, windSat)
        # 使用滑动窗口，计算原本因生气被气走的客户的最大值
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                windSat += customers[i]
            if grumpy[i-minutes] == 1:
                windSat -= customers[i-minutes]
            winMax = max(winMax, windSat)

        return winMax + sum_

"""
相比于传统的滑动窗口，该问题，增加了一些，干扰项目，用了两个列表，顾客列表和生气列表
所以滑动窗口的作用，就是让原本因生气而减少的顾客，给挽救回来，
窗口的宽度就是老板不生气的时间，定长的
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    customers = [3]
    grumpy = [1]
    minutes = 1
    print("测试用例1输入customers = {}, grumpy = {}, minutes = {}:".format(customers, grumpy, minutes))
    print("测试用例1输出:", solution.maxSatisfied(customers, grumpy, minutes))
    # 预期输出: 3
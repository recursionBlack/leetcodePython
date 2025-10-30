from typing import List

# 1665. 完成所有任务的最少初始能量
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda row: row[1] - row[0])

        ans = 0
        for cost, lest in tasks:
            ans = max(ans+cost, lest)

        return ans

"""
经典的二维数组贪心问题，通常解法是，先按第一个元素或第二个元素进行排序，再将另一个元素丢进大根堆
而该问题，期望的是，花费尽量大，至少电量尽量小的，越早排，通过倒推法，以0电量为起始，逐步根据花费和至少电量
求出最终的电量
所以，排序顺序为，花费-至少电量，且不需要用到堆
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    tasks = [[1,2],[2,4],[4,8]]
    print("测试用例1输入 = {}:".format(tasks))
    print("测试用例1输出:", solution.minimumEffort(tasks))
    # 预期输出: 8

    # # 测试用例1：基础案例
    tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
    print("测试用例1输入 = {}:".format(tasks))
    print("测试用例1输出:", solution.minimumEffort(tasks))
    # 预期输出: 27
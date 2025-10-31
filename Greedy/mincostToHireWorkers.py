from typing import List
import heapq

# 857. 雇佣 K 名工人的最低成本
class employee:
    def __init__(self, r: float, q: int):
        # 该工人，期望工资与工作质量的比例
        self.ratio = r
        # 该工人，工作质量
        self.quality = q

    # 按照期望工资与工作质量的比例来进行排序
    def __lt__(self, other):
        self.ratio < other.ratio

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        emps = []
        for i in range(n):
            emps.append(employee(wage[i]/quality[i], quality[i]))
        emps.sort(key=lambda e: e.ratio)

        # 大根堆，根据工作质量排序
        heap = []
        # 堆里，最小的前k个质量数值的累加和
        qualitySum = 0
        ans = float("inf")

        for i in range(n):
            curQual = emps[i].quality
            # 如果堆里还没有填满，不用比，直接往堆里填
            if len(heap) < k:
                heapq.heappush(heap, -curQual)
                qualitySum += curQual
                if len(heap) == k:
                    ans = min(ans, qualitySum * emps[i].ratio)
            # 如果堆里已经填满k个元素了，则与堆顶元素进行比较
            else:
                if -heap[0] > curQual:
                    qualitySum += heap[0]
                    heapq.heappop(heap)
                    heapq.heappush(heap, -curQual)
                    qualitySum += curQual
                    ans = min(ans, qualitySum * emps[i].ratio)

        return ans

"""
和题目“知识竞赛”很像，都是根据一个标准进行排序，然后按照排序后的顺序，逐一来到每个样本，
计算在该样本参与的情况下最佳答案是什么？排序之后的顺序，可以起到加速计算的效果
"""

"""
首先，根据期望工资与工作质量的比例排序
然后建立一个容量为k的大根堆，选择k个工作质量较小的工人，每次将工作质量较大的，踢出去，插入工作质量小的
最终，在比例越大，与工作质量之间，取得平衡，选择更小的作为答案输出出来
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    quality = [10,20,5]
    wage = [70,50,30]
    k = 2
    print("测试用例1输入 = {}, = {}, = {}:".format(quality, wage, k))
    print("测试用例1输出:", solution.mincostToHireWorkers(quality, wage, k))
    # 预期输出: 105
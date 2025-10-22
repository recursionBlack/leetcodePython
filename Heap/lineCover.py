"""
该题目属于牛客题，在leetcode上是会员题
所以这里手动输入描述
每一个线段都有start和end两个数据项，表示这条线段在X轴上从start位置开始到end位置结束，
给定一批线段，求所有重合区域中最多重合了几条香断，收尾相连的不算重合


"""

from typing import List
import heapq

class Solution:
    @classmethod
    def sort_by_first_element(cls, lst):
        # 使用sorted函数，key指定为每行的第0个元素
        return sorted(lst, key=lambda x: x[0])

    def maxCoverLine(self, lines: List[List[int]]) -> int:
        self.sort_by_first_element(lines)
        n = len(lines)
        res = 0
        hSize = 0
        heap = []
        for i in range(n):
            while hSize > 0 and heap[0] <= lines[i][0]:
                heapq.heappop(heap)
                hSize -= 1
            heapq.heappush(heap, lines[i][1])
            hSize += 1
            res = max(res, hSize)

        return res

"""
时间复杂度分析:
一共n条线段，n个结束的位置，每个都是进入一次，出一次，进入堆后，进行一下自动的排序
自动的排序时间复杂度为O(log n)，n条线段，时间复杂度为O(n * log n)

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    lines = [[1, 2],[2,3],[1,3]]
    print("测试用例1输入 = {}:".format(lines))
    print("测试用例1输出:", solution.maxCoverLine(lines))
    # 预期输出:2

    # # 测试用例1：基础案例
    lines = [[1,5], [1,3], [2,4],[2,6],[3,7],[5,9]]
    print("测试用例1输入 = {}:".format(lines))
    print("测试用例1输出:", solution.maxCoverLine(lines))
    # 预期输出:4
from typing import List
import heapq

# 632. 最小区间
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        # 初始化小根堆，存储元组(v, i, j)：值、来自第i个列表、在列表中的索引j
        heap = []
        current_max = -float('inf')  # 记录当前堆中最大的元素值

        # 初始化堆，加入每个列表的第一个元素
        for i in range(n):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))
            if val > current_max:
                current_max = val  # 更新初始最大值

        min_width = float('inf')
        a, b = 0, 0  # 存储最小范围的结果

        # 当堆中元素数量等于列表总数时（每个列表都有元素在堆中）
        while len(heap) == n:
            # 取出堆中最小的元素（当前范围的左边界）
            v_min, i_min, j_min = heap[0]
            # 计算当前范围宽度
            current_width = current_max - v_min

            # 更新最小范围
            if current_width < min_width:
                min_width = current_width
                a, b = v_min, current_max

            # 弹出最小元素，准备加入其所在列表的下一个元素
            heapq.heappop(heap)

            # 检查当前列表是否有下一个元素
            if j_min + 1 < len(nums[i_min]):
                j_new = j_min + 1
                v_new = nums[i_min][j_new]
                heapq.heappush(heap, (v_new, i_min, j_new))
                # 若新元素更大，更新当前最大值
                if v_new > current_max:
                    current_max = v_new

        return [a, b]

"""
对于堆，如果插入的元素不是数值，而是元组，堆是如何知道怎么排序的呢？
在 Python 中，当堆（通过 heapq 模块实现）中插入的元素是元组时，
堆会按照元组的元素顺序依次比较来确定排序规则，
本质上遵循 Python 对元组的默认比较逻辑。
先比较元组的第0个元素，再比较第一个元素，再比较第二个元素、、、、

如果每次往堆里插入的元素是列表呢？也跟元组类似吗？
在 Python 中，当往堆（heapq）中插入列表时，堆的排序逻辑与元组类似，
也是按列表的元素顺序依次比较，遵循 Python 对序列的默认比较规则。
但需要注意：列表与元组的比较逻辑本质相同，但列表是可变对象，而元组是不可变对象，不过这对比较逻辑本身没有影响。

从第一个元素开始比较：
第一个元素相等时，比较第二个元素：
"""

"""
左神推荐使用有序表，但python中没有java中的有序表，由于每次弹出的是最小值，可以用小根堆来替代
但小根堆，不知道最大值是什么，所以，额外使用一个变量来记录最大值，在每次往堆里加新元素时，就进行比较和记录，
从而始终知道堆的最大值。一个最大值变量和一个小根堆，实现了有序表。
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.smallestRange(nums))
    # 预期输出: [20,24]
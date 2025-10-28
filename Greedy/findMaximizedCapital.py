from typing import List
import heapq

# 502. IPO
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # 将profits和capital组合起来，并按本金排序，这样保证我们总能选取所有小于等于当前资本的
        projects = sorted(zip(profits, capital), key=lambda x: x[1])        # 大佬的题解里，没用字典啊！
        # zip压缩后，是个迭代器，被sorted转化为元组列表了
        cur = []
        idx = 0         # 就是没想到，引入该变量，防止重复遍历已经添加到大根堆里的数据啊，
        while k:
            # 将所有需要的本金小于等于当前资本的项目加入最大堆
            while idx < n and projects[idx][1] <= w:
                heapq.heappush(cur, -projects[idx][0])
                idx += 1
            # 如果有项目在当前的大顶堆中，我们做利益最大的那一个。
            if cur:
                w -= heapq.heappop(cur)
            else:
                break
            k -= 1
        return w

"""
该题听了左神的题解后，已经知道怎么做了，但在语法上，有些地方没有学透，
比如zip的返回值是个迭代器，和sorted可以将迭代器转化为列表，
而我选择了，将迭代器转化为了字典，
最终导致部分测例不通过，没有大佬的答案优雅

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]
    print("测试用例1输入 = {}，= {}，= {}，= {}，:".format(k, w, profits, capital))
    print("测试用例1输出:", solution.findMaximizedCapital(k, w, profits, capital))
    # 预期输出: 4

    # # 测试用例1：基础案例
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    print("测试用例1输入 = {}，= {}，= {}，= {}，:".format(k, w, profits, capital))
    print("测试用例1输出:", solution.findMaximizedCapital(k, w, profits, capital))
    # 预期输出: 6
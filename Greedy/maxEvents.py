from typing import List
from collections import defaultdict
import heapq

# 1353. 最多可以参加的会议数目
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        g = defaultdict(list)
        # 建立小根堆，维护会议结束时间
        heap = []
        # 找出会议开始的最早天数和结束的最晚天数
        minDay = 0
        maxDay = 0
        # 参加的会议次数
        ans = 0

        for begin, end in events:
            g[begin].append(end)
            minDay = min(minDay, begin)
            maxDay = max(maxDay, end)

        for day in range(minDay, maxDay + 1):
            # 当小根堆的顶部，已经小于天数时，说明该会议过期了，没有机会再参加了，丢弃掉
            while heap and heap[0] < day:
                heapq.heappop(heap)
            # 当天数来到会议开始时间的时候，将该会议的结束时间加入堆里
            for end in g[day]:
                heapq.heappush(heap, end)

            # 从未过期的会议中，弹出结束时间最早的那个，参加了，将参加的会议数量+1
            if heap:
                heapq.heappop(heap)
                ans += 1

        return ans


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    events = [[1,2],[2,3],[3,4]]
    print("测试用例1输入 = {}:".format(events))
    print("测试用例1输出:", solution.maxEvents(events))
    # 预期输出: 3

    # # 测试用例1：基础案例
    events = [[1,2],[2,3],[3,4],[1,2]]
    print("测试用例1输入 = {}:".format(events))
    print("测试用例1输出:", solution.maxEvents(events))
    # 预期输出: 4
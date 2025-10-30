from typing import List
import heapq

# 871. 最低加油次数
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        if not stations:
            return -1
        n = len(stations)
        heap = []
        to = startFuel
        cnt = 0 # 要加油的最少次数

        for m, fuel in stations:
            # 如果当前的油量，到达不了当前的加油站，则从大根堆里取出最多的油量
            while to < m:
                # 如果到达不了当前的加油站，而且堆里也已经没有油量了，则说明无法继续开下去了
                if not heap:
                    return -1
                to -= heap[0]
                heapq.heappop(heap)
                cnt += 1
                # 每次油量发生变化时，检查是否可以直接到达目的地
                # 如果可达到目的地，就直接返回了
                if to >= target:
                    return cnt

            # 如果能到达当前的加油站，就将加油站里的油量，加到大根堆里
            heapq.heappush(heap, -fuel)

        # 遍历完了所有的加油站，但程序还没有结束，就要直接与target进行比较了

        while to < target:
            # 如果可加油量已经没了，还没到达target，则表示最终到不了
            if not heap:
                return -1
            to -= heap[0]
            heapq.heappop(heap)
            cnt += 1

            if to >= target:
                return cnt

        # 油量加完，最终还是没有结束，表示到达不了目的地
        return -1

"""
主要要分析，每到达了一个加油站，该做什么事，如果到不了这个加油站，又该怎么办？
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    target = 100
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]
    print("测试用例1输入 = {}, = {}:".format(target, startFuel, stations))
    print("测试用例1输出:", solution.minRefuelStops(target, startFuel, stations))
    # 预期输出: 2

    # # 测试用例1：基础案例
    target = 1
    startFuel = 1
    stations = []
    print("测试用例1输入 = {}, = {}:".format(target, startFuel, stations))
    print("测试用例1输出:", solution.minRefuelStops(target, startFuel, stations))
    # 预期输出: 0
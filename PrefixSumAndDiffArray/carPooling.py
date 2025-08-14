from typing import List
from myLeetcodeUtils import Difference
from sortedcontainers import SortedDict

# 1094. 拼车
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cnt = SortedDict()

        for num, ffrom, tto in trips:
            cnt[ffrom] = cnt.get(ffrom, 0) + num
            cnt[tto] = cnt.get(tto, 0) - num

        prefixSum = 0
        for c in cnt.values():
            prefixSum += c
            if prefixSum > capacity:
                return False

        return True

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    print("测试用例1输入 = {}, = {}:".format(trips, capacity))
    print("测试用例1输出:", solution.carPooling(trips, capacity))
    # 预期输出: False
from typing import List
from myLeetcodeUtils import Difference

# 1109. 航班预订统计
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n+1)
        dif = answer[1:]
        def increment(dif: List[int], i: int, j: int, val: int):
            dif[i] += val
            if j + 1 < len(dif):
                dif[j+1] -= val

        for first, last, seat in bookings:
            increment(dif, first-1, last-1, seat)

        for i in range(n):
            answer[i+1] = answer[i] + dif[i]

        return answer[1:]

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    print("测试用例1输入 = {}, = {}:".format(bookings, n))
    print("测试用例1输出:", solution.corpFlightBookings(bookings, n))
    # 预期输出: [10,55,45,25,25]

    # 测试用例1：基础案例
    bookings = [[1,2,10],[2,2,15]]
    n = 2
    print("测试用例1输入 = {}, = {}:".format(bookings, n))
    print("测试用例1输出:", solution.corpFlightBookings(bookings, n))
    # 预期输出: [10,25]
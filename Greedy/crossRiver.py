"""
过河问题（洛谷P1809）
一共n个人出游，他们走到一条河的西岸，想要过河到东岸
每个人都有一个过河时间Ti，西岸有一条船，一次最多乘坐两人
如果船上有一个人，划到对岸的时间，就是这个人的过河时间，
如果船上有两个人，划到对岸的时间，是这两个人中的较大时间
求全部人过河的最少时间是多少？
"""
from typing import List

class Solution:
    def __init__(self):
        self.dp = []
    def travelRiver(self, arr: List[int]) -> int:
        n = len(arr)
        if not self.dp:
            self.dp = [0] * n
        arr.sort()
        if n >= 1:
            self.dp[0] = arr[0]
        if n >= 2:
            self.dp[1] = arr[1]
        if n >= 3:
            self.dp[2] = arr[0] + arr[1] + arr[2]

        for i in range(3, n):
            # 方法1：
            # 由跑的最快的来运送第i个人
            # 方法2：
            # 由跑的最快的两个人，运送第i和第i-1个人
            self.dp[i] = min(self.dp[i-1] + arr[0] + arr[i],
                             self.dp[i-2] + arr[1] + arr[1] + arr[i] + arr[0])

        return self.dp[n-1]



"""
解决办法，因为每次船都要回来，所以最好想到的策略是，每次让回来最快的人，把每个人一一送过去
但是，还有一种办法，就是以四个人为一组的拉，
其中，每次都是，速度最快的两个人，两个人先过去，然后，让任意一个人回来，再选两个速度最慢的一块乘船，
之后，由留在右侧的人，再单人开船回来，从而实现了把两个速度最慢的人，给送回来的方式。这样，每次可以送回两个左侧最慢的
而只用承担其中一个较慢的人的代价，

但其中，两种方案在某些情况下，依然某些情况各有发挥，所以需要用动态规划，
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    arr = [6,7,10,15]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.travelRiver(arr))
    # 预期输出: 42
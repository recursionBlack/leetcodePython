from typing import List

# 547. 省份数量
class Solution:
    def __init__(self):
        self.MAXSIZE = 200
        self.father = [1] * self.MAXSIZE
        self.sets = 0

    def build(self, isConnected: List[List[int]]):
        n = len(isConnected)
        for i in range(n):
            self.father[i] = i
            self.sets += 1

    def find(self, i: int) -> int:
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, x: int, y: int):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy
            self.sets -= 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.build(isConnected)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    self.union(i, j)

        return self.sets


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print("测试用例1输入 = {}:".format(isConnected))
    print("测试用例1输出:", solution.findCircleNum(isConnected))
    # 预期输出:2

    solution2 = Solution()
    # 测试用例1：基础案例
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print("测试用例1输入 = {}:".format(isConnected))
    print("测试用例1输出:", solution2.findCircleNum(isConnected))
    # 预期输出:3
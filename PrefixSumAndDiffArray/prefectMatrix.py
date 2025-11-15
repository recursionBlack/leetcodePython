import sys
from typing import List
from collections import defaultdict

"""
小美拿到了一个
n
∗
n
n∗n的矩阵，其中每个元素是 0 或者 1。
小美认为一个矩形区域是完美的，当且仅当该区域内 0 的数量恰好等于 1 的数量。
现在，小美希望你回答有多少个
i
∗
i
i∗i的完美矩形区域。你需要回答
1
≤
i
≤
n
1≤i≤n的所有答案。
"""
class NumMatrix:
    def __init__(self, n: int, nums: List[List[int]]):
        self.n = n
        self.preSum = []
        # 初始化空矩阵，分配内存
        for i in range(self.n + 1):
            raw = [0] * (self.n + 1)
            self.preSum.append(raw)
        # 填写数据
        for i in range(n):
            for j in range(n):
                self.preSum[i+1][j+1] = self.preSum[i+1][j] + self.preSum[i][j+1] - self.preSum[i][j] + nums[i][j]

    # 区域求和
    def sumRegion(self, raw1: int, col1: int, raw2: int, col2: int) -> int:
        res = self.preSum[raw2][col2] - self.preSum[raw1][col2] - self.preSum[raw2][col1] + self.preSum[raw1][col1]
        return res


class Solution:
    def solve(self, nums: List[List[int]]):
        n = len(nums)
        nM = NumMatrix(n, nums)
        mydict = defaultdict(int)

        # 起始点的位置
        for i in range(n):
            for j in range(n):
                # 矩形的宽度
                for width in range(1, n):
                    if width & 1:
                        mydict[width] = 0
                        continue
                    if i + width > n or j + width > n:
                        break
                    if width not in mydict:
                        mydict[width] = 0
                    # 统计子矩阵的1和0的数量
                    target = width * width // 2
                    cnt = nM.sumRegion(i, j, i+width, j+width)
                    if cnt == target:
                        mydict[width] += 1

        if n % 2 == 0:
            target = n * n // 2
            if target == nM.preSum[n][n]:
                mydict[n] = 1
            else:
                mydict[n] = 0

        return mydict


if __name__ == "__main__":

    n = int(input())
    mat = []
    """
    4
    1010
    0101
    1100
    0011
    """
    for _ in range(n):
        line = sys.stdin.readline().strip()
        digits = [int(c) for c in line]
        mat.append(digits)

    solution = Solution()
    res = solution.solve(mat)

    sorted_keys = sorted(res.keys())

    for key in sorted_keys:
        print(res[key])
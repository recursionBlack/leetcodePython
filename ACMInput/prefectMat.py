from collections import defaultdict
import sys
from typing import List

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

class Solution:
    def solve(self, nums: List[List[int]]):
        n = len(nums)
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
                    cnt = 0
                    for ii in range(i, i + width):
                        for jj in range(j, j + width):
                            cnt += nums[ii][jj]

                    target = width * width // 2
                    if cnt == target:
                        mydict[width] += 1

        if n % 2 == 0:
            target = n * n // 2
            sums = 0
            for line in nums:
                sums += sum(line)
            if sums == target:
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

"""
没想到，这个题，总测例30道，居然只通过了4道？？？但是错的地方不给看了，就不知道为啥错了。

看了答案，发现，果然，居然要用二维前缀和？？？我还傻傻的按照题意求解，难怪后面想不出来了
"""
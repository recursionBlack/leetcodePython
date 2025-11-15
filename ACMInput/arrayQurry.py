import sys
from typing import List
from collections import Counter

"""
2.
小美的数组询问
小美拿到了一个由正整数组成的数组，但其中有一些元素是未知的（用 0 来表示）。
现在小美想知道，如果那些未知的元素在区间
[
l
,
r
]
[l,r]范围内随机取值的话，数组所有元素之和的最小值和最大值分别是多少？
共有
q
q次询问。
"""

class Solution:
    def solve(self, nums: List[int], queryArray: List[List[int]]) -> List[List[int]]:
        cnt = Counter(nums)

        sums = sum(nums)
        zeroNum = cnt[0]
        res = []
        for l, r in queryArray:
            minSum = sums + zeroNum * l
            maxSum = sums + zeroNum * r
            res.append([minSum, maxSum])

        return res


if __name__ == "__main__":
    solution = Solution()

    """
        3 2
        1 0 3
        1 2
        4 4
    """

    first_line = sys.stdin.readline().strip()
    data = list(map(int, first_line.split()))

    second_line = sys.stdin.readline().strip()
    data2 = list(map(int, second_line.split()))
    array = data2[0: data[0]]

    queryArray = []
    for _ in range(data[1]):
        queryLine = sys.stdin.readline().strip()
        query = list(map(int, queryLine.split()))
        queryArray.append(query[:2])

    res = solution.solve(array, queryArray)
    # 期望输出：
    """
        5 6
        8 8
    """
    for l, r in res:
        print("{} {}".format(l, r))


"""
ac, 比较简单，没用啥操作
"""
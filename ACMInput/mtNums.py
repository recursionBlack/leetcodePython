import sys
from collections import Counter

"""
MT 是美团的缩写，因此小美很喜欢这两个字母。
现在小美拿到了一个仅由大写字母组成字符串，她可以最多操作
k
k次，每次可以修改任意一个字符。小美想知道，操作结束后最多共有多少个'M'和'T'字符？

"""

class Solution:
    def solve(self, strs: str, num: int) -> int:
        cnt = Counter(strs)
        n = len(strs)

        mt = cnt["M"] + cnt["T"]
        if num > n - mt:
            return n
        return mt + num


if __name__ == "__main__":
    solution = Solution()

    first_line = sys.stdin.readline().strip()
    data1 = list(map(int, first_line.split()))

    second_line = sys.stdin.readline().strip()

    res = solution.solve(second_line, data1[1])
    print(res)

"""
AC,没啥好讨论的
"""
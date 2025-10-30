from typing import List

# 1326. 灌溉花园的最少水龙头数目
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # right[i] = j 表示，所有左边界在i的水龙头里，最右侧能影响到j
        right = [0] * (n+1)
        start = 0
        for i in range(n+1):
            start = max(0, i - ranges[i])
            right[start] = max(right[start], i + ranges[i])

        # 当前ans数量的水龙头，打开了，最右影响的边界
        cur = 0
        # 如果再多打开一个水龙头，最右影响的边界
        next = 0
        # 打开水龙头的数量
        ans = 0
        for i in range(n):
            next = max(next, right[i])
            if i == cur:
                if next > i:
                    cur = next
                    ans += 1
                else:
                    return -1

        return ans


"""
说这个题，和45题很像，但45题看起来就很明了，这个题，还要自己实现，改造出一个right列表，
大大增加了理解上的难度，就这吧，难度太高了，
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    n = 5
    ranges = [3,4,1,1,0,0]
    print("测试用例1输入 = {},= {}:".format(n, ranges))
    print("测试用例1输出:", solution.minTaps(n, ranges))
    # 预期输出: 1
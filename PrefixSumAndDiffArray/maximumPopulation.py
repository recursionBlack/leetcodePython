from typing import List

# 1854. 人口最多的年份
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101
        offset = 1950
        for bir, die in logs:
            delta[bir - offset] += 1
            delta[die - offset] -= 1
        mx = 0      # 人口最多的峰值
        ans = 0     # 人口最多的年份
        presum = 0  # 原数组
        for i in range(101):
            presum += delta[i]
            if presum > mx:
                mx = presum
                ans = i

        return ans + offset

"""
该题，用到了差分数组的一个很有趣的性质：差分数组的前缀和，就是原数组。
这也是差分数组，为何总是和前缀和捆绑到一块的原因
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    logs = [[1993,1999],[2000,2010]]
    print("测试用例1输入logs = {}:".format(logs))
    print("测试用例1输出:", solution.maximumPopulation(logs))
    # 预期输出: 1993

    # 测试用例1：基础案例
    logs = [[1950,1961],[1960,1971],[1970,1981]]
    print("测试用例1输入logs = {}:".format(logs))
    print("测试用例1输出:", solution.maximumPopulation(logs))
    # 预期输出: 1960
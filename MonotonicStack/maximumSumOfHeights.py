from typing import List

# 2866. 美丽塔 II
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        tmp = maxHeights[:]
        tmp.sort()
        # 找到最大值所在的坐标
        maxI = maxHeights.index(tmp[-1])

        monoStack = []
        ans = 0
        # 处理左侧
        for i in range(maxI - 1, -1, -1):
            if monoStack and maxHeights[i] < maxHeights[monoStack[0]]:
                ans += maxHeights[monoStack[0]] * (monoStack[0] - i)
                monoStack = []
            monoStack.append(i)

        # 清空栈内，
        if monoStack:
            ans += maxHeights[monoStack[0]] * (monoStack[0] + 1)
            monoStack = []

        # 处理右侧
        for i in range(maxI, n):
            if monoStack and maxHeights[i] < maxHeights[monoStack[0]]:
                ans += maxHeights[monoStack[0]] * (i - monoStack[0])
                monoStack = []
            monoStack.append(i)

        # 清空栈内，
        if monoStack:
            ans += maxHeights[monoStack[0]] * (n - monoStack[0])

        return ans


"""
该方法只能处理，最大值唯一的美丽塔，如果最大值不止有一个，比如，全数组的元素一样，就会很麻烦

没做出来，也没看懂题解，无语了，不做了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    maxHeights = [5,3,4,1,1]
    print("测试用例1输入 = {}:".format(maxHeights))
    print("测试用例1输出:", solution.maximumSumOfHeights(maxHeights))
    # 预期输出:13

    # 测试用例1：基础案例
    maxHeights = [6,5,3,9,2,7]
    print("测试用例1输入 = {}:".format(maxHeights))
    print("测试用例1输出:", solution.maximumSumOfHeights(maxHeights))
    # 预期输出:22
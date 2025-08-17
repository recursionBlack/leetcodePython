from typing import List

# 84. 柱状图中最大的矩形
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        monoStack = []

        ans = 0
        # 遍历阶段
        for i in range(n):
            while monoStack and heights[i] <= heights[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                left = monoStack[-1] if monoStack else -1
                ans = max(ans, heights[cur] * (i - left - 1))
            monoStack.append(i)

        # 清算阶段
        last = monoStack[-1]
        while monoStack:
            cur = monoStack[-1]
            monoStack.pop()
            left = monoStack[-1] if monoStack else -1
            ans = max(ans, heights[cur] * (last - left))

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    heights = [2,1,5,6,2,3]
    print("测试用例1输入 = {}:".format(heights))
    print("测试用例1输出:", solution.largestRectangleArea(heights))
    # 预期输出: 10

    # 测试用例1：基础案例
    heights = [2,4]
    print("测试用例1输入 = {}:".format(heights))
    print("测试用例1输出:", solution.largestRectangleArea(heights))
    # 预期输出: 4
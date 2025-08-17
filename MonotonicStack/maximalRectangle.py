from typing import List

# 85. 最大矩形
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            monoStack = []

            ans = 0
            for i in range(n):
                while monoStack and heights[i] <= heights[monoStack[-1]]:
                    cur = monoStack[-1]
                    monoStack.pop()
                    left = monoStack[-1] if monoStack else -1
                    ans = max(ans, heights[cur] * (i-left-1))
                monoStack.append(i)

            last = monoStack[-1]
            while monoStack:
                cur = monoStack[-1]
                monoStack.pop()
                left = monoStack[-1] if monoStack else -1
                ans = max(ans, heights[cur] * (last - left))

            return ans

        n = len(matrix)
        m = len(matrix[0])

        area = 0
        heights = [0] * m
        for row in matrix:
            for i in range(m):
                if row[i] == "0":
                    heights[i] = 0
                else:
                    heights[i] += 1
            area = max(area, largestRectangleArea(heights))

        return area

"""
看了左神讲解，一次过，哈哈哈哈，
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print("测试用例1输入 = {}:".format(matrix))
    print("测试用例1输出:", solution.maximalRectangle(matrix))
    # 预期输出: 6

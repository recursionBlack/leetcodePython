# 根据左程云算法讲解052的一道题，位于牛客网上的
# 非常经典的单调栈解题模板

"""
给定一个数组，求解每个位置元素的，左侧最近的小于其的值，和右侧最近的小于其的值，如果没有，请写成-1
数组容量最大为1000
"""
from typing import List

class Solution:
    def leftRightLess(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        stack = [0] * n
        ans = []
        for i in range(n):
            ans.append([0, 0])

        cur = r = 0     # cur是栈顶的值，r是栈顶指针
        # 遍历阶段
        for i in range(n):
            while r > 0 and arr[i] <= arr[stack[r-1]]:
                cur = stack[r-1]    # 栈顶元素值
                r -= 1
                ans[cur][0] = stack[r-1] if r > 0 else -1
                ans[cur][1] = i
            stack[r] = i
            r += 1

        # 清算阶段。遍历完整个数组了，但栈内还有一些值，对栈内剩余值的处理
        while r > 0:
            cur = stack[r - 1]  # 栈顶元素值
            r -= 1
            ans[cur][0] = stack[r-1] if r > 0 else -1
            ans[cur][1] = -1

        # 修正阶段。因为该题未保证，数组中的每一个元素都不相同，所以有一些值是相等的，
        # 而对于这些相等的值的处理，就是右侧的值暂时也是相等的，通过修正阶段，才全部改为严格小于的
        for i in range(n-2, -1, -1):
            if ans[i][1] != - 1 and arr[ans[i][1]] == arr[i]:
                ans[i][1] = ans[ans[i][1]][1]

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    arr = [2,3,4,3,2,1,3,5,6,3,4,3,2]       # 有重复值的
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.leftRightLess(arr))
    # 预期输出: [[-1, 5],[0,4],[1,3],[0,4],[-1,5],[-1,-1],[5,12],[6,9],[7,9],[5,12],[9,11],[5,12],[5,-1]]

    # 测试用例1：基础案例
    arr = [2,5,6,7,3,4,1,8]         # 严格无重复值的
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.leftRightLess(arr))
    # 预期输出: [[-1, 6], [0, 4], [1, 4], [2, 4], [0, 6], [4, 6], [-1, -1], [6, -1]]
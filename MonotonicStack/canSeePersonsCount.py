from typing import List

# 1944. 队列中可以看到的人数
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        monoStack = []
        ans = [0] * n

        for i in range(n-1, -1, -1):
            while monoStack and heights[i] > heights[monoStack[-1]]:
                monoStack.pop()
                ans[i] += 1
            # 小于栈顶元素的
            if monoStack:
                ans[i] += 1
            monoStack.append(i)

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    heights = [10,6,8,5,11,9]
    print("测试用例1输入 = {}:".format(heights))
    print("测试用例1输出:", solution.canSeePersonsCount(heights))
    # 预期输出:[3,1,2,1,1,0]

    # 测试用例1：基础案例
    heights = [5,1,2,3,10]
    print("测试用例1输入 = {}:".format(heights))
    print("测试用例1输出:", solution.canSeePersonsCount(heights))
    # 预期输出:[4,1,1,1,0]
from typing import List

# 962. 最大宽度坡
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        monoStack = []

        # 建立一个单调栈，但不pop任何元素
        for i in range(n):
            if not monoStack:
                monoStack.append(i)
                continue
            if nums[i] < nums[monoStack[-1]]:
                monoStack.append(i)

        maxWidth = 0
        # 再倒序遍历
        for i in range(n-1, -1, -1):
            while monoStack and nums[i] >= nums[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                maxWidth = max(maxWidth, i-cur)

        return maxWidth


"""
该题又是一个，用了单调栈，但又不是传统经典单调栈模板的问题，感觉这种类型的题，现在好多啊！！！
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [6,0,8,2,1,5]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.maxWidthRamp(nums))
    # 预期输出:4
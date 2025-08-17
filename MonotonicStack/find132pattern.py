from typing import List

# 456. 132 模式
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = -(10 ** 9 + 7)
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] < k:
                return True
            while stack and nums[i] > stack[-1]:
                k = max(k, stack.pop())
            stack.append(nums[i])
        return False

"""
其实这里维护的是在 (i, n - 1]中, 能找到的最优 (3, 2) 型元组.
stack维护的是 3
k维护的是 2
因为k是从stack中弹出的, 故下标必比3的下标大, 且值必比3小
故只需枚举到 nums[i] 是否满足 < k 就行了.
"""

"""
该题虽说是用的单调栈，但其与左神所说的，左侧最近的较小/较大值，和右侧最近的较小/较大值，都不符合
完全不符合左神模板，故没有看出来，还是从题解中，看到为啥可以用单调栈了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,3,4]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.find132pattern(nums))
    # 预期输出: false

    # 测试用例1：基础案例
    nums = [3,1,4,2]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.find132pattern(nums))
    # 预期输出: True
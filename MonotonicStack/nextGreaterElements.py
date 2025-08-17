from typing import List

# 503. 下一个更大元素 II
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        monoStack = []
        ans = [0] * n

        for i in range(n):
            while monoStack and nums[i] >= nums[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                ans[cur] = i
            monoStack.append(i)

        # 找到全数组最大值的位置
        bigI = monoStack[0]
        # 第二轮，注意此时需要严格大于了，而不能再大于等于了
        for i in range(bigI + 1):
            while monoStack and nums[i] > nums[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                ans[cur] = i
            monoStack.append(i)

        ans[bigI] = -1
        # 修正阶段
        for i in range(n-1, -1, -1):
            if ans[i] != - 1 and nums[ans[i]] == nums[i]:
                ans[i] = ans[ans[i]]

        for i in range(n):
            if ans[i] != -1:
                ans[i] = nums[ans[i]]

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,2,1]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.nextGreaterElements(nums))
    # 预期输出: [2,-1,2]

    # # 测试用例1：基础案例
    nums = [1,1,1,1,1]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.nextGreaterElements(nums))
    # 预期输出: [-1,-1,-1,-1,-1]

    # 测试用例1：基础案例
    nums = [1,2,3,2,1]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.nextGreaterElements(nums))
    # 预期输出: [2,3,-1,3,2]
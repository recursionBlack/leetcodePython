from typing import List

# 1793. 好子数组的最大分数
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        monoStack = []

        area = 0
        for i in range(n):
            while monoStack and nums[i] <= nums[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                left = monoStack[-1] if monoStack else -1
                if left < k < i:
                    area = max(area, nums[cur] * (i -left -1))
            monoStack.append(i)

        while monoStack:
            cur = monoStack[-1]
            monoStack.pop()
            left = monoStack[-1] if monoStack else -1
            if left < k < n:
                area = max(area, nums[cur] * (n - left - 1))

        return area


"""
这个问题，几乎做出来了，但就是，中间的哪个k不知道怎么处理，经过几次实验后，终于将k的范围定在了left < k <= i-1
而一开始，用的是left <= k <= i，总之，测试用例差了十几个就快通过了。看了别人的题解后，我觉得，左神模板没问题啊，
还是范围取得有问题
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [1,4,3,7,4,5]
    k = 3
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.maximumScore(nums, k))
    # 预期输出:15

    # 测试用例1：基础案例
    nums = [5,5,4,5,4,1,1,1]
    k = 0
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.maximumScore(nums, k))
    # 预期输出:20
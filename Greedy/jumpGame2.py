from typing import List

# 45. 跳跃游戏 II
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cur = 0     # 当前位置
        next = nums[cur]    # 下一步可以跳到的最远位置
        ans = 0     # 总共跳跃的最少次数

        for i in range(n):
            if cur < i:
                ans += 1
                cur = next
            next = max(next, i + nums[i])

        return ans


"""
列一些简单的例子，观察规律，就很容易发现，需要同时记录当前位置，以及下一次跳跃时，可到达的最远位置
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [2,3,1,1,4]
    print("测试用例1输入 = {},:".format(nums))
    print("测试用例1输出:", solution.jump(nums))
    # 预期输出: 2
from typing import List

# 55. 跳跃游戏
class Solution:
    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
        cur = 0     # 当前位置
        next = nums[cur]    # 下一步可以跳到的最远位置

        for i in range(n):
            if cur < i:
                cur = next
            if next < i:
                return False
            next = max(next, i + nums[i])

        return True


"""
列一些简单的例子，观察规律，就很容易发现，需要同时记录当前位置，以及下一次跳跃时，可到达的最远位置
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [3,2,1,0,4]
    print("测试用例1输入 = {},:".format(nums))
    print("测试用例1输出:", solution.jump(nums))
    # 预期输出: false
from typing import List
import heapq

# 2208. 将数组和减半的最少操作次数
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sumN = sum(nums)

        # 需要减少的目标
        sumN /= 2
        # 全员取反，因为heapq是小根堆，取反后当大根堆来用
        heap = [float(-x) for x in nums]
        ans = 0
        # 堆化
        heapq.heapify(heap)
        while sumN > 0:
            x = heapq.heappop(heap)
            sumN += x/2
            heapq.heappush(heap, x/2)
            ans += 1

        return ans

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [5,19,8,1]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.halveArray(nums))
    # 预期输出:3

    # # 测试用例1：基础案例
    nums = [3,8,20]
    print("测试用例1输入 = {}:".format(nums))
    print("测试用例1输出:", solution.halveArray(nums))
    # 预期输出:3


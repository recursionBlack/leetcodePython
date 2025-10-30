from typing import List
import heapq

# 1675. 数组的最小偏移量
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        heap = []
        minInheap = float("inf")
        # 入堆
        for i in range(n):
            if nums[i] & 1:
                nums[i] *= 2

            minInheap = min(minInheap, nums[i])
            heapq.heappush(heap, -nums[i])
        # 出堆
        cur = heap[0]
        ans = float("inf")
        while cur % 2 == 0:
            heapq.heappop(heap)
            ans = min(ans, -cur - minInheap)
            minInheap = min(minInheap, -cur//2)
            heapq.heappush(heap, cur//2)
            cur = heap[0]

        return min(ans, -heap[0] - minInheap)


"""
时间复杂度分析：对于进入的每个数，其经历过的除2的次数为log2 k
总共n的数，每个数都可能经历那么多次的除以2，
堆内数据大小也为n，每次堆调整的时间复杂度也为log2 n
所以，总的时间复杂度为 O(n * log2_n * log2_k)
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    nums = [1,2,3,4]
    print("测试用例1输入 = {},:".format(nums))
    print("测试用例1输出:", solution.minimumDeviation(nums))
    # 预期输出: 1

    # # 测试用例1：基础案例
    nums = [3, 5]
    print("测试用例1输入 = {},:".format(nums))
    print("测试用例1输出:", solution.minimumDeviation(nums))
    # 预期输出: 1
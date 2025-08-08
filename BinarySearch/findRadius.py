from typing import List

# 475. 供暖器
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        ans = 0
        heaters.sort()
        for h in houses:
            left = 0
            right = len(heaters) - 1
            dist = float("Inf")
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] - h <= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            # 此时的left就是第一个大于h的值，left - 1就是最后一个小于h的值，
            # 但要注意，left -1 可能不存在，比如只有一个元素
            # 防止左侧最近的heater超出边界
            if left - 1 < 0:
                dist = heaters[left] - h
            # 防止右侧最近的heater超出边界
            elif left > len(heaters) - 1:
                dist = h - heaters[left - 1]
            # 左右两个heater都没超出边界
            else:
                dist = min(h - heaters[left - 1], heaters[left] - h)

            ans = max(ans, dist)

        return ans

"""
又一个，看了题解才明白题目想表达什么的问题，
对于两个序列，房子和暖气，用二分法，在暖气序列里，查找到距离其最近的暖气，记录该距离
并于ans比较，ans取所有房子最近的暖气距离的最大值，就是要找的答案

这里，需要理解，并自己手撕一个upper_bound，才能明白，循环结束时，left和right时，分别表示的含义

def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1  # 右边界初始化为数组最后一个元素的索引
    
    while left <= right:
        mid = left + (right - left) // 2  # 避免整数溢出（Python中无此问题，但保持习惯）
        
        if arr[mid] <= target:
            # 当前元素小于等于目标值，说明第一个大于target的位置在右侧
            left = mid + 1
        else:
            # 当前元素大于目标值，可能是候选位置，但需继续向左查找更左侧的符合条件位置
            right = mid - 1
    
    # 循环结束时，left即为第一个大于target的位置
    return left

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    houses = [1,2,3]
    heaters = [2]
    print("测试用例1输入houses = {}, heaters = {}:".format(houses, heaters))
    print("测试用例1输出:", solution.findRadius(houses, heaters))
    # 预期输出: 1
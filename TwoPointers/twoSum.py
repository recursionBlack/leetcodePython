from typing import List

# 167. 两数之和 II - 输入有序数组
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while left <= right:
            if numbers[left] + numbers[right] < target:
                # c++, java,可能存在(right + left)超出整形范围的问题，可以使用left + (right - left) // 2
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums = [3,24,50,79,88,150,345]
    target = 200
    print("测试用例1输入nums = {}, target = {}:".format(nums, target))
    print("测试用例1输出:", solution.twoSum(nums, target))
    # 预期输出: 12.75
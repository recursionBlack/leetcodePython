from typing import List

# 167. 两数之和 II - 输入有序数组
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         n = len(numbers)
#         left = 0
#         right = n - 1
#
#         while left <= right:
#             if numbers[left] + numbers[right] < target:
#                 # c++, java,可能存在(right + left)超出整形范围的问题，可以使用left + (right - left) // 2
#                 left += 1
#             elif numbers[left] + numbers[right] > target:
#                 right -= 1
#             else:
#                 return [left + 1, right + 1]
#
#         return [-1, -1]

"""
用双指针就可以了，但既然二分查找也能解，那就二分法也写了吧
具体解法，就是使用for循环固定一个数，再用二分法，去找target与固定的数的差
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (right + left) // 2
                if numbers[mid] < target - numbers[i]:
                    left = mid + 1
                elif numbers[mid] > target - numbers[i]:
                    right = mid - 1
                else:
                    return [i+1, mid+1]

        return [-1, -1]

"""
结果就是，速度比双指针还要慢很多，不过，为了练习新题型也就这样了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # nums = [3,24,50,79,88,150,345]
    # target = 200
    # print("测试用例1输入nums = {}, target = {}:".format(nums, target))
    # print("测试用例1输出:", solution.twoSum(nums, target))
    # # 预期输出: [3, 6]

    # 测试用例1：基础案例
    nums = [2,7,11,15]
    target = 9
    print("测试用例1输入nums = {}, target = {}:".format(nums, target))
    print("测试用例1输出:", solution.twoSum(nums, target))
    # 预期输出: [1, 2]
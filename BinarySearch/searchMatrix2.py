from typing import List

# 240. 搜索二维矩阵 II
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target< matrix[0][0]:
            return False
        # 逐列进行二分查找
        for l in matrix:
            if target >= l[0] and target <= l[-1]:
                left = 0
                right = len(l) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if l[mid] == target:
                        return True
                    elif l[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        return False

"""
这个问题把我绕晕了，我居然真的按照二维逐渐往中间靠去了，
最后其实逐行执行二分查找就行了
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    # target = 5
    # print("测试用例1输入matrix = {}, target = {}:".format(matrix, target))
    # print("测试用例1输出:", solution.searchMatrix(matrix, target))
    # # 预期输出: True

    # 测试用例1：基础案例
    # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    # target = 20
    # print("测试用例1输入matrix = {}, target = {}:".format(matrix, target))
    # print("测试用例1输出:", solution.searchMatrix(matrix, target))
    # # 预期输出: False

    # 测试用例1：基础案例
    # matrix = [[-5]]
    # target = -2
    # print("测试用例1输入matrix = {}, target = {}:".format(matrix, target))
    # print("测试用例1输出:", solution.searchMatrix(matrix, target))
    # # 预期输出: False

    # 测试用例1：基础案例
    # matrix = [[1,1]]
    # target = 2
    # print("测试用例1输入matrix = {}, target = {}:".format(matrix, target))
    # print("测试用例1输出:", solution.searchMatrix(matrix, target))
    # # 预期输出: False

    # 测试用例1：基础案例
    # matrix = [[-1],[-1]]
    # target = 0
    # print("测试用例1输入matrix = {}, target = {}:".format(matrix, target))
    # print("测试用例1输出:", solution.searchMatrix(matrix, target))
    # # 预期输出: False

    # 测试用例1：基础案例
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 15
    print("测试用例1输入matrix = {}, target = {}:".format(matrix, target))
    print("测试用例1输出:", solution.searchMatrix(matrix, target))
    # 预期输出: False


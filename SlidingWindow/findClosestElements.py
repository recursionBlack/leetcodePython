from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        nums = []
        for num in arr:
            nums.append(abs(num - x))

        min_dist = curdist = sum(nums[:k])
        begin = 0
        for i in range(k, len(nums)):
            curdist = curdist - nums[i-k] + nums[i]
            if curdist < min_dist:
                begin = i - k + 1
                min_dist = curdist

        return arr[begin: begin + k]

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # arr = [1,2,3,4,5]
    # k = 4
    # x = 3
    # print("测试用例1输入arr = {}, k = {}, x = {}:".format(arr, k, x))
    # print("测试用例1输出:", solution.findClosestElements(arr, k, x))
    # # 预期输出: [1,2,3,4]

    # 测试用例1：基础案例
    arr = [0,1,1,1,2,3,6,7,8,9]
    k = 9
    x = 4
    print("测试用例1输入arr = {}, k = {}, x = {}:".format(arr, k, x))
    print("测试用例1输出:", solution.findClosestElements(arr, k, x))
    # 预期输出: [0,1,1,1,2,3,6,7,8]

    # 测试用例1：基础案例
    # arr = [1,1,1,10,10,10]
    # k = 1
    # x = 9
    # print("测试用例1输入arr = {}, k = {}, x = {}:".format(arr, k, x))
    # print("测试用例1输出:", solution.findClosestElements(arr, k, x))
    # # 预期输出: [10]
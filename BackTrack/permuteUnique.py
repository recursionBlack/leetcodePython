from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int], n: int, tmp: List[int], path: List[List[int]]):
            if n == len(nums):
                path.append(tmp[:])

            for i in range(len(nums)):
                # 同级的相同数字必须跳过，纵向的相同数字则可以使用
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                # 纵向的数字，检查使用次数，是否达到nums里该数字的上限？
                if tmp.count(nums[i]) == nums.count(nums[i]):
                    continue

                tmp.append(nums[i])
                dfs(nums, n + 1, tmp, path)
                tmp.pop()

        nums.sort()
        path = []
        dfs(nums, 0, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [1, 1, 2]
    print("测试用例1输入nums1 = {}:".format(nums1))
    print("测试用例1输出:", solution.permuteUnique(nums1))
    # 预期输出: [[1,1,2], [1,2,1], [2,1,1]]
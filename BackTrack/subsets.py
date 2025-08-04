from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 这道题，跟其他的回溯不太一样，其他回溯算法都是定长的，但这个是变长的
        # 其他的是，只有达到指定长度后，才会添加到结果路径中，
        def dfs(nums: List[int], startIndex: int, tmp: List[int], path: List[List[int]]):
            path.append(tmp[:])         # 当前数字不选，直接加到结果路径里
            for i in range(startIndex, len(nums)):      # 当前数字选择，继续dfs，但要从startIndex开始
                tmp.append(nums[i])
                dfs(nums, i + 1, tmp, path)
                tmp.pop()

        nums.sort()
        path = []
        dfs(nums, 0, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [1, 2, 3]
    print("测试用例1输入nums1 = {}:".format(nums1))
    print("测试用例1输出:", solution.subsets(nums1))
    # 预期输出: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
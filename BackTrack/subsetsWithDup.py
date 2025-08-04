from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int], startIndex: int, tmp: List[int], path: List[List[int]]):
            path.append(tmp[:])
            for i in range(startIndex, len(nums)):
                # 同层剪枝去重
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                dfs(nums, i + 1, tmp, path)
                tmp.pop()

        nums.sort()
        path = []
        dfs(nums, 0, [], path)

        return path
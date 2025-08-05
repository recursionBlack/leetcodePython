from typing import List, Set

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int], startIndex: int, tmp: List[int], path: List[List[int]]):
            if len(tmp) > 1:
                    path.append(tmp[:])

            usage_list = set()    # 仅对同层去重，不用加入dfs参数，
            for i in range(startIndex, len(nums)):
                # 当前数字小于tmp的最后一个数字,继续往后执行，不能break，
                if (tmp and nums[i] < tmp[-1]) or nums[i] in usage_list:
                    continue
                usage_list.add(nums[i])
                tmp.append(nums[i])
                dfs(nums, i + 1, tmp, path)
                tmp.pop()

        path = []
        dfs(nums, 0, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [4, 6, 7, 7]
    print("测试用例1输入nums1 = {}:".format(nums1))
    print("测试用例1输出:", solution.findSubsequences(nums1))
    # 预期输出: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n表示当前用的是nums里的第几个数
        def dfs(nums: List[int], n: int, tmp: List[int], path: List[List[int]])->None:
            if n == len(nums):
                path.append(tmp[:])
                return

            for num in nums:
                # 如果该数字已经被添加进tmp里了，就跳过。
                if num in tmp:
                    continue
                tmp.append(num)
                dfs(nums, n + 1, tmp, path)
                tmp.pop()

        path = []
        dfs(nums, 0, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    nums1 = [1, 2, 3]
    print("测试用例1输入nums1 = {}:".format(nums1))
    print("测试用例1输出:", solution.permute(nums1))
    # 预期输出: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
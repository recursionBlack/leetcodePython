from typing import List

# 完全背包式的解法，不算回溯
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         tmp = []
#         path = []
#
#         # left：剩余值，而不是左侧的
#         def dfs(i: int, left: int) -> None:
#             if left == 0:
#                 # 找到一个合法组合
#                 path.append(tmp.copy())
#                 return
#
#             # 如果递归中发现 left<candidates[i]，由于后面的数字只会更大，所以无法把 left 减小到 0，可以直接返回
#             if i == len(candidates) or left < candidates[i]:
#                 return
#
#             # 不选
#             dfs(i + 1, left)
#
#             # 选
#             tmp.append(candidates[i])
#             dfs(i, left - candidates[i])
#             tmp.pop()  # 恢复现场
#
#         dfs(0, target)
#
#         return path


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        def dfs(candidates, target, begin, path, res)->None:
            """
            由于题目中说，每个元素可以重复，考虑所有候选数，所以导致了重复。
            可不可以在搜索的时候就去重呢？答案是可以的。
            遇到这一类相同元素不计算顺序的问题，我们在搜索的时候就需要按某种顺序搜索。
            具体的做法是：
            每一次搜索的时候设置 下一轮搜索的起点 begin
            """
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, len(candidates)):
                dfs(candidates, target - candidates[index], index, path + [candidates[index]], res)

        candidates.sort()

        path = []
        res = []
        dfs(candidates, target, 0, path, res)

        return res


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print("测试用例1输入candidates1 = {}, target1 = {}:".format(candidates1, target1))
    print("测试用例1输出:", solution.combinationSum(candidates1, target1))
    # 预期输出: [[2,2,3],[7]]


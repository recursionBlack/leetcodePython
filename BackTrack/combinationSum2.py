from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        def dfs(candidates, target, begin, tmp, path) -> None:
            """
            该题其实比39题简单，应该先做这个再做39题的
            """
            if target == 0:
                path.append(tmp[:])
                return

            for index in range(begin, len(candidates)):
                if target < candidates[index]:
                    break

                # 去重
                if index > begin and candidates[index] == candidates[index - 1]:
                    continue
                tmp.append(candidates[index])
                dfs(candidates, target - candidates[index], index + 1, tmp, path)
                tmp.pop()

        candidates.sort()
        path = []
        dfs(candidates, target, 0, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print("测试用例1输入candidates1 = {}, target1 = {}:".format(candidates1, target1))
    print("测试用例1输出:", solution.combinationSum2(candidates1, target1))
    # 预期输出: [[1,1,6], [1,2,5], [1,7], [2,6]]



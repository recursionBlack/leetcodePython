from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(k: int, n: int, startIndex: int, tmp: List[int], path: List[List[int]]):
            if n == 0 and k == 0:
                path.append(tmp[:])
                return

            for i in range(startIndex, 10):
                if i > n:
                    break
                tmp.append(i)
                dfs(k - 1, n - i, i + 1, tmp, path)
                tmp.pop()

        path = []
        dfs(k, n, 1, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    k1 = 3
    n1 = 7
    print("测试用例1输入k1 = {}, n1 = {}:".format(k1, n1))
    print("测试用例1输出:", solution.combinationSum3(k1, n1))
    # 预期输出: [[1,2,4]]
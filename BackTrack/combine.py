from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(n: int, k: int, begin: int, tmp: List[int], path: List[List[int]]):
            if k == 0:
                path.append(tmp[:])
                return
            # 剩余待选数字不足了，直接返回，
            if n + 1 - begin < k:
                return

            for i in range(begin, n + 1):
                tmp.append(i)
                dfs(n, k - 1, i + 1, tmp, path)
                tmp.pop()

        path = []
        dfs(n, k, 1, [], path)

        return path

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    n1 = 4
    k1 = 2
    print("测试用例1输入n1 = {}, k1 = {}:".format(n1, k1))
    print("测试用例1输出:", solution.combine(n1, k1))
    # 预期输出: [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4],]
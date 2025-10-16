from typing import List

# 839. 相似字符串组
class Solution:
    def build(self, size: int):
        self.MAXN = 301
        self.father = list(range(size))
        self.sets = size
        for i in range(size):
            self.father[i] = i

    def find(self, i: int):
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, x: int, y: int):
        fx = self.father[x]
        fy = self.father[y]
        if fx != fy:
            self.father[fx] = fy
            self.sets -= 1

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        self.build(n)

        for i in range(n):
            for j in range(i+1, n):
                if self.find(i) != self.find(j):
                    diff = 0
                    for k in range(m):
                        if diff > 2:
                            break
                        if strs[i][k] != strs[j][k]:
                            diff += 1

                    if diff == 0 or diff == 2:
                        self.union(i, j)

        return self.sets


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    strs = ["tars","rats","arts","star"]
    print("测试用例1输入 = {}:".format(strs))
    print("测试用例1输出:", solution.numSimilarGroups(strs))
    # 预期输出:2

    # 测试用例1：基础案例
    strs = ["omv","ovm"]
    print("测试用例1输入 = {}:".format(strs))
    print("测试用例1输出:", solution.numSimilarGroups(strs))
    # 预期输出:1
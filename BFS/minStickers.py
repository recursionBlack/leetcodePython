from typing import List
from collections import deque
from collections import defaultdict
from collections import Counter

# 691. 贴纸拼词
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        visited = set()
        # key是26个字母，如果一个单词中含有该字母，则将该单词放到该字母的val里
        graph = defaultdict(set)

        # 遍历所有贴纸
        for s in stickers:
            # 按照从小到大排序，再拼成字符串
            for i, c in enumerate(s):
                graph[c].add(s)

        target = "".join(sorted(target))

        def next(src: str, substrict: str) -> str:
            scnt = Counter(src)
            subCnt = Counter(substrict)
            res = ""
            for key, val in scnt.items():
                time = max(0, val-subCnt[key])
                res += key * time

            return res

        l, r = 0, 0
        visited.add(target)
        queue = deque()
        queue.append(target)
        r += 1
        level = 1
        while l < r:
            size = r - l
            for i in range(size):
                cur = queue.popleft()
                l += 1
                for word in graph[cur[0]]:
                    nt = next(cur, word)
                    if not len(nt):
                        return level
                    elif nt not in visited:
                        visited.add(nt)
                        queue.append(nt)
                        r += 1
            level += 1

        return -1

"""
该题是一个困难题，最大的难点在于，如何看出来，这个题，可以用宽度优先搜索？？？
什么是路径？以及，如何剪枝？（使用排序，并且逐字母来去除）
已访问的又是什么？等等，其实还是非常的难想到的
而且，即使想出来使用bfs算法了，不会剪枝，不知道如何优化，同样会难以做出来。
最后，即使也知道如何剪枝了，BFS的代码量依然很大。
"""

if __name__ == "__main__":
    solution = Solution()

    # 测试用例
    stickers = ["with", "example", "science"]
    target = "thehat"
    print("parameters ={}, ={},:".format(stickers, target))
    print(solution.minStickers(stickers, target))
    # 输出：3

    # 测试用例
    stickers = ["notice","possible"]
    target = "basicbasic"
    print("parameters ={}, ={},:".format(stickers, target))
    print(solution.minStickers(stickers, target))
    # 输出：-1
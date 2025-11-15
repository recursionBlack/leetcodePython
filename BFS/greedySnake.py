"""
贪吃蛇问题，华为od笔试中，遇到的第一道大题
给一个二维的矩阵，矩阵的每一个元素都是一个字符，再给一个字符串，
现在有一条贪吃蛇，要按照字符串的顺序，在矩阵中移动，贪吃蛇不能穿过自己的身体，
另外，地图边缘与另一边是相连的，比如说，蛇从最下一行面进去，可以从最上一行出来。
问贪吃蛇，能否在矩阵中走出这个字符串？如果同时有好几个能走出的结果，请返回最靠近左上角的结果
返回的答案，为每个字符的坐标，若无法形成结果，则返回[[-1,-1]]

a s e r t
w d g t u
r y u n p
z n c s g
x u e d k
比如，如上目标矩阵，请返回是否可以连成字符串： “ gtnscn”
答案为 [[1,2],[1,3],[2,3],[3,3],[3,2],[3,1]]

"""
from typing import List

class Solution:
    def solve(self, matrix: List[List[int]], target: str):
        if not matrix or not matrix[0] or not target:
            return [[-1, -1]]

        rows = len(matrix)
        cols = len(matrix[0])
        target_len = len(target)

        # 找到所有起点（与target[0]匹配，按行优先、列优先排序）
        starts = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target[0]:
                    starts.append((i, j))

        if not starts:
            return [[-1, -1]]

        # 方向：上、下、左、右（按此顺序保证优先级）
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 对每个起点BFS
        for start_i, start_j in starts:
            # 初始状态：路径为[(start_i, start_j)], 已匹配长度1
            from collections import deque
            queue = deque()
            initial_path = [(start_i, start_j)]
            queue.append((start_i, start_j, initial_path, 1))
            # 记录已访问状态：(当前位置, 蛇身frozenset) 避免重复
            visited = set()
            body_set = frozenset(initial_path)
            visited.add((start_i, start_j, body_set))

            while queue:
                i, j, path, step = queue.popleft()

                # 若已匹配完所有字符，返回路径
                if step == target_len:
                    return [list(pos) for pos in path]

                # 探索四个方向（按优先级顺序）
                for di, dj in directions:
                    # 计算循环后的新坐标
                    new_i = (i + di) % rows
                    new_j = (j + dj) % cols

                    # 检查下一个字符是否匹配
                    if matrix[new_i][new_j] != target[step]:
                        continue

                    # 检查新位置是否与蛇身重叠
                    if (new_i, new_j) in path:
                        continue

                    # 生成新路径和新蛇身
                    new_path = path.copy()
                    new_path.append((new_i, new_j))
                    new_body_set = frozenset(new_path)
                    new_state = (new_i, new_j, new_body_set)

                    # 若未访问过，加入队列
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_i, new_j, new_path, step + 1))

        # 无有效路径
        return [[-1, -1]]


if __name__ == "__main__":
    solution = Solution()
    # 测试用例
    matrix = [
        ['a', 's', 'e', 'r', 't'],
        ['w', 'd', 'g', 't', 'u'],
        ['r', 'y', 'u', 'n', 'p'],
        ['z', 'n', 'c', 's', 'g'],
        ['x', 'u', 'e', 'd', 'k']
    ]
    target = "gtnscn"
    print(solution.solve(matrix, target))
    # 输出：[[1, 2], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1]]


"""
看了豆包给的答案，感觉依然做不了，用来记录各种状态的变量实在是太多了，
尤其是，一条路径如果走失败了，如何防止再次走这条路径呢？？？BFS算法还是太复杂了。
"""
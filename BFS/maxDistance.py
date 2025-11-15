from typing import List
from collections import deque

# 1162. 地图分析
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # r - l 表示单层的长度
        l, r = 0, 0
        queue = deque()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = []
        for i in range(m):
            raw = [False] * n
            visited.append(raw)

        seas = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    queue.append([i, j])
                    seas += 1
                    r += 1

        if seas == 0 or seas == m*n:
            return -1

        level = 0  # 层数
        # 队列不为空
        while l < r:
            level += 1
            size = r - l    # 单层的大小
            # 遍历队列内，同一层的节点
            for i in range(size):
                x, y = queue.popleft()
                l += 1
                # 遍历四个方向
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    # 下一个待访问的点，1.不可以越界，2.不可以被访问过，
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                        r += 1

        return level - 1


if __name__ == "__main__":
    solution = Solution()

    # 测试用例
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print("={},".format(grid))
    print(solution.maxDistance(grid))
    # 输出：2

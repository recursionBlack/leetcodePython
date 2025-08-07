from typing import List

# 74. 搜索二维矩阵
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ll = []
        for line in matrix:
            ll += line

        left = 0
        right = len(ll) - 1
        while left <= right:
            mid = (left + right) // 2
            if ll[mid] == target:
                return True
            elif ll[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
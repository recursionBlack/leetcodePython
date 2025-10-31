from typing import List
import heapq

# 1792. 最大平均通过率
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        heap = []

        for pas, total in classes:
            # 对该班级再增加一个学生，该班级的通过率的提升幅度
            nextPass = (pas + 1) / (total + 1) - pas / total
            heapq.heappush(heap, (-nextPass, pas, total))

        # 从堆中，取出通过率提升最大的班级，将该天才加到该班里
        # 然后修改该班级的三个数据，重新插入到堆里
        while extraStudents > 0:
            nextPass, pas, total = heap[0]
            heapq.heappop(heap)
            pas += 1
            total += 1
            nextPass = (pas + 1) / (total + 1) - pas / total
            heapq.heappush(heap, (-nextPass, pas, total))
            extraStudents -= 1

        ans = 0
        for _, pas, total in heap:
            ans += pas / total

        ans /= n

        return ans

"""
和组团买票很像，但比之简单的多，对于每个天才学生来说，选择当前，通过率提升最大的班级进入，就能使得最终结果最大化
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    print("测试用例1输入 = {}, = {}:".format(classes, extraStudents))
    print("测试用例1输出:", solution.maxAverageRatio(classes, extraStudents))
    # 预期输出: 0.78333
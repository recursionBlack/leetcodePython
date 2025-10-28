from typing import List
import heapq

# 630. 课程表 III
class Solution:
    @classmethod
    def sort_by_first_element(cls, lst: List[List[int]]):
        # 使用sorted函数，key指定为每行的第1个元素
        return sorted(lst, key=lambda x: x[1])

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = self.sort_by_first_element(courses)
        time = 0
        heap = []
        for val, end in courses:
            if time + val <= end:
                heapq.heappush(heap, -val)
                time += val
            elif heap and -heap[0] > val:
                time += heapq.heappop(heap)
                heapq.heappush(heap, -val)
                time += val

        return len(heap)


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # # 测试用例1：基础案例
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print("测试用例1输入 = {}:".format(courses))
    print("测试用例1输出:", solution.scheduleCourse(courses))
    # 预期输出:3

    # # 测试用例1：基础案例
    courses = [[3,2],[4,3]]
    print("测试用例1输入 = {}:".format(courses))
    print("测试用例1输出:", solution.scheduleCourse(courses))
    # 预期输出:0

    # # 测试用例1：基础案例
    courses = [[2, 5], [2, 19], [1, 8], [1, 3]]
    print("测试用例1输入 = {}:".format(courses))
    print("测试用例1输出:", solution.scheduleCourse(courses))
    # 预期输出:4
from typing import List
import heapq

# 630. 课程表 III
class Solution:
    @classmethod
    def sort_by_first_element(cls, lst: List[List[int]]):
        # 使用sorted函数，key指定为每行的第1个元素
        return sorted(lst, key=lambda x: x[1])

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 根据课程结束时间先进行排序
        courses = self.sort_by_first_element(courses)
        time = 0    # 累计修课用的时间
        # 用一个大根堆，来维护
        heap = []
        # 对于每一门课程，如果该课程的花费时间，加上当前其他课程的结束时间，小于课程的结束时间
        # 则将该门课加进time里，并将该课程的花费时间，存到大根堆里维护
        # 如果该课程时间超了，但大根堆里，有别的课程，耗时代价较大，则将该耗时较大的课程踢出
        # 将当前课程加进来
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
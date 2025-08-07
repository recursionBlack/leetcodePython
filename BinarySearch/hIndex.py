from typing import List

# 275. H 指数 II
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 1
        right = len(citations)
        while left <= right:
            # 循环不变量：
            # left-1 的回答一定为「是」
            # right+1 的回答一定为「否」
            mid = (left + right) // 2
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                left = mid + 1
            else:
                right = mid - 1

        # 循环结束后 right 等于 left-1，回答一定为「是」
        # 根据循环不变量，right 现在是最大的回答为「是」的数
        return right

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    # citations = [0,1,3,5,6]
    # print("测试用例1输入citations = {}:".format(citations))
    # print("测试用例1输出:", solution.hIndex(citations))
    # # 预期输出: True

    # 测试用例1：基础案例
    citations = [100]
    print("测试用例1输入citations = {}:".format(citations))
    print("测试用例1输出:", solution.hIndex(citations))
    # 预期输出: 1
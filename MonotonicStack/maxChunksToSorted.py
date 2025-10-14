from typing import List

# 769. 最多能完成排序的块
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        monoStack = []
        for num in arr:
            if not monoStack or monoStack[-1] < num:
                monoStack.append(num)
            else:
                # 说明栈顶元素是大于 num 的，此时说明这两个元素属于同一个分块，
                # 如果接下来栈中还有大于 num 的元素，说明这些元素跟栈顶元素也属于同一个分块，
                # 我们只保存每个分块的最大值，也即是 mx，同一分块的其他元素要弹出。
                mx = monoStack.pop()
                while monoStack and num < monoStack[-1]:
                    monoStack.pop()
                monoStack.append(mx)

        return len(monoStack)


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    arr = [4,3,2,1,0]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.maxChunksToSorted(arr))
    # 预期输出:1

    # 测试用例1：基础案例
    arr = [1,0,2,3,4]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.maxChunksToSorted(arr))
    # 预期输出:4
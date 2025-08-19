from typing import List

# 1130. 叶值的最小代价生成树
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        monoStack = []
        ans = 0

        for i in range(n):
            while monoStack and arr[i] > arr[monoStack[-1]]:
                cur = monoStack[-1]
                monoStack.pop()
                left = monoStack[-1] if monoStack else -1
                if monoStack:
                    ans += arr[cur] * min(arr[left], arr[i])
                else:
                    ans += arr[cur] * arr[i]
            monoStack.append(i)

        while monoStack:
            cur = monoStack[-1]
            monoStack.pop()
            left = monoStack[-1] if monoStack else -1
            if monoStack:
                ans += arr[cur] * arr[left]

        return ans


"""
首先，想让 mct 值最小，那么值较小的叶子节点就要尽量放到底部，值较大的叶子节点要尽量放到靠上的部分。
因为越是底部的叶子节点，被用来做乘法的次数越多。这就决定了我们有必要去寻找一个极小值。
通过维护一个单调递减栈就可以找到一个极小值，因为既然是单调递减栈，左侧节点一定大于栈顶节点，
而当前节点（右侧）也大于栈顶节点（因为当前节点小于栈顶的话，就被直接入栈了）。
然后找到这个极小值后，就需要左右看看，左边和右边哪个值更小，因为我们的目的是把较小的值尽量放到底部。
还有一点，构造出来的二叉树一定是形如下面图一的样子，比如 [6,2,3,4] 构成的二叉树：
图一 (最小 mct 一定形如以下的样子)：
mct: 24 + 12 + 6 = 42
"""

"""
单调栈的本质，是贪心，所以，贪心问题，可以用单调栈来解。
这个问题，难点在于，想清楚，为啥可以用递减的单调栈来解？？？
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    arr = [6,2,4]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.mctFromLeafValues(arr))
    # 预期输出:32

    # 测试用例1：基础案例
    arr = [4,11]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.mctFromLeafValues(arr))
    # 预期输出:44
from typing import List

# 907. 子数组的最小值之和
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(arr)
        monoStack = []
        left = [0] * n
        right = [0] * n
        for i, x in enumerate(arr):
            while monoStack and x <= arr[monoStack[-1]]:    # 栈内大压小
                monoStack.pop()
            left[i] = i - (monoStack[-1] if monoStack else -1)  # 记录下，当前元素左侧第一个较小值的位置
            monoStack.append(i)
        monoStack = []
        for i in range(n - 1, -1, -1):
            while monoStack and arr[i] < arr[monoStack[-1]]:    # 栈内大压小
                monoStack.pop()
            right[i] = (monoStack[-1] if monoStack else n) - i  # 记录下，当前元素右侧第一个较小值的位置
            monoStack.append(i)

        ans = 0
        for l, r, x in zip(left, right, arr):
            ans = (ans + l * r * x) % MOD
        return ans

"""
上述即转化为经典的单调栈问题，即求数组中当前元素  左边第一个小于当前元素的的元素以及右边第一个小于等于当前元素的元素
这句话，才是把题意转为单调栈的原因.该问题的难点，就在于，为啥可以转成单调栈了？
对每个数，算出它是哪些子数组的最小值。
分别向左右两侧，找到第一个最近的，比他更小的位置，那么，以(left,right)两边都是开区间，就是以当前值为最小值的范围了。

另外注意到，这道题，并不太好套用左神的模板，看来，左神的做题模板，也是不完全适用于各种情况的呦。单调栈还是一个，需要很深度的思考
而不是一种无脑套模板的题型啊
"""


if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    arr = [3,1,2,4]
    print("测试用例1输入 = {}:".format(arr))
    print("测试用例1输出:", solution.sumSubarrayMins(arr))
    # 预期输出: 17。最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
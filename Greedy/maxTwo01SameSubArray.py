"""
两个0和1相等区间的最大长度
给出一个长度为n的01串，现在请你找到两个区间
使得两个区间中，1的个数相等，0的个数也相等，
这两个区间可以相交，但不可以完全重叠，即两个区间的左右端点不可以完全一样，
现在请你找到两个最长区间，满足以上条件，返回区间最大长度

来自真实大厂笔试，没有在线测试，对数器验证
"""
from typing import List


class Solution:
    def maxTwo01SameSubArray(self, arr: List[int]) -> int:
        leftZero, rightZero = -1, -1
        leftOne, rightOne = -1, -1
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                leftZero = i
                break
        for i in range(n):
            if arr[i] == 1:
                leftOne = i
                break
        for i in range(n-1, -1, -1):
            if arr[i] == 0:
                rightZero = i
                break
        for i in range(n - 1, -1, -1):
            if arr[i] == 1:
                rightOne = i
                break

        ans0 = rightZero - leftZero
        ans1 = rightOne - leftOne

        return max(ans0, ans1)

"""
对于一个数组，其最大的长度，分别是，最左侧的1和最右侧的1的位置，左边的区间从最左侧的1到最右侧的1，左闭右开，
右边的区间则是不包含最左侧的1，在其后一位，直到最右侧的1，这两个区间的0和1的数量一定是相等的。
另一种情况，则是最左侧的0和最右侧的0，也是和1类似的
最终，这两个区间比较大小，返回较大的那个区间
非常需要灵感。
"""
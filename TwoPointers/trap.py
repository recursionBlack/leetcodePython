from typing import List

# 42. 接雨水
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         # 前缀最大值容器
#         pre_max = [0] * n
#         pre_max[0] = height[0]
#         for i in range(1, n):
#             pre_max[i] = max(pre_max[i-1], height[i])
#
#         # 后缀最大值容器
#         suf_max = [0] * n
#         suf_max [-1] = height[-1]
#         for i in range(n-2, -1, -1):
#             suf_max[i] = max(suf_max[i+1], height[i])
#
#         ans = 0
#         # 三个容器一块遍历
#         for h, pr, su in zip(height, pre_max, suf_max):
#             ans += min(pr, su) - h
#
#         return ans

"""
该方法，时间复杂度仅为O(n),但空间复杂度也是O(n)
由于这个问题太经典了，耳熟能详，臭名昭著，所以另一种解法也要学习
因为，如果只需要做题的话，掌握第一种方法就行了，
但面试可能会问到，所以第二种方法也要掌握
"""


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         left = 0
#         right = n - 1
#         # 用变量代替了原来，要用容器记录的前缀最大值
#         pre_max = height[left]
#         suf_max = height[right]
#         ans = 0
#
#         while left < right:
#             pre_max = max(pre_max, height[left])
#             suf_max = max(suf_max, height[right])
#             # 每次使两者中更低的向中间移动
#             if pre_max < suf_max:
#                 ans += pre_max - height[left]
#                 left += 1
#             else:
#                 ans += suf_max - height[right]
#                 right -= 1
#
#         return ans


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                # 如果栈已经空了
                if not st:
                    break
                # 栈顶已经被弹出过一次了，这里其实是栈顶元素左侧的桶高，
                # 所以才必须先检验栈是否已经空了
                left = st[-1]
                # 高度差，桶的左侧边缘和右侧边缘中，较低的，然后减去栈顶高度
                dh = min(height[left], h) - bottom_h
                # 面积 = 高度差 * 横向差
                ans += dh * (i - left - 1)
            st.append(i)

        return ans


"""
单调栈做法，相比于双指针，双指针是竖着计算每一个桶的容量，
而单调栈则是基于横向做的.每次计算面积时，需要三个元素：
当前的列（桶的右半边），栈顶（桶底高度），栈顶左侧（桶的左半边）

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("测试用例1输入 height = {}: ".format(height))
    print("测试用例1输出:", solution.trap(height))
    # 预期输出: 6

    # 测试用例1：基础案例
    height = [4,2,0,3,2,5]
    print("测试用例1输入 height = {}: ".format(height))
    print("测试用例1输出:", solution.trap(height))
    # 预期输出: 9
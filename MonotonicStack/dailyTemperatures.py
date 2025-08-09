from typing import List

# 739. 每日温度（单调栈系列第一题）
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = [] # 要维护的栈，存储的是第i日
        # 逆序遍历
        for i in range(n-1, -1, -1):
            # 第i天的温度
           t = temperatures[i]
           # 如果大于栈顶元素，
           while st and t >= temperatures[st[-1]]:
               st.pop()         # 数据没用了，直接丢弃掉
           if st:
                ans[i] = st[-1] - i
           st.append(i)

        return ans

"""
本题为单调栈，开宗立派第一题，根据b站灵茶山艾府的教学学习，开始理解单调栈

"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    temperatures = [73,74,75,71,69,72,76,73]
    print("测试用例1输入temperatures = {}:".format(temperatures))
    print("测试用例1输出:", solution.dailyTemperatures(temperatures))
    # 预期输出: [1,1,4,2,1,1,0,0]
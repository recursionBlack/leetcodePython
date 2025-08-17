from typing import List

# 853. 车队
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0] * n
        for i, [pos, sp] in enumerate(sorted(zip(position, speed))):  # 按pos升序
            time[i] = (target - pos) / sp

        st = []
        for t in time:
            while st and t >= st[-1]:
                st.pop()
            st.append(t)
        return len(st)

"""
这个问题，难点在于，需要将两个列表压缩成一个后，在进行排序，此时，计算出来的time才可以进行单调栈
直接想用单调栈是很难看出来的
"""

if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()

    # 测试用例1：基础案例
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print("测试用例1输入 = {}, = {}, = {}:".format(target, position, speed))
    print("测试用例1输出:", solution.carFleet(target, position, speed))
    # 预期输出: 3
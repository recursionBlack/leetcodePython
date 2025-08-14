from myLeetcodeUtils import RandomSelect

if __name__ == "__main__":
    # 创建Solution实例
    solution = RandomSelect([1, 3])

    # 测试用例1：基础案例
    print("测试用例1输出:", solution.pickIndex())
    # 预期输出: 0的概率为25%，1的概率为75%
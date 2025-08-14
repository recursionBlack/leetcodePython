from myLeetcodeUtils import RectsRandomPoint

if __name__ == "__main__":
    # 创建Solution实例
    solution = RectsRandomPoint([[-2,-2,1,1],[2,2,4,6]])

    # 测试用例1：基础案例
    print("测试用例1输出:", solution.pick())
    # 预期输出: 0的概率为25%，1的概率为75%
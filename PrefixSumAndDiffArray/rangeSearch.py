from myLeetcodeUtils import NumArray

if __name__ == "__main__":
    # 创建Solution实例
    solution = NumArray([-2,0,3,-5,2,-1])

    # 测试用例1：基础案例
    rag = [0,2]
    print("测试用例1输入rag = {}:".format(rag))
    print("测试用例1输出:", solution.sumRange(rag[0], rag[1]))
    # 预期输出: 1

    # 测试用例1：基础案例
    rag = [2,5]
    print("测试用例1输入rag = {}:".format(rag))
    print("测试用例1输出:", solution.sumRange(rag[0], rag[1]))
    # 预期输出: -1

    # 测试用例1：基础案例
    rag = [0,5]
    print("测试用例1输入rag = {}:".format(rag))
    print("测试用例1输出:", solution.sumRange(rag[0], rag[1]))
    # 预期输出: -3

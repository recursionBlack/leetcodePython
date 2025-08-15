from myLeetcodeUtils import MyCircularQueue

if __name__ == "__main__":
    circularQueue = MyCircularQueue(3)  # 设置长度为 3

    print(circularQueue.enQueue(1))    # 返回 true
    print(circularQueue.enQueue(2))    # 返回 true
    print(circularQueue.enQueue(3))    # 返回 true
    print(circularQueue.enQueue(4))    # 返回 false，队列已满
    print(circularQueue.Rear())        # 返回 3
    print(circularQueue.isFull())      # 返回 true
    print(circularQueue.deQueue())     # 返回 true
    print(circularQueue.enQueue(4))    # 返回 true
    print(circularQueue.Rear())        # 返回 4
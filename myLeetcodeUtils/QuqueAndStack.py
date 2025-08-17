
# 手撕队列
class Queue2:
    # n是加入操作的总次数是多少，一定要明确
    # 一般笔试，面试，都会给一个明确的数据量(最大追加次数n)，这是最常用的方式
    def  __init__(self, n: int):
        self.queue = [0] * n
        self.l = 0
        self.r = 0

    # 调用任何方法之前，先调用这个方法来判断队列中是否有东西
    def isEmpty(self) -> bool:
        return self.l == self.r

    # 尾部指针指向尾部元素的下一个下标，即尾部指针指向的实际为空，左闭右开
    def append(self, num: int):
        self.queue[self.r] = num
        self.r += 1

    def pop(self) -> int:
        res = self.queue[self.l]
        self.l += 1
        return res

    def head(self) -> int:
        return self.queue[self.l]

    def tail(self) -> int:
        return self.queue[self.r - 1]

    def size(self) -> int:
        return self.r - self.l


# 手撕栈
class Stack2:
    # 通常会提供，栈内最大容量n
    # 一般笔试，面试，都会给一个明确的数据量(栈内最大容量n)，这是最常用的方式
    def __init__(self, n: int):
        self.stack = [0] * n
        self.size = 0       # size 指针也是指向下一个元素的位置，栈顶元素的上面，指向的位置不属于栈内合法空间

    # 调用任何方法之前，先调用这个方法来判断队列中是否有东西
    def isEmpty(self) -> bool:
        return self.size == 0

    def push(self, num: int):
        self.stack[self.size] = num
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack[self.size]

    # 只返回栈顶元素，不移动栈顶指针，有的语言也叫peek
    def top(self) -> int:
        return self.stack[self.size - 1]

    def size(self) -> int:
        return self.size


# 622. 设计循环队列
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.l = 0
        self.r = 0
        self.size = 0       # 重点在于该变量的设置
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.r] = value
            self.r = 0 if (self.r == self.limit - 1) else self.r + 1
            self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            value = self.queue[self.l]
            self.l = 0 if (self.l == self.limit - 1) else self.l + 1
            self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
             return self.queue[self.l]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            last = self.limit - 1 if self.r == 0 else self.r - 1
            return self.queue[last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# 901. 股票价格跨度
class StockSpanner:

    def __init__(self):
        self.log = []
        self.span = []
        self.monoStack = []
        self.size = 0

    def next(self, price: int) -> int:

        if not self.log:
            self.log.append(price)
            self.span.append(1)
            self.monoStack.append(0)
            self.size = 1
            return self.span[-1]

        newkua = 1
        while self.monoStack and price >= self.log[self.monoStack[-1]]:
            cur = self.monoStack[-1]
            self.monoStack.pop()
            newkua += self.span[cur]

        self.log.append(price)
        self.span.append(newkua)
        self.monoStack.append(self.size)
        self.size += 1

        return self.span[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
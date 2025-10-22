from typing import List

class HeapSort:
    def swap(self, arr: List[int], i: int, j: int):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    # i位置的数，向上调整大根堆
    # arr[i] = x， x是新来的，需要一直跟父节点比大小，
    # 如果比父节点大，则与父节点交换，直到不比父节点大，或者来带0位置（顶）
    def heapInsert(self, arr: List[int], i: int):
        while arr[i] > arr[(i-1) // 2]:
            self.swap(arr, i, (i-1) // 2)
            i = (i-1) // 2

    # i位置的数，突然变小了，又想继续维持大根堆结构，
    # 向下调整大根堆
    # 当前根堆的大小为size
    def heapify(self, arr: List[int], i: int, size: int):
        l = i * 2 + 1
        while l < size:
            # 有左孩子，右孩子为l+1，评选那个孩子是最强孩子
            best = -1
            if l + 1 < size:
                beat = l+1 if arr[l+1] > arr[l] else l
            # 再将最强孩子与当前节点比大小，取较大者
            best = best if arr[best] > arr[i] else i
            # 当前节点已经比最强孩子还大了，就停止，不再向下换了
            if best == i:
                break
            self.swap(arr, best, i)
            i = best
            l = i * 2 + 1


    ### 两种堆排序，一种从上往下，建立堆结构，一种从下往上，建立堆结构
    # 方式1，从顶到底建立大根堆，O（n * log n)
    # 依次弹出最大值并排好序
    # 整体时间复杂度O（n * log n）
    def heapSort1(self, arr: List[int]):
        n = len(arr)
        # 建立大根堆
        for i in range(n):
            self.heapInsert(arr, i)

        size = n
        while size > 1:
            # 将最大的值，移到尾部，并缩小size，使得已经排好序的最大值
            # 不再参与堆调整
            self.swap(arr, 0, size)
            size -= 1
            self.heapify(arr, 0, size)


    # 方式2，从底到顶，建立大根堆，O（n）
    # 依次弹出堆内最大值，并排好序，O（n * log n)
    # 整体时间复杂度O（n * log n)
    def heapSort2(self, arr: List[int]):
        n = len(arr)
        for i in range(n - 1, 0, -1):
            self.heapify(arr, i, n)
        size = n
        while size > 1:
            self.swap(arr, 0, size)
            size -= 1
            self.heapify(arr, 0, size)
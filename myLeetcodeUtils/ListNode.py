from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_to_linked_list(self, lst: List[int]):
        """
        将列表转换为链表
        参数: lst: 输入的列表
        返回:链表的头节点
        """
        # 处理空列表情况
        if not lst:
            return None

        # 创建头节点
        head = ListNode(lst[0])
        current = head

        # 遍历列表剩余元素，创建节点并链接
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next

        return head
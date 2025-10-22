from typing import List
from collections import deque

# Definition for singly-linked list.
# leetcode中的常见自定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list_to_linked_list(cls, lst: List[int]):
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

# Definition for a binary tree node.
# leetcode中的常见自定义二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order_with_null(root):
        """层序遍历，只包含必要的null，完全匹配预期结果"""
        if not root:
            return []

        result = []
        queue = deque([root])
        last_non_null_index = 0  # 记录最后一个非空节点的位置

        while queue:
            node = queue.popleft()

            if node:
                # 添加当前节点值
                result.append(node.val)
                last_non_null_index = len(result) - 1  # 更新最后非空节点位置

                # 只对非空节点添加其子节点（无论子节点是否为空）
                queue.append(node.left)
                queue.append(node.right)
            else:
                # 空节点添加None，但不再为其添加子节点
                result.append(None)

        # 截断到最后一个非空节点
        return result[:last_non_null_index + 1]
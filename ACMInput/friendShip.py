import sys
from typing import List
from collections import defaultdict

"""
小美认为，在人际交往中，但是随着时间的流逝，朋友的关系也是会慢慢变淡的，最终朋友关系就淡忘了。
现在初始有一些朋友关系，存在一些事件会导致两个人淡忘了他们的朋友关系。小美想知道某一时刻中，某两人是否可以通过朋友介绍互相认识？
事件共有 2 种：
1 u v：代表编号 u 的人和编号 v 的人淡忘了他们的朋友关系。
2 u v：代表小美查询编号 u 的人和编号 v 的人是否能通过朋友介绍互相认识。

注：介绍可以有多层，比如 2 号把 1 号介绍给 3 号，然后 3 号再把 1 号介绍给 4 号，这样 1 号和 4 号就认识了。

"""

class Solution:
    def solve(self, num: int, shipArray: List[List[int]], opArray: List[List[int]]) -> List[bool]:
        shipDict = defaultdict(list)

        for l, r in shipArray:
            shipDict[l].append(r)
            shipDict[r].append(l)

        # 获取某个人的所有朋友返回到一个List里
        def getAllFriendOfOne2(l: int, friends: List[int]):
            if l not in friends:
                friends.append(l)
            for i in shipDict[l]:
                if i not in friends:
                    friends.append(i)
                    getAllFriendOfOne(i, friends)

        def getAllFriendOfOne(l: int, friends: List[int]) -> None:
            if not friends:  # 确保列表初始为空（避免重复处理）
                friends.clear()

            stack = [l]  # 栈初始化，放入起始节点
            visited = set(friends)  # 用集合记录已处理的节点（加速判断）

            while stack:
                current = stack.pop()  # 弹出栈顶节点（最后加入的节点，模拟递归深度优先）
                if current not in visited:
                    friends.append(current)  # 加入结果列表
                    visited.add(current)  # 标记为已处理
                    # 将当前节点的相邻节点压入栈（注意：逆序压入可保持与递归相同的遍历顺序，不逆序也不影响结果）
                    for neighbor in reversed(shipDict.get(current, [])):
                        if neighbor not in visited:
                            stack.append(neighbor)

        res = []
        for op, l, r in opArray:
            if op == 1:
                if r in shipDict[l]:
                    shipDict[l].remove(r)
                    shipDict[r].remove(l)

            elif op == 2:
                y = []
                getAllFriendOfOne(l, y)
                res.append(r in y)

        return res

if __name__ == "__main__":
    solution = Solution()

    """
5 3 5
1 2
2 3
4 5
1 1 5
2 1 3
2 1 4
1 1 2
2 1 3

    """

    first_line = sys.stdin.readline().strip()
    data1 = list(map(int, first_line.split()))

    shipArray = []
    for _ in range(data1[1]):
        ship_line = sys.stdin.readline().strip()
        data2 = list(map(int, ship_line.split()))
        shipArray.append(data2)

    opArray = []
    for _ in range(data1[2]):
        op_line = sys.stdin.readline().strip()
        data3 = list(map(int, op_line.split()))
        opArray.append(data3)

    res = solution.solve(data1[0], shipArray, opArray)
    for b in res:
        if b:
            print("Yes")
        else:
            print("No")


"""
最终即使用栈代替递归，也超时了，在数据量极大的时候。
因为看着，像是用并查集，但由于增加了删减操作，导致每次删减后，并查集都要重新生成，而并查集仅支持合并和查询
并不支持删减，而且，如果数据特别大的话，每次修改后重新生成并查集都会特别大，内存和时间消耗都非常的大。

最终，只通过了3个测例，第3个例子的数据量过大， 超时了。

看了答案，确实是用的并查集解的，因为太明显了，但删除连接关系同样让大佬们也头疼，
他们采取了，逆序添加，因为每次的操作1，都是删除连接关系，那直接，先把所有的删除操作给做了，从后往前倒推，
这样每次的删除操作就变成了添加，这样并查集就会变成越来越大的样子了，
不过，最终的输出结果也变成倒序的了，再倒回来就是正确结果了

由于并查集仅支持插入关系而不能删除已有的关系，因此要进行“删除”的话得反向思考。
先遍历所有关系和事件，提取出所有事件结果后仍保持的关系，将它们加入并查集中。
然后逆序遍历事件，正序时遇到的“删除”事件相当于逆序下的“添加”，
因此碰到删除时进行添加操作即可。

作者：zeroize
链接：https://www.nowcoder.com/exam/test/93462536/submission?examPageSource=
Company&pid=55750560&testCallback=https%3A%2F%2Fwww.nowcoder.com%
2Fexam%2Fcompany%3FquestionJobId%3D10%26subTabName%3Dwritten_page&
testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91
来源：牛客网

"""
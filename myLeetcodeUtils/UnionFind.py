class UnionFind:
    """
    并查集（Union-Find）数据结构实现

    支持两种主要操作：
    1. find: 查找元素所在集合的根节点
    2. union: 合并两个元素所在的集合

    实现了路径压缩和按秩合并两种优化，以提高操作效率

    做并查集问题时，可能需要手撕，必须记住该类的两个方法的实现。
    不过这个模板写的不太好，最好还是看另外三个的题解。那里面有个sets属性，非常的重要，
    这里没法加进来。
    """

    def __init__(self, size):
        """
        初始化并查集

        参数:
            size: 元素的数量，元素编号从0到size-1
        """
        # parent数组记录每个元素的父节点
        self.parent = list(range(size))
        # rank数组用于按秩合并，记录树的高度
        self.rank = [0] * size
        # 记录每个集合的大小
        self.size = [1] * size

    def find(self, x):
        """
        查找元素x所在集合的根节点

        参数:
            x: 要查找的元素

        返回:
            x所在集合的根节点

        采用路径压缩优化，将查找路径上的所有节点直接指向根节点
        """
        if self.parent[x] != x:
            # 递归查找根节点，并将x的父节点直接设为根节点（路径压缩）
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        """
        合并元素x和元素y所在的集合

        参数:
            x: 第一个元素
            y: 第二个元素

        返回:
            布尔值: 如果两个元素原本不在同一集合则返回True，否则返回False

        采用按秩合并优化，将秩较小的树合并到秩较大的树的根节点下
        """
        # 查找x和y的根节点
        root_x = self.find(x)
        root_y = self.find(y)

        # 如果根节点相同，说明已经在同一集合中
        if root_x == root_y:
            return False

        # 按秩合并：将秩较小的树合并到秩较大的树的根节点下
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            # 如果两个树的秩相同，合并后秩加1
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

        return True

    def isSameSet(self, x, y):
        """
        判断元素x和元素y是否在同一集合中

        参数:
            x: 第一个元素
            y: 第二个元素

        返回:
            布尔值: 如果在同一集合中返回True，否则返回False
        """
        return self.find(x) == self.find(y)

    def get_set_size(self, x):
        """
        获取元素x所在集合的大小

        参数:
            x: 要查询的元素

        返回:
            整数: x所在集合的元素数量
        """
        root = self.find(x)
        return self.size[root]


# 示例用法
if __name__ == "__main__":
    # 创建一个包含10个元素的并查集
    uf = UnionFind(10)

    # 合并一些元素
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(4, 5)
    uf.union(0, 3)

    # 检查连通性
    print("0和5是否连通?", uf.isSameSet(0, 5))  # 应该输出True
    print("0和6是否连通?", uf.isSameSet(0, 6))  # 应该输出False

    # 查看集合大小
    print("0所在集合的大小:", uf.get_set_size(0))  # 应该输出6
    print("6所在集合的大小:", uf.get_set_size(6))  # 应该输出1
from typing import List


class UnionFind:
    __slots__ = "father", "size", "sets"

    def __init__(self, n: int):
        self.father: List[int] = list(range(n))
        self.size: List[int] = [1] * n
        self.sets = n

    def find(self, x: int) -> int:
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a: int, b: int) -> bool:
        fa, fb = self.find(a), self.find(b)
        if fa == fb:
            return False
        if self.size[fa] > self.size[fb]:
            self.father[fb] = fa
            self.size[fa] += self.size[fb]
            self.sets -= 1
        else:
            self.father[fa] = fb
            self.size[fb] += self.size[fa]
            self.sets -= 1
        return True

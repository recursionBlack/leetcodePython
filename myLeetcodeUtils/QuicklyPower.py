
# 手动实现快速幂
class QuicklyPower:
    @classmethod
    def power(cls, x: int, n: int, mod: int) -> int:
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = (ans * x) % mod
            x = (x * x) % mod
            n >>= 1

        return ans
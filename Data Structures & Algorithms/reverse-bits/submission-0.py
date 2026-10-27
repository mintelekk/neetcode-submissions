class Solution:
    def reverseBits(self, n: int) -> int:
        n = f"{n:032b}"
        n = n[::-1]
        return int(n, 2)
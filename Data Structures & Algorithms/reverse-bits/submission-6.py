class Solution:
    def reverseBits(self, n: int) -> int:
        r =  1 << 31
        b = bin(n)[2:].zfill(32)
        b = b[::-1]

        return int(b,2)

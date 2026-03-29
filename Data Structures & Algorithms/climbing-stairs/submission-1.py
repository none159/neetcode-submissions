class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        next = 1
        count = 1
        while count < n:
            count+=1
            a,b = b,next
            next = a+b
        return next
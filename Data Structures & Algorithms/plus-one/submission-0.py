class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(n) for n in str(int("".join(str(i) for i in digits)) + 1)]

# My brute force way
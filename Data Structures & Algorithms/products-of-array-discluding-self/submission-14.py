class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        zero_mult = nonzero_mult = 1
        for n in nums:
            if n!=0:
                nonzero_mult *= n
            zero_mult *= n
        
        if nums.count(0) > 1:
            return [0] * len(nums)
        for n in nums:
            if 0 in nums:
                result.append(zero_mult//n if n != 0 else nonzero_mult)
            else:
                result.append(nonzero_mult//n)
        return result

# my other attempt => complexity:o(n^2), space: o(n)

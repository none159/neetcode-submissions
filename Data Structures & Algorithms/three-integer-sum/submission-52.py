class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        j = len(nums) - 1
        k = i + 1
        res = []
        while i < len(nums) - 1:         
            if nums[j] + nums[k] == -nums[i] and [nums[i], nums[j], nums[k]] not in res:
                res.append([nums[i], nums[j], nums[k]])
            elif nums[j] + nums[k] > -nums[i]:
                j -= 1
            else:
                k += 1
            if k >= j:
                i += 1
                k = i + 1
                j = len(nums) - 1
      
        return res

# my solution with the help of the hint , removed a loop to optimize it more
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        j = len(nums) - 1
        k = i + 1
        res = []
        while i < len(nums) - 1:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            k = i + 1
            j = len(nums) - 1
            while k < j:
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i],nums[k], nums[j]])
                    k += 1
                    while nums[k] == nums[k - 1] and k < j:
                        k += 1
                elif nums[j] + nums[k] > -nums[i]:
                    j -= 1
                else:
                    k += 1
            
            i += 1
                
      
        return res

# Last Solution optimized based on the video
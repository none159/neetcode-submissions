class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < len(numbers):
            j = len(numbers) - 1
            while j >= 0:
                if i < j and numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                j -= 1
            i += 1
        return []
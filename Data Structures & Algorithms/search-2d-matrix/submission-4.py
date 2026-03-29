class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            low = 0
            high = len(matrix[i]) - 1
            while True:
                middle = (low+high)//2
                if matrix[i][middle] == target:
                    return True
                elif matrix[i][low:high] == []:
                    break
                if matrix[i][middle] > target:
                    high = middle - 1
                else:
                    low = middle + 1
            i += 1
        return False
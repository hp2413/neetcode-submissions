class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n -1
        while l <= r:
            mid = l + ((r - l)// 2)
            nr = mid // n
            nc = mid % n
            if matrix[nr][nc] == target:
                return True
            elif matrix[nr][nc] < target:
                l = mid + 1
            else:
                r = mid - 1 
        
        return False


        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows*cols
        left = 0
        right = n-1
        while left<=right:
            mid = (left+right)//2
            print(mid//cols, mid%rows)
            midNum = matrix[mid//cols][mid%cols]
            print("MID/MIDNUM", mid, midNum)
            if midNum==target:
                return True
            elif midNum>target:
                right = mid-1
            else:
                left = mid+1
        return False
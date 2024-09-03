class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        i = 0
        j = len(height)-1
        while i<j:            
            if height[i]<height[j]:
                maxA = max((j-i)*height[i], maxA)
                i+=1
            else:
                maxA = max((j-i)*height[j], maxA)
                j-=1
        return maxA
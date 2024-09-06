class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left = 0
        right = len(height)-1
        while left<right:            
            if height[left]<height[right]:
                maxA = max((right-left)*height[left], maxA)
                left+=1
            else:
                maxA = max((right-left)*height[right], maxA)
                right-=1
        return maxA
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            center = (left+right)//2
            if nums[center]==target:
                return center
            elif nums[center]>target:
                right=center-1
            else:
                left=center+1
        return -1
        
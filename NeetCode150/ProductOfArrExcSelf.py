class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = 1
        suff = 1
        n = len(nums)
        ans = [1]*n
        for i in range(n):
            ans[i]*=pref
            pref*=nums[i]
        for j in range(n-1, -1, -1):
            ans[j]*=suff
            suff*=nums[j]
        return ans
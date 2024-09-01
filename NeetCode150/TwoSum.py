class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSum = {}
        for i in range(len(nums)):
            numSum[nums[i]] = i
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in numSum and numSum[complement] != j:
                return [j, numSum[complement]]
        return []
            
        
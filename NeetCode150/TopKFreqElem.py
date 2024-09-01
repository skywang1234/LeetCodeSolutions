class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        ans = []
        for n in nums:
            freq[n]+=1
        freq = dict(sorted(freq.items(), key= lambda x:x[1], reverse=True))
        ans = list(freq.keys())[:k]
        return ans
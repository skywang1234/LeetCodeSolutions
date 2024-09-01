class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda: [])
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return list(groups.values())
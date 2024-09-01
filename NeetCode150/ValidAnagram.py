class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        chars = defaultdict(lambda: 0)
        for i in range(len(s)):
            chars[s[i]]+=1
            chars[t[i]]-=1
        return list(chars.values())==[0]*len(chars)
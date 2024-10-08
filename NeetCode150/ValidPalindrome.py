class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        while left<right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            elif not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
        return True
        
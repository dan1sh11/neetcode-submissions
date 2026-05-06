class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i:i+1] in t:
                    t = t.replace(s[i:i+1], "", 1)
                else:
                    return False
            return True
        return False
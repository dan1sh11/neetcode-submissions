class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for c in s:
            if t == "" or c not in t:
                return False

            t = t.replace(c, "", 1)
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = []
        if len(t) != len(s):
            return False 
        for i in s:
            chars.append(i)
        for i in t:
            if (i not in chars) or t.count(i) != s.count(i):
                return False
            
        return True
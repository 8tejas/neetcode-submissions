class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS, lenT = len(s), len(t)
        if lenS != lenT:
            return False
        sCount, tCount = {}, {}
        for i in range(lenS):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        return sCount == tCount
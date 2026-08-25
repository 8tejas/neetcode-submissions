class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        l = 0
        s1Count = {}
        s2Count = {}
        for i in s1:
            s1Count[i] = s1Count.get(i, 0) + 1
        for r in range(len(s2)):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1
            if r - l + 1 > size:
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1
            if s1Count == s2Count:
                return True
        return False
            
        
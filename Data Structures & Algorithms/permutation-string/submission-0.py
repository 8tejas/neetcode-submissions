class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        target = sorted(s1)
        for r in range(size, len(s2) + 1):
            window = sorted(s2[r-size:r])
            if window == target:
                return True
        return False
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        for i in nums:
            if i not in countDict:
                countDict[i] = 1
            else:
                return True
        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i,n in enumerate(nums):
            numsDict[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in nums and numsDict[diff] != i:
                return[i, numsDict[diff]]
        return[]

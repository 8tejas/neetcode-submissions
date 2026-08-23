class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in numDict:
                return [numDict[diff], i]
            numDict[v] = i

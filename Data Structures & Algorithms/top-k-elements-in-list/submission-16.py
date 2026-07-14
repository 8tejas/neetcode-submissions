class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        if k == len(nums):
            return nums
        for i in nums:
            countNums[i] = countNums.get(i,0) + 1
        top_k = sorted(countNums, key=countNums.get, reverse=True)[:k]
        return top_k
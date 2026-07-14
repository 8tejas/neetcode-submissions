class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        origNums = nums
        last = len(nums) - 1
        mid = len(nums)//2
        while len(nums) >= 1:
            if nums[mid] == target:
                return origNums.index(nums[mid])
            elif nums[mid] > target:
                nums = nums[first:mid]
                mid = len(nums)//2
            elif nums[mid] < target:
                nums = nums[mid+1:]
                mid = len(nums)//2
            else:
                return -1
        return -1

        
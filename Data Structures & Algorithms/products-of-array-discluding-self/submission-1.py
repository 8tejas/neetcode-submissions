class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodWithoutZero = 1
        mult = []
        for i in nums:
            if i == 0:
                prodWithoutZero = prod
                prod *= i
                continue
            prod *= i 
            prodWithoutZero *= i
        for i in nums:
            if i == 0:
                mult.append(prodWithoutZero)
                continue
            mult.append(prod//i)
        return mult
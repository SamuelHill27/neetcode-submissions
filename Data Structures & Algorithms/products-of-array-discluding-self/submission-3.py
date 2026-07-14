import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        for i in range(len(nums)):
            prod = math.prod(nums[:i]) * math.prod(nums[i+1:])
            prod_list.append(prod)
        return prod_list
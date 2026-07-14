class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        for i in range(len(nums)):
            prod = 1
            for j in nums[:i]:
                prod *= j
            for k in nums[i+1:]:
                prod *= k
            prod_list.append(prod)
        return prod_list
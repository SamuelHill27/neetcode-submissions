class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            product *= num

        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 1:
            products = [0] * len(nums)
            for i, num in enumerate(nums):
                if num == 0:
                    products[i] = product
                    return products

        products = []
        for num in nums:
            products.append(product // num)

        return products
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            product *= num

        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    products = [0] * len(nums)
                    products[i] = 1
                    without_zero = nums[:i] + nums[i+1:]
                    for num in without_zero:
                        products[i] *= num
                    return products

        products = []
        for num in nums:
            products.append(product // num)

        return products
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for idx, num in enumerate(nums):
            without = nums[:idx] + nums[idx+1:]
            entry = reduce(lambda x, y: x * y, without)
            output.append(entry)
        return output
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            for jdx, j in enumerate(nums[idx + 1:]):
                if i + j == target:
                    return [idx, idx + jdx + 1]

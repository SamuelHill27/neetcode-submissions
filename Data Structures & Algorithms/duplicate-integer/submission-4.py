class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)
        return len(set_of_nums) != len(nums)
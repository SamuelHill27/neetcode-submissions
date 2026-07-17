class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0

        l, r = 0, len(heights) - 1
        while l < r:
            lower = min(heights[l], heights[r])
            area = lower * (r - l)
            if area > total:
                total = area
            
            if (heights[l] < heights[r]):
                l += 1
            else: 
                r -= 1
            
        return total
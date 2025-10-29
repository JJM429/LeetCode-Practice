class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height) - 1, 0

        while l < r:
            #work out area
            area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, area)
            #increment l or r depending on which height is smaller
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            lh = heights[l]
            rh = heights[r]

            max_area = max(max_area, (r - l) * min(lh, rh))
            if lh < rh:
                l += 1
            else:
                r -= 1

        return max_area
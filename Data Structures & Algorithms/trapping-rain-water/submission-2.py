class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        max_left = [0] * n
        left_max = 0
        for i in range(n):
            left_max = max(left_max, height[i])
            max_left[i] = left_max
        
        max_right = [0] * n
        right_max = 0
        for j in range(n - 1, -1, -1):
            right_max = max(right_max, height[j])
            max_right[j] = right_max
        
        water = 0
        for k in range(n):
            water += max(0, min(max_left[k], max_right[k]) - height[k])

        return water
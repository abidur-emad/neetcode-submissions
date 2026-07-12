class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numbers = set(nums)
        max_count = 0

        for num in numbers:
            if num - 1 not in numbers:
                count = 1
                while num + 1 in numbers:
                    num += 1
                    count += 1
                max_count = max(max_count, count)
        
        return max_count
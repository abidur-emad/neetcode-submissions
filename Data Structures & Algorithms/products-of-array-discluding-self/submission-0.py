class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            prefix[i] = product

        suffix = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            suffix[i] = product
        
        return [p * s for p, s in zip(prefix, suffix)]
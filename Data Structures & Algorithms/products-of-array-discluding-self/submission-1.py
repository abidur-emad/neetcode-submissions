class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            ans[i] = product
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]

        return ans
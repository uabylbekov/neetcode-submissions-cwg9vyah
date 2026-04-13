class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            result = max(result, current)
        
        return result
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        result = float("inf")

        while left <= right:
            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return result
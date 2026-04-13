class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0

        for num in nums:
            if num - 1 in seen:
                continue
            current = 1
            while num + 1 in seen:
                current += 1
                num += 1
            
            result = max(result, current)
        
        return result
class Solution:
    def longestConsecutive(self, nums):
        result = 0
        seen = set(nums)
        
        for num in nums:
            if num - 1 not in seen:
                current = 1
                while num + 1 in seen:
                    current += 1
                    num += 1
                result = max(current, result)

        return result
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        best_max = 1

        for i in nums:
            j = i
            current_max = 1
            while j + 1 in seen:
                current_max+=1
                j+=1
            
            best_max = max(current_max, best_max)
        
        return best_max



        2,20,4,10,3,4,5

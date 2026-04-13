class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):

            potential = target - v

            if potential in seen:
                return [seen[potential], i]
    
            seen[v] = i


        return [-1,-1]

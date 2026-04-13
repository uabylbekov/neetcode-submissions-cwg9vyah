class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) -  1
            
            while l < r:
                num1 = nums[i]
                num2 = nums[l]
                num3 = nums[r] 
                if num1 + num2 + num3 == 0:
                    triplets.append([num1, num2, num3])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                elif num1 + num2 + num3 < 0:
                    l += 1
                else:
                    r -= 1

        return triplets   
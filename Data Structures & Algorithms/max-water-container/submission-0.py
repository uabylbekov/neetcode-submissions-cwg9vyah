class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights)-1

        while left < right:
            min_boundary = min(heights[left], heights[right])
            result = max(result, min_boundary * (right-left))
            if heights[left] >= heights[right]:
                right-=1
            else:
                left+=1
        
        return result



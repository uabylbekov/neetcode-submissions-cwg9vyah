class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}
        l = 0
        
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            if (r - l + 1) - max(list(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        result = 0
        left = 0

        for right in (range(len(s))):
            if s[right] in char_to_index and char_to_index[s[right]] >= left:
                left = char_to_index[s[right]] + 1
            
            else:
                result = max(result, right-left+1)
            char_to_index[s[right]] = right

        return result
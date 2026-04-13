class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0
        left = 0  # Left pointer to maintain the start of the substring

        for right in range(len(s)):  
            while s[right] in seen:  # If duplicate found, shrink the window
                seen.remove(s[left])
                left += 1  # Move left pointer
            
            seen.add(s[right])  # Add new character to set
            result = max(result, right - left + 1)  # Update result

        return result
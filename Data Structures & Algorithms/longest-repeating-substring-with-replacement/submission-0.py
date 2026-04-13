class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        seen = {}

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1

            if (right - left + 1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left+=1

            result = max(result, right - left + 1) 

        return result

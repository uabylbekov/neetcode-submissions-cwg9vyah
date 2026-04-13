class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        seen = {}

        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        
        for char in t:
            if char in seen:
                seen[char] -= 1
                if seen[char] == 0:
                    del seen[char]

        return len(seen) == 0
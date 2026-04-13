class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Compare the length of the strings
        if len(t) != len(s):
            # return false if the lengths don't match
            return False

        # Create a dict to count the frequency of the characters
        seen = {}

        # Iterate through the first string to count the characters
        for char in s:
            # increment the frequency count
            seen[char] = seen.get(char, 0) + 1
        

        # Iterate through the second string to 
        for char in t:

            # if char is not in the dict then return false
            if char not in seen:
                return False  # If t has a char not in s
            
            # Otherwise decrease the frequenct counter
            seen[char] -= 1

            # If after the decrease counter is equal to 0 delete the entry
            if seen[char] == 0:
                del seen[char]

        # if the length of the dict is not empy return false
        return len(seen) == 0
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsGroup = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            if key in anagramsGroup:
                anagramsGroup[key].append(s)
            else:
                anagramsGroup[key] = [s]
        
    
        return list(anagramsGroup.values())

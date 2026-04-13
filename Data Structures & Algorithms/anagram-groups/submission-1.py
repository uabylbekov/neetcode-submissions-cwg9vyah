class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsGroup = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            anagramsGroup[tuple(count)].append(s)
        
    
        return list(anagramsGroup.values())

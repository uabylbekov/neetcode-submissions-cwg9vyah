class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for elm in strs:
            count = [0] * 26
            for char in elm:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)

            if key in groups:
                groups[key].append(elm)
            else:
                groups[key] = [elm]

        return list(groups.values())
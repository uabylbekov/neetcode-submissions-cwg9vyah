class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        
        for elm in strs:
            count = [0] * 26

            for char in elm:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)
            
            if key in result:
                result[key].append(elm)
            else:
                result[key] = [elm]
        
        return list(result.values())
            

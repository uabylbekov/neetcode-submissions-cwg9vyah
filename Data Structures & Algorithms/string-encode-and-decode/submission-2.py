class Solution:

    def encode(self, strs):
        result = ""
        
        for s in strs:
            result += str(len(s))  + "#" + s
        
        return result

    def decode(self, s):
        result = []
        
        l = 0
        r = 0

        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r])
                r += 1
                result.append(s[r:r+length])
                r = r + length
                l = r
            else:
                r += 1

        return result





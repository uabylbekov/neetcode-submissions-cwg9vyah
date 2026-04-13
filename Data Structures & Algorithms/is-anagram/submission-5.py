class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_n = Counter(s)
        t_n = Counter(t)

        return s_n == t_n
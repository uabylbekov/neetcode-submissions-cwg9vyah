class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current: str, open_n: int, close_n: int):
            if open_n == close_n == n:
                res.append(current)
            
            if open_n < n:
                backtrack(current + '(', open_n + 1, close_n)
            
            if close_n < open_n:
                backtrack(current + ')', open_n, close_n + 1)
        
        backtrack("", 0, 0)

        return res
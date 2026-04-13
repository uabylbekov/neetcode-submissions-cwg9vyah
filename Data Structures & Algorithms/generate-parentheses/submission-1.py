class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(parentheses, openers, closers):
            if openers  == closers == n:
                result.append(parentheses)
            if openers < n:
                helper(parentheses + "(", openers + 1, closers)
            if closers < openers:
                helper(parentheses + ")", openers, closers + 1)
        
        
        helper("", 0, 0)
        
        
        return result
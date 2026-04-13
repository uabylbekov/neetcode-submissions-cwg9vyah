class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        openers_to_closers = {
                            "(": ")",
                            "[": "]",
                            "{": "}",			
                            }
        
        
        for elm in s:
            if elm in openers_to_closers:
                stack.append(elm)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()

                if openers_to_closers[last] != elm:
                    return False

        return len(stack) == 0
        
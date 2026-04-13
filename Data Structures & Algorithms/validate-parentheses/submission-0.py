class Solution:
    def isValid(self, s: str) -> bool:
        openers_to_closers = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        openers = set(["(", "{", "["])
        stack = []

        for elm in s:
            if elm in openers:
                stack.append(elm)
            else:
                if len(stack) == 0:
                    return False

                last = stack.pop()

                if openers_to_closers[last] != elm:
                    return False
        
        return len(stack) == 0

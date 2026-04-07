class Solution:
    def isValid(self, s: str) -> bool:
        braces = {'(':')', '{':'}', '[':']'}
        stack = []

        for ch in s:
            if ch in braces:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if braces[popped] != ch:
                    return False
            
        if len(stack) != 0:
            return False
        
        return True
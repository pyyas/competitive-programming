class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in lookup: 
                if len(stack) == 0:
                    return False
                if stack[-1] != lookup[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False

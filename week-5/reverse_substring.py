class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                temp = ''
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                for i in temp:
                    stack.append(i)
            else:
                stack.append(i)
        return ''.join(stack)

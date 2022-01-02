class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i=='+':
                stack[-1] = stack[-2]+stack[-1]
                stack.pop(-2)
            elif i=='-':
                stack[-1] = stack[-2]-stack[-1]
                stack.pop(-2)
            elif i=='*':
                stack[-1] = stack[-1]*stack[-2]
                stack.pop(-2)
            elif i=='/':
                stack[-1] = int(stack[-2]/stack[-1])
                stack.pop(-2)
                
            else:
                stack.append(int(i))
        return stack[-1]

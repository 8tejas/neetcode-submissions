class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i == '+':
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif i == '-':
                num = -(stack.pop() - stack.pop())
                stack.append(num) 
            elif i == '*':
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif i == '/':
                last = stack.pop()
                num = int(stack.pop() / last)
                stack.append(num)
            else:
                stack.append(int(i))
        return stack[0]
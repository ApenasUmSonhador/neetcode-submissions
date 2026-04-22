class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        for x in tokens:
            if x in ops:
                r = stack.pop()
                l = stack.pop()
                stack.append(ops[x](l,r))
            else:
                stack.append(int(x))
        return stack[0]
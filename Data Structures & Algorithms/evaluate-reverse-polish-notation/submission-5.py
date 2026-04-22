class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def div(x, y):
            return -(abs(x) // abs(y)) if x*y < 0 else x//y
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": div
        }
        for x in tokens:
            if x in ops:
                r = stack.pop()
                l = stack.pop()
                stack.append(ops[x](l,r))
            else:
                stack.append(int(x))
        return stack[0]
        
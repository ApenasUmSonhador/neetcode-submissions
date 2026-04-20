class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        closing_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in closing_map:
                if not stack or stack.pop() != closing_map[char]:
                    return False
            else:
                stack.append(char)

        return not stack
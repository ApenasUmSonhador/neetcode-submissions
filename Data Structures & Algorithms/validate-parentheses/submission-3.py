class Solution:
    def isValid(self, s: str) -> bool:
        acc = []
        close = {
             ')': '(',
             ']': '[',
             '}': '{'
        }
        if not s[-1] in close or len(s) % 2 != 0:
            return False

        for x in s:
            if x in close:
                if len(acc) == 0:
                    return False
                last = acc.pop()
                if (close[x]) != last:
                    return False
            else:
                acc.append(x) 
    
        return len(acc) == 0
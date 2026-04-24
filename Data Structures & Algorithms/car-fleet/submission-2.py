class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(position[i], float(speed[i])) for i in range(len(position))]
        stack.sort()
        ans = 1
        prev = (target - stack[-1][0])/stack[-1][1]
        for i in range(len(stack)-2 , -1, -1):           
            atual = (target - stack[i][0])/stack[i][1]
            if prev < atual:
                prev = atual
                ans += 1
        return ans            
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ans = 0
        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                b = s.pop()
                a = s.pop()
                if c == '+':
                    s.append(a + b)
                elif c == '-':
                    s.append(a - b)
                elif c == '*':
                    s.append(a * b)
                elif c == '/':
                    s.append(int(a / b))  # Truncates toward zero
            else:
                s.append(int(c))
        return s.pop()
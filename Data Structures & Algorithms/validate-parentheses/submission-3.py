class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack1.append(c)
            else:
                c2 = ''
                if len(stack1) > 0:
                    c2 = stack1.pop()
                else:
                    return False
                if c == ')':
                    if c2 != '(':
                        return False
                elif c == '}':
                    if c2 != '{':
                        return False
                elif c == ']':
                    if c2 != '[':
                        return False
        if len(stack1) > 0:
            return False
        return True

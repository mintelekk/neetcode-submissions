class Solution:
    def checkValidString(self, s: str) -> bool:
        #Stack of indices for counting parenthesis and stars
        leftParenStack = []
        starStack = []

        #Iterate over string
        for i, c in enumerate(s):
        #Count left parenthesis
            if c == "(":
                leftParenStack.append(i)
            #Remove a left parenthesis for each right parenthesis
            elif c == ")":
                if leftParenStack:
                    leftParenStack.pop()
                #Remove star if no left parenthesis
                elif starStack:
                    starStack.pop()
                else:
                    return False
            else:
                starStack.append(i)
        #Burn extra left parenthesis
        while leftParenStack:
            leftParen = leftParenStack.pop()
            if starStack:
                star = starStack.pop()
            else:
                return False
            if leftParen > star:
                return False
        #Extra stars are empty string
        return True

class Solution:
    def charForDigit(self, d):
        if d == 2:
            return ['a','b','c']
        elif d == 3:
            return ['d','e','f']
        elif d == 4:
            return ['g','h','i']
        elif d == 5:
            return ['j','k','l']
        elif d == 6:
            return ['m','n','o']
        elif d == 7:
            return ['p','q','r', 's']
        elif d == 8:
            return ['t','u','v']
        elif d == 9:
            return ['w','x','y','z']
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ans = []
        
        combo = ""

        def dfs(i):
            nonlocal combo
            if i == len(digits):
                ans.append(combo)
                return
            digit_chars = self.charForDigit(int(digits[i]))
            print(digit_chars)
            for c in digit_chars:
                combo += c
                dfs(i+1)
                combo = combo[:len(combo)-1]
        dfs(0)
        return ans
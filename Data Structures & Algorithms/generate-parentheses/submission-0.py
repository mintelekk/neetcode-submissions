class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        combinations = ""
        openc = 0
        close = 0
        def dfs(openc, close, combinations):
            if openc == n and close == n:
                ans.append(combinations)
                return
            if openc < n:
                dfs(openc + 1, close, combinations + '(')
            if close < openc:
                dfs(openc, close + 1, combinations+ ")")
        dfs(0,0,'')
        return ans
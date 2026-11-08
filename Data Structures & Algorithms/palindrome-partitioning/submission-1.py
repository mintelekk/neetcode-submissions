class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s2):
            if s2 == s2[::-1]:
                return True
            return False
        ans = []
        combo = []
        def dfs(j,i):
            #j start of current substring
            #i current iterating index
            
            #Base case
            if j == len(s):
                ans.append(combo.copy())
                return

            if i == len(s):
                return
            
            if isPalindrome(s[j:i+1]):
                combo.append(s[j:i+1])
                dfs(i+1, i+1)
                combo.pop()
            dfs(j, i+1)

        dfs(0,0)
        return ans
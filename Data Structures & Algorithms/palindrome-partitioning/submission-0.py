class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s2):
            if s2 == s2[::-1]:
                return True
            return False
        ans = []
        combo = []
        def dfs(j):
            #j start of current substring
            #i current iterating index
            
            #Base case
            if j == len(s):
                ans.append(combo.copy())
                return
            #Sub j to i is palidrome or not
            for end in range(j, len(s)):
                if isPalindrome(s[j:end+1]):
                    combo.append(s[j:end+1])
                    dfs(end+1)
                    combo.pop()
        dfs(0)
        return ans
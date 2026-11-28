class Solution:
    
    hashTable = {}
    def climbStairs(self, n: int) -> int:
        
        ans = 0
        if n > 2:
            if n in self.hashTable:
                return self.hashTable[n]
            else:
                ans += self.climbStairs(n-1)
                ans += self.climbStairs(n-2)
                self.hashTable[n] = ans
        elif n == 2:
            return 2
        elif n == 1:
            return 1
        return ans
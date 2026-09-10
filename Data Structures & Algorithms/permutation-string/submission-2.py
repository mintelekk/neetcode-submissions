class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0,0
        s1counts = dict()
        s2counts = dict()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        #Initialize permutation dictionary. 
        #Perm 1 counts of s1 perm2 counts of substring starting zero.
        for c in s1:
            if c in s1counts:
                s1counts[c] = s1counts[c] + 1
            else:
                s1counts[c] = 1
            s2counts[c] = 0
        #Dictionaries are counts of each character in s1 and s2 substring
        while r < len(s2):
            #Check next character is in permutation.
            if s2[r] in s2counts:
                #Check if this character is needed in current substring
                #To count towards permutation
                if s2counts[s2[r]] < s1counts[s2[r]]:
                    s2counts[s2[r]] = s2counts[s2[r]] + 1 
                else:
                    #Character not needed -> Move window forward on l
                    #Until it skips one not needed character of that letter.
                    while s2[l] != s2[r]:
                        s2counts[s2[l]] = s2counts[s2[l]] - 1
                        l+=1
            #If not then move left of window to r+1
            else:
                while l < r and l < len(s2):
                    s2counts[s2[l]] = s2counts[s2[l]] - 1
                    l+=1
                l+=1
            r+=1
            #Check current substring if it is permutation.
            if s1counts == s2counts:
                return True
            #else:
                #print(s2[l:r+1])
                #print(s2counts)
        return False
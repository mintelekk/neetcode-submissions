class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0,0
        s1counts = dict()
        s2counts = dict()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        #Submission 2 speed up time.
        #Use matches variable to check if dictionaries are equal.
        #Initialize permutation dictionary. 
        #Perm 1 counts of s1 perm2 counts of substring starting zero.
        for c in alpha:
            s1counts[c] = 0
            s2counts[c] = 0
        for i in range(len(s1)):
            s1counts[s1[i]] = s1counts[s1[i]] + 1
            s2counts[s2[i]] = s2counts[s2[i]] + 1

        matches = 0
        for c in alpha:
            matches += (1 if s1counts[c] == s2counts[c] else 0)
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = s2[r]
            s2counts[index] = s2counts[index]+1
            if s1counts[index] == s2counts[index]:
                matches+=1
            elif s1counts[index] + 1 == s2counts[index]:
                matches-=1

            index = s2[l]
            s2counts[index] = s2counts[index]-1
            if s1counts[index] == s2counts[index]:
                matches+=1
            elif s1counts[index] - 1 == s2counts[index]:
                matches-=1
            l+=1
        return matches == 26
        '''
        Dictionaries are counts of each character in s1 and s2 substring
        while r < len(s2):
            Check next character is in permutation.
            if s2[r] in s2counts:
                Check if this character is needed in current substring
                To count towards permutation
                if s2counts[s2[r]] < s1counts[s2[r]]:
                    s2counts[s2[r]] = s2counts[s2[r]] + 1 
                else:
                    Character not needed -> Move window forward on l
                    Until it skips one not needed character of that letter.
                    while s2[l] != s2[r]:
                        s2counts[s2[l]] = s2counts[s2[l]] - 1
                        l+=1
            If not then move left of window to r+1
            else:
                while l < r and l < len(s2):
                    s2counts[s2[l]] = s2counts[s2[l]] - 1
                    l+=1
                l+=1
            r+=1
            Check current substring if it is permutation.
            if s1counts == s2counts:
                return True
            else:
                print(s2[l:r+1])
                print(s2counts)
        return False
        '''
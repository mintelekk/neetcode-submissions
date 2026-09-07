class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        ans = 0
        l,r = 0,0
        while r < len(s):
            while s[r] in characterSet:
                characterSet.remove(s[l])
                l += 1
            characterSet.add(s[r])
            ans = max(ans, r-l + 1)
            r += 1

        return ans
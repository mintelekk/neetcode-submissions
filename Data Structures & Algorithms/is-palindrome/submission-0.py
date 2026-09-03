class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(str.isalnum, s)).lower()
        return s1 == s1[::-1]
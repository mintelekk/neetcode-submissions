class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for c in s:
            if c not in dict1.keys():
                dict1[c] = 1
            else:
                dict1[c] = dict1[c] + 1
        for c in t:
            if c not in dict2.keys():
                dict2[c] = 1
            else:
                dict2[c] = dict2[c] + 1
        if dict1 == dict2:
            return True
        return False
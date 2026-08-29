class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i, s in enumerate(strs):
            sortedStr = "".join(sorted(s))
            if sortedStr in dict1:
                dict1[sortedStr].append(i)
            else:
                dict1[sortedStr] = [i]
        ans = []
        for k, v in dict1.items():
            v2 = []
            for v3 in v:
                v2.append(strs[v3])
            ans.append(v2)
        return ans
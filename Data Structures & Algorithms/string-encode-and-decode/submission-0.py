class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        inLength = True
        len1 = ""
        while i < len(s):
            if s[i] != '#':
                len1 += s[i]
            elif s[i] == '#':
                ans.append(s[i+1:i+1+int(len1)])
                i+= int(len1)
                len1 = "" 
            i += 1
        return ans
        
               

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()
        have, need = 0, len(target)
        min_len = 100001
        best_l = 0
        l = 0
        for r, char in enumerate(s):
            window[char] += 1
            if char in target and window[char] == target[char]:
                have += 1

            #Window valid when have == need
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r- l  + 1
                    best_l = l
                #Shrink from left
                left_char = s[l]
                window[left_char] -= 1
                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                l += 1
        return "" if min_len == 100001 else s[best_l:best_l + min_len]
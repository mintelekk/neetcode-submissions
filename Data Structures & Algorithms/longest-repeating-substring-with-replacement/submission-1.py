class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return len(s)

        l, r = 0, 0
        maxLength = 0
        freq = dict()

        while r < len(s):
            if s[r] in freq:
                freq[s[r]] = freq[s[r]] + 1
            else:
                freq[s[r]] = 1
            max_freq = max(freq.values())
            window_length = r - l + 1
            if window_length - max_freq <= k:
                maxLength = max(maxLength, window_length)
            else:
                freq[s[l]] = freq[s[l]] - 1
                l += 1
            r += 1
        return maxLength
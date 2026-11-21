class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #If there is a repeat character that character must be in same substring as first one.
        #two pointers with hash table
        #Find first and last index of each character.
        i, i2 = 0, 0
        hashTable = {}
        while i2 < len(s):
            hashTable[s[i2]] = i2
            i2 += 1
        result = []
        start, end = 0,0
        #Build substring list answer
        for i, char in enumerate(s):
            end = max(end, hashTable[char])

            if i == end:
                result.append(i- start + 1)
                start = i + 1 
        return result
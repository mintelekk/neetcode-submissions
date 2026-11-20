class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handSorted = sorted(hand)
        
        hashTable = {}
        for n in hand:
            if n not in hashTable:
                hashTable[n] =1
            else:
                hashTable[n]= hashTable[n]+1
        #handSorted is sorted list of cards
        #hashTable has count of every card
        if len(hand) % groupSize != 0:
            return False
        current_n = min(hashTable.keys())
        while len(hashTable) > 0:
            current_n = min(hashTable.keys())
            for i in range(current_n, current_n+groupSize, 1):
                if i in hashTable and hashTable[i] > 0:
                    hashTable[i] = hashTable[i]-1
                    if hashTable[i] == 0:
                        hashTable.pop(i)
                else:
                    return False
        return True
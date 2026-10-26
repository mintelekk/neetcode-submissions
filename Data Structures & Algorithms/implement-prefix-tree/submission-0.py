class PrefixTree:

    def __init__(self):
        self.map1 = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.map1:
                curr.map1[ch] = PrefixTree()
            curr = curr.map1[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch not in curr.map1:
                return False
            curr = curr.map1[ch]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch not in curr.map1:
                return False
            curr = curr.map1[ch]
        return True
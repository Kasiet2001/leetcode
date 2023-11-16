class Trie:

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        if word not in self.trie:
            self.trie.append(word)

    def search(self, word: str) -> bool:
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        for i in self.trie:
            if i[:len(prefix)] == prefix:
                return True
        return False

class MagicDictionary:

    def __init__(self):
        self.dict = set()
    def buildDict(self, dictionary):
        self.dict = set(dictionary)
    def search(self, searchWord):
        for w in self.dict:
            if len(searchWord) == len(w):
                diff = 0
                for i in range(len(searchWord)):
                    if searchWord[i] != w[i]:
                        diff += 1
                if diff == 1:
                    return True
        return False
print()

class MyHashSet:

    def __init__(self):
        self.occur = dict()

    def add(self, key: int) -> None:
        self.occur[key] = True

    def remove(self, key: int) -> None:
        if key in self.occur:
            del self.occur[key] 

    def contains(self, key: int) -> bool:
        return True if key in self.occur else False
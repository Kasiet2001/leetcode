from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
    def pop(self) -> int:
        max_freq = max(self.group.keys())
        val = self.group[max_freq].pop()
        if not self.group[max_freq]:
            del self.group[max_freq]
        self.freq[val] -= 1
        return val

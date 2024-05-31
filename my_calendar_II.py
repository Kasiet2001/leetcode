import bisect
class MyCalendarTwo:

    def __init__(self):
        self.events = []
    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.events, (start, 1))
        bisect.insort(self.events, (end, -1))
        total = 0
        for event, t in self.events:
            total += t
            if total == 3:
                self.events.remove((start,1))
                self.events.remove((end,-1))
                return False

        return True
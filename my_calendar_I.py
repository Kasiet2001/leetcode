from sortedcontainers import SortedList


class MyCalendar:
    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.events.bisect_left((start, end))
        if (idx < len(self.events) and end > self.events[idx][0] or
                idx > 0 and self.events[idx - 1][1] > start):
            return False

        self.events.add((start, end))
        return True
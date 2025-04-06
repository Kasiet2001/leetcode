from collections import deque
from sortedcontainers import SortedList
from typing import List, Tuple

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.packetSet = set()
        self.sorted_by_dest_time = SortedList()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packetSet:
            return False

        if len(self.queue) >= self.memoryLimit:
            oldest = self.queue.popleft()
            self.packetSet.remove(tuple(oldest))
            self.sorted_by_dest_time.remove((oldest[1], oldest[2]))

        self.queue.append([source, destination, timestamp])
        self.packetSet.add(packet)
        self.sorted_by_dest_time.add((destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.packetSet.remove(tuple(packet))
        self.sorted_by_dest_time.remove((packet[1], packet[2]))
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = self.sorted_by_dest_time.bisect_left((destination, startTime))
        right = self.sorted_by_dest_time.bisect_right((destination, endTime))
        return right - left
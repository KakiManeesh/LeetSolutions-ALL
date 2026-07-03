# Last updated: 7/3/2026, 12:55:10 PM
import heapq

class EventManager:
    def __init__(self, events: list[list[int]]):
        self.event = {}
        self.heap = []
        for i in events :
            self.event[i[0]] = i[1]
            heapq.heappush(self.heap, (-i[1] , i[0]) )

            
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.event[eventId] = newPriority
        heapq.heappush(self.heap,(-newPriority,eventId))
    
    def pollHighest(self) -> int:
        while self.heap:
            priority, eventId = heapq.heappop(self.heap)

            if (eventId in self.event and self.event[eventId] == -priority ):
                del self.event[eventId]
                return eventId
        return -1
        
# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()'''

'''
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.event = events
            
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        for i in range(len(self.event)):
            if self.event[i][0] == eventId :
                self.event[i][1] = newPriority
                break      

    def pollHighest(self) -> int:
        if self.event :
            self.event.sort(key=lambda x: (-x[1], x[0]))
            return self.event.pop(0)[0]
        else:
            return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()











'''

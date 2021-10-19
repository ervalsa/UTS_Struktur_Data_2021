import heapq


class PriorityQueue:
    def __init__(self):
        self.data = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.data, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.data)[-1]


priority_queue = PriorityQueue()
priority_queue.push('Kakek', 5)  # || Kakek ||
priority_queue.push('Ibu hamil 2', 4)  # || Kakek || Ibu hamil 2 ||
priority_queue.push('Kakek 2', 5)  # || Kakek || Kakek 2 || Ibu hamil 2 ||
priority_queue.push('Ibu hamil ', 4)  # || Kakek || Kakek 2 || Ibu hamil 2 || Ibu hamil ||
priority_queue.pop()  # || Kakek 2 || Ibu hamil 2 || Ibu hamil ||
priority_queue.push('Penumpang biasa', 1)  # || Kakek 2 || Ibu hamil 2 || Ibu hamil || Penumpang biasa ||
priority_queue.pop()  # || Ibu hamil 2 || Ibu hamil || Penumpang biasa ||
priority_queue.push('Disabilitas', 3)  # || Ibu hamil 2 || Ibu hamil || Disabilitas || Penumpang biasa ||

while len(priority_queue.data) != 0:  # Pop semua yang tersisa
    print(priority_queue.pop(), end=" || ")

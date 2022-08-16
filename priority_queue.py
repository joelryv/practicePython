import heapq

class PrioritQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority,item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)

if __name__ == "__main__":
    pq = PrioritQueue()
    print(pq)
    print(pq.is_empty())

    pq.put("Cheems", 1)
    pq.put("Comida", 2)
    pq.put("Dineros", 3)

    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())

    print(pq)
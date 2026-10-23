class Patient:
    def __init__(self,name,urgency):
        self.name = name
        self.urgency = urgency
    
    def __repr__(self):
        return f"Patient ({self.name}, urgency={self.urgency})"

class MinHeap:
    def __init__(self):
        self.data = []
    
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data)-1)
    
    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"-{patient.name} ({patient.urgency})")
    
    def peek(self):
        if not self.data:
            return None
        return self.data[0]
    
    def remove_min(self):
        if not self.data:
            return None
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return root
    
    def heapify_up(self, index): 
        while index > 0:
            parent = (index - 1) // 2 
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break                  

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest           



# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency)   
assert next_up.name == "Taylor"

served = heap.remove_min()
print(served.name)                    
assert served.name == "Taylor"
heap.print_heap()

assert heap.peek().name == "Jordan"
assert len(heap.data) == 2

assert heap.remove_min().name == "Jordan"
assert heap.remove_min().name == "Avery"
assert len(heap.data) == 0

assert heap.peek() is None
assert heap.remove_min() is None
heap.print_heap()                     

solo = MinHeap()
solo.insert(Patient("Solo", 4))
assert solo.peek().name == "Solo"
assert solo.remove_min().name == "Solo"
assert solo.data == []

dup = MinHeap()
dup.insert(Patient("A", 2))
dup.insert(Patient("B", 2))
dup.insert(Patient("C", 2))
assert len(dup.data) == 3
assert dup.remove_min().urgency == 2
assert dup.remove_min().urgency == 2
assert dup.remove_min().urgency == 2

b = MinHeap()
b.insert(Patient("Low", 10))
b.insert(Patient("High", 1))
assert b.peek().name == "High"

worst = MinHeap()
for i, u in enumerate([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]):
    worst.insert(Patient(f"P{i}", u))
assert worst.peek().urgency == 1

best = MinHeap()
for i, u in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    best.insert(Patient(f"P{i}", u))
assert best.peek().urgency == 1

def is_valid_heap(h):
    for i in range(1, len(h.data)):
        parent = (i - 1) // 2
        if h.data[parent].urgency > h.data[i].urgency:
            return False
    return True

h = MinHeap()
for i, u in enumerate([7, 3, 9, 1, 5, 2, 8, 4, 6, 10]):
    h.insert(Patient(f"P{i}", u))
    assert is_valid_heap(h)

order = []
while h.data:
    order.append(h.remove_min().urgency)
    assert is_valid_heap(h)
assert order == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

m = MinHeap()
m.insert(Patient("X", 5))
m.insert(Patient("Y", 2))
assert m.remove_min().name == "Y"
m.insert(Patient("Z", 1))
m.insert(Patient("W", 8))
assert m.remove_min().name == "Z"
assert m.remove_min().name == "X"
assert m.remove_min().name == "W"
assert m.remove_min() is None

print("All MinHeap tests passed!")
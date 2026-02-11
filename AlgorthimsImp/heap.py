class Heap: 
    def __init__(self):
        self.heap = [float('-inf')]

    def push(self, val): 
        self.heap.append(val)

        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]: # smaller than it is parent 
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i //2 

        return

    def pop(self): 
        if len(self.heap) == 1: #empty 
            return None
        if len(self.heap) == 2: # one value
            return self.heap.pop()

        out = self.heap[1]

        self.heap[1] = self.heap.pop()

        i = 1
        lh = len(self.heap)
        while i * 2 < lh:
            left = i * 2
            right = left + 1

            # Assume left is smaller child
            smaller_child = left

            # Check if right child exists and is smaller
            if right < lh and self.heap[right] < self.heap[left]:
                smaller_child = right

            # If parent is already smaller, stop
            if self.heap[i] <= self.heap[smaller_child]:
                break

            # Otherwise swap
            self.heap[i], self.heap[smaller_child] = \
                self.heap[smaller_child], self.heap[i]

            i = smaller_child


        return out
        

        

if __name__ == '__main__': 
    pq = Heap()
    pq.push(2)
    pq.push(3)
    pq.push(1)


    print(pq.pop())
    print(pq.pop())
    print(pq.pop())

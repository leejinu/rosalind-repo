class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return position of parent, left child, or right child at pos
    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2*pos
    
    def rightChild(self, pos):
        return (2*pos)+1

    # Function that returns true if the passed node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:  
            return True
        return False

    # Function to swap two nodes of heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        
        # If current node is non-leaf node, 
        if not self.isLeaf(pos):
            # and smaller than any of its child node
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                # Swap with the left child and heapify the left child
                if (self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]):
                    self.swap(pos,self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))
        

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMax(self):
        if self.size == 0:
            return
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.maxHeapify(self.FRONT)
        self.size -= 1
        return popped
    
    def heap_sort(self):
        sorted_arr = []
        original_size = self.size
        for _ in range(original_size):
            sorted_arr.append(self.extractMax())
            
        return sorted_arr
            

def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    maxsize = int(lines[0])
    A = lines[1].split()
    A = [int(n) for n in A]

    return A, maxsize

def heapSort(Heap):
    A = []

    

if __name__ == "__main__":
    import sys

    A = []
    A, maxsize = read_file('rosalind_hs.txt')
    
    max_heap= MaxHeap(maxsize)

    for n in A:
        max_heap.insert(n)

    
    sorted_A = max_heap.heap_sort()
    with open('output_heapSort.txt', 'w') as f:
        line = ""
        for i in range(0, len(sorted_A)):
            line += str(sorted_A[len(sorted_A)-i-1])+" "
        f.write(line)
    f.close()
    


    
        

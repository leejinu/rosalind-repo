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
                if (self.Heap[leftChild(pos)] > self.Heap[rightChild(pos)]):
                    self.swap(pos,leftChild(pos))
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
            

def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    maxsize = int(lines[0])
    A = lines[1].split()
    A = [int(n) for n in A]

    return A, maxsize
    

if __name__ == "__main__":
    import sys

    A = []
    A, maxsize = read_file('rosalind_hea.txt')
    
    max_heap= MaxHeap(maxsize)

    for n in A:
        max_heap.insert(n)

    with open('output_heap.txt', 'w') as f:
        line = ""
        for i in range(1, len(max_heap.Heap)):
            line += str(max_heap.Heap[i])+" "
        f.write(line)
    f.close()
    


    
        

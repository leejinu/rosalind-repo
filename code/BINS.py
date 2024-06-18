class Node:
    def __init__(self, data):
        """
        Initialize a Node with data and left/right child nodes.
        """
        self.data = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        """
        Initialize a Binary Search Tree with a root node.
        """
        self.root = None

    def insert(self, data):
        """
        Insert a new node with data into the tree.
        """
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        """
        Recursively insert a new node with data into the tree.
        """
        if node is None:
            return Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        """
        Find a node with key in the tree.
        """
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        """
        Recursively find a node with key in the tree.
        """
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)


def read_file(path):
    """
    Read a file and return its contents.
    """
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: {path} is not exist in current file path.")
        print("Terminate program.")
        return ""


def split_data(text):
    """
    Split the input text into n, m, sorted array, and test array.
    """
    lines = text.split('\n')
    n = int(lines[0].strip())
    m = int(lines[1].strip())
    sorted_arr = lines[2].split()
    test_arr = lines[3].split()
    return n, m, sorted_arr, test_arr

if __name__ == "__main__":
    import sys

    # Unlimit maximum of recursion
    sys.setrecursionlimit(10**6)

    # Read the sample dataset
    text = read_file('../test/rosalind_bins.txt')

    # Split the data into two positive integer, a sorted array A[1...n] of integers, and a list of m integers
    n, m, sorted_arr, test_arr = split_data(text)

    bst = BinarySearchTree()

    # Insert sorted array into the binary search tree
    for x in sorted_arr:
        bst.insert(int(x))

    result = ""
    result_list = []

    # Find the index of each test number in the sorted array
    for number in test_arr:
        if bst.find(int(number)):
            for i, item in enumerate(sorted_arr, 1):
                if int(number) == int(item):
                    result += str(i)
                    result += " "
                    result_list.append(str(i))
                    break
        else:
            result += "-1"
            result += " "
            result_list.append("-1")

    print(result)

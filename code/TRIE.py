

# Node 구조 class 
class Node(object):

    # constructor 
    def __init__(self, key, data=None):
        self.key = key # character for value
        self.data = data # for saving whole string at last node
        self.children = {} # for saving children node

    def __getitem__(self, key):
        return self.children[key]

# Tries 구조 class
class Trie:
    def __init__(self):
        self.head = Node(None)

    def __getitem__(self, key):
        return self.head.children[key]

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string


def print_trie_to_file(node, depth=1, number=[2], output_file='output.txt'):
    with open(output_file, 'w') as f:
        print_trie_recursive_to_file(node, f, depth, number)

def print_trie_recursive_to_file(node, file, depth=1, number=[2]):
    depth = number[0]-1
    for key, child_node in sorted(node.children.items()):
        file.write('{} {} {}\n'.format(depth, number[0], key))
        if child_node.children != None:
            number[0] += 1
            print_trie_recursive_to_file(child_node, file, depth + 1, number)
    
def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    return lines

    
if __name__ == "__main__":
    seqs = []
    seqs = read_file('rosalind_trie.txt')
    print(len(seqs))

    # Trie 구조 선
    trie = Trie()

    for seq in seqs:
        trie.insert(seq)
    print_trie_to_file(trie.head)

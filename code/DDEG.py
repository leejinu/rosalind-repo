# Open and read 'edge list format .txt' file
filename = 'rosalind_ddeg.txt'

with open(filename, 'r') as f:
    lines = f.read().split('\n')

# Save information about the number of vertices and edges
size_info = lines[0].split()

vertex_size = int(size_info[0])
edge_size = int(size_info[1])

V = list(range(1,vertex_size+1))
E = dict()

for key in V:
    E[key] = []

for i in range(0, edge_size+1):
    if i == 0:
        continue
    line = [int(x) for x in lines[i].split()]
    if line[1] not in E[line[0]]:
        E[line[0]].append(line[1])
        E[line[1]].append(line[0])

for key in E.keys():
    print(len(E[key]), end = ' ')

  
    


"""
Problem: Reversal distance
"""

from heapq import heappush, heappop

def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    pi = []
    sigma = []
    lines = [line for line in lines if line != '']        
        
    for i, line in enumerate(lines):
        line = line.strip('\n')
        line = line.split(' ')
        if i%2 == 0 and line != ['']:
            pi.append(line)
        elif i%2==1 and line != ['']:
            sigma.append(line)
    pi = [[int(x) for x in list] for list in pi]
    sigma = [[int(x) for x in list] for list in sigma]

    return pi, sigma

def reverse(perm, i, j):
    while i< j:
        perm[i], perm[j] = perm[j], perm[i]
        i+=1
        j-=1
def heuristic(perm, target):
    # 휴리스틱 함수: 현재 순열에서 목표 순열까지의 거리 추정
    return sum(1 for i in range(len(perm)) if perm[i] != target[i])

def min_reversals(perm1, perm2):
    queue = [(0, perm1, 0)]  # (휴리스틱값 + 지금까지의 리버스 수, 현재 순열, 지금까지의 리버스 수)
    visited = set()
    
    while queue:
        _, perm, dist = heappop(queue)
        if perm == perm2:
            return dist
        for i in range(len(perm)):
            for j in range(i+1, len(perm)):
                next_perm = perm[:]
                reverse(next_perm, i, j)
                if tuple(next_perm) not in visited:
                    visited.add(tuple(next_perm))
                    heappush(queue, (dist + 1 + heuristic(next_perm, perm2), next_perm, dist + 1))
    
    return -1
"""
def get_rev_distance(pi, sigma):
    count = 0
    i = 0
    j = 0
    while i<= len(pi) and j <= len(pi):
        if i == len(pi):
            print(pi)
            print(sigma)
            break
        if pi[i] == sigma[i]:
            i += 1
            j += 1
        else:
            a, b = sigma.index(pi[i]), sigma.index(sigma[i])
            reverse(sigma, a,b)
            count +=1
    return count
"""

pi = []
sigma = []

pi, sigma = read_file('rosalind_revd.txt')

rev_distances = []

for i in range(0, len(pi)):
    print(pi[i])
    print(sigma[i])
    rev_distances.append(min_reversals(pi[i],sigma[i]))

for dist in rev_distances:
    print(dist, end = ' ')
                        


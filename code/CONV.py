def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    S1 = []
    S2 = []
    S1 = lines[0].split(' ')
    S2 = lines[1].split(' ')

    S1 = [round(float(s1), 5) for s1 in S1]
    S2 = [round(float(s2), 5) for s2 in S2]

    return S1, S2

def Minkowski_diff(S1, S2):
    results =[]

    for s1 in S1:
        for s2 in S2:
            results.append(abs(round(s1-s2,5)))
    return results

def find_largest_multiplicity(results):
    return max(results, key=results.count)

if __name__ == '__main__':
    import math
    S1 = []
    S2 = []

    S1, S2 = read_file('rosalind_conv.txt')

    results = []
    results = Minkowski_diff(S1,S2)

    max_diff = find_largest_multiplicity(results)

    print(results.count(max_diff))
    print(max_diff)
    

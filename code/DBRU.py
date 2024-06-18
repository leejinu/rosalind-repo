def read_file(path):
    # Read A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.
    with open(path) as f:
        S = f.read().split('\n')

    return S

def reverse_complement(S):
    return [str(Seq(s).reverse_complement()) for s in S]

def create_node(S_U_Src):
    B = []
    
    for kp1mer in S_U_Src:
        s, t = kp1mer[0:len(kp1mer)-1], kp1mer[1:len(kp1mer)]

        # Do not form multiple nodes corresponding to the same DNA string.
        if (s, t) not in B:
            B.append((s,t))

        B = sorted(B)
            
    return B
                
def write_n_save(results, path):
    with open(path, 'w') as f:
        for line in results:
            line += '\n'
            f.write(line)
    f.close()
            

if __name__ == "__main__":

    from Bio.Seq import Seq
    
    S = [] # Set of (k+1)-mers
    Src = [] # reverse complement Set of (k+1)-mers

   
    S = read_file('rosalind_dbru.txt')
    Src = reverse_complement(S)

    S_U_Src = list(set(S + Src))
    
    # Create node of B for any length k substring of some (k+1)-mer in S U Src
    B = []
    B = create_node(S_U_Src)

    results = []
    for head, tail in B:
        line = "("+head+", "+tail+")"
        results.append(line)
    write_n_save(results, 'output_dbru.txt')
        
        
        

        

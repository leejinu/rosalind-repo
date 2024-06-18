

def read_file(path):
    with open(path, 'r') as f:
        L = f.read().split('\n')

    # Convert str list to float list
    L = [float(n) for n in L]
    n = int((len(L)-3)/2)
    parent_mass = L.pop(0)

    return parent_mass, L, n

def make_mass_table():
    proteins = []
    masses = []
    with open('protein_mass_table.txt', 'r') as f:
        lines = f.read().split('\n')
    
    for line in lines:
        proteins.append(line[0])
        masses.append(round(float(line[1:].strip()),5))
    mass_table = dict(zip(masses, proteins))

    return mass_table

mass_table = make_mass_table()

def inferring_peptide(parent_mass, ions, n, peptide = [""]):
    # condition to terminate: peptide length equals to n
    if len(peptide[0]) == n:
        return peptide
    
    BYions = []
    for i in range(0, len(ions)-1):
        for j in range(1,len(ions)-1):
            aa = mass_table.get(round(ions[j]-ions[i],5),0)
            if aa:
                BYions.append([i,j,aa])
    
    if BYions[0]:
        new_ions = ions[BYions[0][1]:]
        new_parent_mass = BYions[0][2]
        new_peptide = [p+np for np in new_parent_mass for p in peptide]
        peptide =inferring_peptide(parent_mass, new_ions, n, new_peptide)
    
    return peptide

    

if __name__ == "__main__":
    from itertools import combinations
    ions = []
    parent_mass, ions, n = read_file('rosalind_full.txt')

    #inferring_peptide(parent_mass, ions, n)

    

    ions = sorted(ions)

    t = inferring_peptide(parent_mass, ions, n)
    print(t[0])
    
    

    
    

    

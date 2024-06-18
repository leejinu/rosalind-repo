def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    prefixes = [float(line) for line in lines]

    return prefixes

def find_protein_str(prefixes, mass_table):
    protein_str = ""
    for i in range(0, len(prefixes)-1):
        target_mass = abs(prefixes[i] - prefixes[i+1])
        
        for aa, mass in mass_table:
            
            if round(target_mass,5) == round(mass,5):
                protein_str += aa
                break

    return protein_str
        

def make_mass_table():
    proteins = []
    masses = []
    with open('protein_mass_table.txt', 'r') as f:
        lines = f.read().split('\n')
    
    for line in lines:
        proteins.append(line[0])

        masses.append(float(line[1:].strip()))
    mass_table = list(zip(proteins, masses))
    

    return mass_table
        
if __name__ == "__main__":
    import math

    mass_table = make_mass_table()
    
    prefixes = []
    prefixes= read_file('rosalind_spec.txt')
    
    print(find_protein_str(prefixes, mass_table))

    print(len(prefixes))
    print(len(find_protein_str(prefixes, mass_table)))


    

    

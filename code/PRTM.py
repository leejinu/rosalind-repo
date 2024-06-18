def read_file(path):
    f = open(path,'r')

    if f is False:
        print("ERROR: "+path+" is not exist in current file path.")
        print("Terminate program.")
        result = ""
        return result
    text = f.read()
    return text

def make_mass_table(text):
    proteins = []
    masses = []

    lines = text.split('\n')
    
    for line in lines:
        proteins.append(line[0])
        #print(line[1:].strip())
        masses.append(float(line[1:].strip()))
    mass_table = dict(zip(proteins, masses))
    #print(mass_table)
    return mass_table

def calculate_mass(seq, table):
    total = 0.0
    for protein in seq:
        total += table[protein]
    return round(total,3)
        
        
# Read monoisotopic mass table

text = read_file('protein_mass_table.txt')

mass_table = make_mass_table(text)

protein_seq = input("Give me the protein sequence:")

result = calculate_mass(protein_seq, mass_table)

print("Total mass of protein sequence: "+str(result))

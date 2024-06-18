seq = input()

A = 0
C = 0
G = 0
T = 0
for nucleotide in seq:
    if nucleotide == 'A':
        A +=1
    elif nucleotide == 'C':
        C +=1
    elif nucleotide == 'G':
        G +=1
    elif nucleotide == 'T':
        T +=1
    else:
        continue

print(str(A)+" "+str(C)+" "+str(G)+" "+str(T))        

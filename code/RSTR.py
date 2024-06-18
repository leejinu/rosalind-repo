"""
we discussed searching for motifs in large genomes, in which random occurrences of
the motif are possible.

our aim: quantify how frequently random motifs occur

ex) promoters, or regions of DNA that initiate the transcription of gene

promoter: located shortly before the start of its gene, and contains specific
          intervals of DNA that provide an initial binding site for RNA polymerase
          to initiate transcription.

** finding a promoter is the second step in gene prediction
   after establishing the presence of an ORF(ex. start codon, or stop codon)

GC contents가 0.6일 때, ATAGCCGA가 만들어질 확률 = 0.2^4*0.3^4= 0.00001296
90000번의 시행에서 1번도 나오지 않을 확률
(1-0.00001296)^90000

"""
N = int(input("the number of random DNA strings: "))
s = input("seq: ")
GC_content = float(input("GC contents: "))

def calculate_prob(N, s, GC_content):
    AT = s.count('A')+s.count('T')
    GC = s.count('G')+s.count('C')

    prob = (((GC_content)/2)**GC)*(((1-GC_content)/2)**AT)

    prob = 1-(1-prob)**N

    return prob
print('{:.3f}'.format(calculate_prob(N,s, GC_content)))
        


"""
Solution)
1. Find sequences about two GenBank IDs by facilitating Entrez python library
2. Run EMBOSS’s Stretcher for the Pairwise Global alignment
    - Set option gap opening penalty into 10, gap extension penalty into 1
3. Get maximum global alignment score between the DNA strings associated with these IDs.
"""

def read_file(path):
    with open(path, 'r') as f:
        entryIDs = f.read().replace(' ', ', ')

    return entryIDs


if __name__  == '__main__':
    from Bio import Entrez
    from Bio import SeqIO
    """
    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:997)>
    Trouble shooting
    """
    
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    
    entryIDs = read_file('../test/rosalind_need.txt')
    
    Entrez.email = 'ljljw@hanmail.net'
            
    handle = Entrez.efetch(db="nucleotide", id = entryIDs, rettype = "fasta")
    for i, record in enumerate(SeqIO.parse(handle, "fasta")):
        print(">"+record.description)
        print(record.seq)



    


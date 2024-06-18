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
    
    entryIDs = read_file('rosalind_frmt.txt')

    
    Entrez.email = 'ljljw@hanmail.net'

    handle = Entrez.efetch(db="nucleotide", id = entryIDs, rettype = "fasta")
    
    min_length = 10**6
    for i, record in enumerate(SeqIO.parse(handle, "fasta")):
        temp_length = len(record.seq)
        if temp_length < min_length:
            min_length = temp_length
            
    handle = Entrez.efetch(db="nucleotide", id = entryIDs, rettype = "fasta")
    for i, record in enumerate(SeqIO.parse(handle, "fasta")):
        if len(record.seq) == min_length:
            print(">"+record.description)
            print(record.seq)

    


def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    genus = lines[0]
    dates = []
    for i in range(1,3):
        dates.append(lines[i])

    return genus, dates


if __name__  == '__main__':
    from Bio import Entrez
    """
    urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:997)>
    Trouble shooting
    """
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    
    dates = []
    genus, dates = read_file('rosalind_gbk.txt')
    mindate, maxdate = dates[0], dates[1]
    
    print(genus)
    print(dates)
    Entrez.email = 'ljljw@hanmail.net'
    handle = Entrez.esearch(db="nucleotide", term=genus+'[Organism]', mindate=mindate, maxdate = maxdate, datetype="pdat")
    record = Entrez.read(handle)
    
    print(record['Count'])


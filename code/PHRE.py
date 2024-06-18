def read_file(path):
    with open(path, 'r') as f:
        threshold = int(f.readline().strip())
        seqs = f.readlines()
    fastq_path ='rosalind_onlyfastq.txt' 

    with open(fastq_path,'w') as f:
        for seq in seqs:
            f.write(seq)

        f.close()
        
    return threshold, fastq_path


if __name__ == "__main__":
    from Bio import SeqIO
    import numpy as np
    path = 'rosalind_phre.txt'
    threshold, fastq_path = read_file(path)

    averages = []
    for rec in SeqIO.parse(fastq_path, "fastq"):
        a = np.array(rec.letter_annotations["phred_quality"])
        averages.append(a.mean())

    good_reads = [x for x in averages if x < threshold]

    print(len(good_reads))


    

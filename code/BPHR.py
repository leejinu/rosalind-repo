def split_file(path):
    with open(path, 'r') as f:
        threshold = int(f.readline())
        lines = f.read().split('\n')

    file_name = 'rosalind_base.fq.txt'
    with open(file_name, 'w') as f:
        for line in lines:
            line += '\n'
            f.write(line)

    f.close()

    return threshold, file_name

def count_below_threshold(threshold, FASTQ_file_name):
    count = 0

    position_mat = []
    
    with open(FASTQ_file_name, 'r') as f:
        for i, record in enumerate(SeqIO.parse(FASTQ_file_name, 'fastq')):
            position_mat.append(record.letter_annotations["phred_quality"])
    mean_mat = [0 for _ in position_mat[0]]

    for i in range(0, len(position_mat)):
        for j in range(0, len(position_mat[0])):
            mean_mat[j] += position_mat[i][j]
    for i in range(0, len(mean_mat)):
        mean_mat[i] /= len(position_mat)

    count = len([x for x in mean_mat if x < threshold])
    return count
if __name__== "__main__":
    from Bio import SeqIO
    path = 'rosalind_bphr.txt'
    threshold, FASTQ_file_name = split_file(path)

    count = count_below_threshold(threshold, FASTQ_file_name)

    print(count)


        
# record.letter_annotations["phred_quality"]

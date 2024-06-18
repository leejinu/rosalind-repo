from Bio.Seq import Seq

def find_orf(seq):
    idxes = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            idxes.append(i)
    return idxes

def translate_orf(seq, idxes):
    proteins = []
    for idx in idxes:
        orf_seq = seq[idx:]
        protein_seq = orf_seq.translate(to_stop=True)
        proteins.append(str(protein_seq))
    return proteins

if __name__ == '__main__':
    DNA_seq = input("Seq: ")
    
    # 원본 DNA 시퀀스와 리버스 컴플리먼트를 생성
    DNA_seq = Seq(DNA_seq)
    r_DNA_seq = DNA_seq.reverse_complement()

    # ORF를 찾기 위해 원본 DNA 시퀀스와 리버스 컴플리먼트에서 시작 위치를 찾음
    idxes = find_orf(DNA_seq)
    reverse_idxes = find_orf(r_DNA_seq)

    # 번역된 단백질 시퀀스 저장
    translated_proteins = translate_orf(DNA_seq, idxes)
    translated_proteins.extend(translate_orf(r_DNA_seq, reverse_idxes))

    longest_protein = max(translated_proteins, key=len)
    print(longest_protein)

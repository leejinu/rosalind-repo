# read txt file and return text
def read_file(filename):
    f = open(filename, 'r')
    if f is False:
        print("{Error} "+filename+" does not exist.")
        print("Terminate the program.")
        return "Error"
    else:
        text = f.read()
        return text

# parse text -> samples, and sequences
def parse_text(text):
    lines = text.split()
    samples = []
    sequences = []

    current_sequence = ""
    current_sample = ""
    for line in lines:
        if line.startswith(">Rosalind"):
            if current_sequence:
                samples.append(current_sample)
                sequences.append(current_sequence)
                current_sequence = ""
            current_sample = line[1:]
        else:
            current_sequence += line.strip()

    if current_sequence: # Save last sequence
        samples.append(current_sample)
        sequences.append(current_sequence)
        
    return samples, sequences

from functools import partial, reduce
from itertools import chain
from typing import Iterator

def ngram(seq: str, n: int) -> Iterator[str]:
    return (seq[i:i+n] for i in range(0, len(seq)-n+1))

def allngram(seq: str) -> set:
    lengths = range(len(seq))
    ngrams = map(partial(ngram, seq), lengths)
    return set(chain.from_iterable(ngrams))

    
# Initialize sample and sequence array
samples = []
sequences = []

# Read the txt file
text = read_file('rosalind_lcsm.txt')

# Parse samples and sequences in the text
samples, sequences = parse_text(text)       

seqs_ngrams = map(allngram, sequences)
intersection = reduce(set.intersection, seqs_ngrams)
longest = max(intersection, key = len)


print(longest)

def valid(seq):
    seq_set = set(seq.upper())
    # confirm if its elements is equal to 
    # the set of valid DNA bases
    bases = {"A", "T", "G", "C"}
    return seq and bases.union(seq_set) == bases

def validated(seqs, delimiter):
    seqs = seqs.upper()
    seq_list = seqs.split(delimiter)
    res = []
    for i, seq in enumerate(seq_list):
        if valid(seq):
            res.append((seq, i+1))
    return res

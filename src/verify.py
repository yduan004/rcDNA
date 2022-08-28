def valid(seq):
    seq_set = set(seq.upper())
      
    # confirm if its elements is equal to 
    # the set of valid DNA bases
    bases = {"A", "T", "G", "C"}
    if bases.union(seq_set) == bases:
        return True
    return False

def validated(seqs):
    seqs = seqs.upper()
    seq_list = seqs.split('\n')
    res = []
    for seq in seq_list:
        if valid(seq):
            res.append(seq)
    return res

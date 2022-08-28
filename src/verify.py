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
    seq_list = seqs.split('\r\n')
    if seq_list[0] == '':
        return []
    res = []
    for i, seq in enumerate(seq_list):
        if valid(seq):
            res.append((seq, i+1))
    return res

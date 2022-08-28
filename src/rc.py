def reverseComplement(seqs):
    res = []
    for seq, i in seqs:
        comp = seq.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
        res.append((comp[::-1].upper(), i))
    return res
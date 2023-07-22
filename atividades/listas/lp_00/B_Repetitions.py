dna = input()

i = 0
seq = 1
seqMax = 1
lenght = len(dna)
while i + 1 < lenght:
    if dna[i] == dna[i + 1]:
        seq += 1
    else:
        seqMax = seqMax if seqMax > seq else seq 
        seq = 1
    i += 1
else:
    seqMax = seqMax if seqMax > seq else seq
    
print(seqMax)  

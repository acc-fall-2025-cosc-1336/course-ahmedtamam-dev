def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        return "Error: DNA strings must be the same length."
    
    distance = 0
    index = 0
    while index < len(dna1):
        if dna1[index] != dna2[index]:
            distance += 1
        index += 1
    
    return distance

def get_dna_complement(dna):
    complement = ""

    index = len(dna) - 1
    while index >= 0:
        letter = dna[index]

        if letter == 'A':
            complement += 'T'
        elif letter == 'T':
            complement += 'A'
        elif letter == 'C':
            complement += 'G'
        elif letter == 'G':
            complement += 'C'
        else:
            complement += '?'

        index -= 1
    
    return complement

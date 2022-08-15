from scipy.spatial.distance import hamming
# Calculate Hamming distance
bit_1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
bit_2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
dist = hamming(bit_1, bit_2)
# Print result
print(dist)
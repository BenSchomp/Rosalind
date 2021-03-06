#!/usr/bin/python

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" # sample
dna = "CCTTATCACGCTGCTGATTAAGCGTCCTCGAGCGGGCTGTGATGCGCCGCCAGGCATAGTAGGAGGCGTAGGATACCTACTCGATATGTCGTGGCTAATTGCATCGGTATACCGGCCTTTATCGCGATGAGGAGGATTGGAGTCGGGGTTTTGACATCCTGAGCATGATCCGCGACCAACTGGAGTGAGTACGCGCAACGCGAGCAACTACAGGACGTGGCGCGTGTCATCTGCGTAGTCTAAAAACTGTCCGGCGAGAACGCATGGTCAGACCAGTCACGCCCAATTGAAGCTAGTTCCTTCTGCTTAAATCCCCCACACAGATCTTAACTATGTGCTCTCCAAGATGCCCGTTCCAGGTCTACTACGTATAAATCCGCTTCATTATATCCAACCGCATATCCTTAAGACTTGAGTGGATAAAGATACCAGGACAACAGCGGCGGACCATTGTCTAGGCCAGCAGCTGCAACTGCGATAGCTAACTTCCACAGCTGGCCGAGTCGGGACGCACATTAAAGAGGTAGTCACACTCCGCGGAGACGACGCATTACCCGCCGCGTAGTAGTGATGATGTCGGTTGAATGGCCGAAAACACATTTTTGCCAGTCTCGCGACGATGAAGGGGCTCGTCCATAAATGAGCCGGCGTGCACTCACATTTAATTAGTTACTACCAGGTGTAGCGTTCTAAACGGTTAGGTCGACACGTCTTAACACCGTCGCGACTGCCCGTTACACAGCCCGGGAGTCATCACGCGGCGCACTGATTAGGGTGGCTAGATTAGTCCATTTGCTTTCTTTAGAACGTCTCCAGAGCGTCAATTACTTCTCCGTCGAATTCTGAAAGAGAAGTTCACGGAACCCTTCGTAAATCAAACTGAGGTTTCTCCGGCTGTTATCAGACGATTCCAGGGGATGATCGTTCGTTCTATATACCGGCAAAAAG"
result = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for c in dna:
  if c == 'A' or c == 'C' or \
     c == 'G' or c == 'T':
    result[c] += 1;

print( '%d %d %d %d' % (result['A'], result['C'], result['G'], result['T']) )



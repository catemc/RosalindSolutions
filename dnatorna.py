# -*- coding: utf-8 -*-
"""DNAtoRNA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1joQmkwc3fU3tMsP3oMAfnaPFK6qEu1bs
"""

sequence = 'TTATAGAACAGTAAATAAGCTCCCAATCGGAAGAACTCGAATTGACAAGACATTCTAGAAGGATAAGAATCTAAAACGAGCCAGATGTATGTACGCAGCGAGTCCAGACAATCGGAGCCGAACGGGTACCCTGACGGCCAGCTGAGAGTTATACTGACATAGTCTACGTAGCCCCGTTATATTTCTCGTCTTTAATCAGTCGTTGTAATTGCCTGGCCGATTGGCGTTGTACGACTTTCGATCAGAAAGATAATGTCTAAATAGAGGCGCACCGGTACCAACGACAATCATCTATCGCCCATGGCCGATATGTTCGTGACTGGTAATACGTCATACCTGTTAACGTCTACTTTTTGACGCACAGCGAGAAAAGGGCGCCACCTATCTCGAAGTGAACTACTTAGAGGCAGGACTAAACTAACCTGGCTTAGAGGTCACTATAAGACTGTGAAGGTGATTGTTCGATGCTCGGGTTCCCGTGCGGGAACGCACACACGGCTAGCCTGGTGGCTCATTCTCATCTTTAACAAAGTCGAAGGCCATCCATCTACAGCACGCGGTGCTCTTAACATTAATTTCTCCCCTCTTAAAACCATGTCTGAAAGCCTCGCTAAAATTTTGAAGTATATTAATTTGGCGATCGTGTACGGGGCCCGGGAGCGAGTCTTGGCGTGGGTTAGCTGCGCCGAGTCCGCACTCGACGATAGTCATCGCGCGAAACTTGGGAGCGCTTCCGAGCAAGGCGCAAGTCTCGACCCCGCATGTCGTTCGTATTCATGAGACCTATGGCGGGGACCTGTAATCACGATAAACCAACACTATGTCACTACCATCTTCCTTCCGTCCTCCCAACCTAGTGTAGCGGTTCGCATGAACCAAAATGATGATTTCCGTGCCGAGCCTTTATGCCCTCCGCCGGT'
def dnatorna(seq):
  print(seq.replace('T', 'U'))
  return

dnatorna(sequence)
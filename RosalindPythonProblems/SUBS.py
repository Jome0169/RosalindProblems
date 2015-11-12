

from Bio import Motif

Protein = open("rosalind_subs.txt", "r")
Realseq = Protein.read()


SeqLen = len(Realseq)
Direct = str(Realseq)
for item in Direct:
    item = item.rstrip("\n")
    if item == "TCTGGGTTC":
        print "I found the Motif!!"
    else:
        print "No motif was found!"

print Direct

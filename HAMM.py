""" Sample: GAGCCTACTAACGGGAT
			CATCGTAATGACGGCCT
	Output: 7"""

a = raw_input()
b = raw_input()
dna = list(a)
dna2 = list(b)
count = 0
d = {'A':'T','T':'A','G':'C','C':'G'}


for i in range(len(dna)):
	q = dna[i]
	if q != dna2[i]:
		count += 1

print count

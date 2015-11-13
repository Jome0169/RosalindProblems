""" 

Sample: AAAACCCGGT
Output: ACCGGGTTTT """

dna = raw_input()
dna2 = list(dna)
dna3 = []

for item in dna2:
	if item == 'A':
		dna3.append('T')
	elif item == 'C':
		dna3.append('G')
	elif item == "G":
		dna3.append("C")
	elif item == "T":
		dna3.append("A")


dna4 = dna3[::-1]
print ''.join(dna4)
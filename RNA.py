""" Sample:GATGGAACTTGACTACGTAAATT
	Output: GAUGGAACUUGACUACGUAAAUU

	Change T to U"""


dna = raw_input()
dnal = list(dna)
dna2 = []

for item in dnal:
	if item == 'T':
		dna2.append('U')
	elif item =='A':
		dna2.append('A')
	elif item == 'C':
		dna2.append('C')
	elif item =='G':
		dna2.append('G')



print "Here She IS!!!!!", "".join(dna2)

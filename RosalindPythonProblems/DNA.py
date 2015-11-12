"""Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective 
number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample:AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Output: 20 12 17 21 """

acount = 0
ccount = 0
tcount = 0
gcount = 0

nuc = raw_input()

for item in nuc:
	if item == "A":
		acount += 1
	elif item == "C":
		ccount += 1
	elif item == 'T':
		tcount += 1
	elif item == 'G':
		gcount +=1
	else:
		acount += 0

print acount, ccount, gcount, tcount

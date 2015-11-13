""" AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"""
"""MAMAPRTEINSTRING"""

x = open('rosalind_prot.txt','r')
rna = x.read().replace('\n', '' ) 

d = {
'UUU':'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC':'V',
'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
'UUG' :'L',      'CUG' :'L',      'AUG' :'M',      'GUG' :'V',
'UCU' :'S',      'CCU' :'P',      'ACU' :'T',      'GCU' :'A',
'UCC' :'S',     'CCC' :'P',      'ACC' :'T',      'GCC' :'A',
'UCA': 'S',      'CCA' :'P',      'ACA' :'T',      'GCA' :'A',
'UCG' :'S',     'CCG' :'P',      'ACG' :'T',      'GCG' :'A',
'UAU' :'Y',      'CAU' :'H',     'AAU' :'N',      'GAU' :'D',
'UAC' :'Y',      'CAC' :'H',      'AAC' :'N',      'GAC' :'D',
'UAA' :'Stop',   'CAA' :'Q',      'AAA' :'K',      'GAA' :'E',
'UAG' :'Stop',   'CAG' :'Q',    'AAG' :'K',      'GAG' :'E',
'UGU' :'C',      'CGU' :'R',      'AGU' :'S',      'GGU' :'G',
'UGC' :'C',      'CGC' :'R',      'AGC' :'S',      'GGC' :'G',
'UGA' :'Stop',   'CGA':'R',      'AGA' :'R',     'GGA' :'G',
'UGG' :'W',      'CGG' :'R',      'AGG' :'R',      'GGG' :'G' }



protein = ""

w = len(rna)
#Takes length of rna


for i in range(0,w,3):
#where 0 is the start, w is the length of the string, and
# 3 is the amount we are increasing by
	stri = rna[i:i+3]
	#slicing of the strong rna where I is taken, and then +3 is added to the next i
	pro = d[stri]
	#looks up the string from stri in the dict
	protein = protein + pro
	# adds the two strings together.

print protein


x.close

fo


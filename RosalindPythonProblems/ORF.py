import itertools
import Bio.Seq  
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna, generic_dna
d = {'UUU':'F', 'CUC':'L','AUC':'I','GUC':'V',
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


#ORF: AUG
#CLOSE : UAA, UAG, UGA

#>Rosalind_99

#MLLGSFRLIPKETLIQVAGSSPCNLS
#M
#MGMTPRLGLESLLE
#MTPRLGLESLLE


with open("rosalind_orf.txt", 'r') as Z:
    DNA1 = Z.read()
    DNA = DNA1.replace("\n", '')
ReverseDNA = Seq(DNA, generic_dna)
FinalReverse = str(ReverseDNA.reverse_complement())

FinalizedProt = []

def ReadingFrameFinder(DNASTRING):
    CleanDNA = DNASTRING.rstrip("\n")
    OpenLocations = []
    CloseLocations = []
    stringlen = len(CleanDNA)
    TtoU = CleanDNA.replace("T", 'U')
    readingframeRange = xrange(0, stringlen)
    PossibleGenes = []
    for item in readingframeRange:
        if TtoU[item:item+3] == "AUG":
            Newthing = xrange(item, stringlen, 3)
            storage = item
            for number in Newthing:
                if TtoU[number:number+3] == "UAA" or TtoU[number:number+3] == "UAG" or TtoU[number:number+3] == "UGA":
                    PossibleGenes.append(TtoU[storage:number+3])
                    break
    for Seqeu in PossibleGenes:
        if len(Seqeu) % 3 == 0:
            LETGO = Seq(Seqeu, generic_rna)
            FinalizedProt.append(str(LETGO.translate()))
        else:
            Removal_Len = len(Seqeu) % 3
            UpdatedSequence = Seqeu[:-Removal_Len]
            ETGO2 = Seq(UpdatedSequence, generic_rna)
            FinalizedProt.append(str(ETGO2.translate()))



def FileWriter(ListOfProt):
    FinalizedProt = set(ListOfProt)
    with open('ProtSeq.txt', 'w') as f:
        for item in FinalizedProt:
            Cutitem = item.replace("*", '')
            f.write(Cutitem)
            f.write("\n")



ReadingFrameFinder(DNA)
ReadingFrameFinder(FinalReverse)
FileWriter(FinalizedProt)

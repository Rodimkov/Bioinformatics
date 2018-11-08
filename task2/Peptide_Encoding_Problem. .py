RNA = {
	'AAA' : 'K', 'AAC' : 'N', 'AAG' : 'K', 'AAU' : 'N', 'ACA' : 'T', 
	'ACC' : 'T', 'ACG' : 'T', 'ACU' : 'T', 'AGA' : 'R', 'AGC' : 'S', 'AGG' : 'R',
	'AGU' : 'S', 'AUA' : 'I', 'AUC' : 'I', 'AUG' : 'M', 'AUU' : 'I', 'CAA' : 'Q',
	'CAC' : 'H', 'CAG' : 'Q', 'CAU' : 'H', 'CCA' : 'P', 'CCC' : 'P', 'CCG' : 'P',
	'CCU' : 'P', 'CGA' : 'R', 'CGC' : 'R', 'CGG' : 'R', 'CGU' : 'R', 'CUA' : 'L',
	'CUC' : 'L', 'CUG' : 'L', 'CUU' : 'L', 'GAA' : 'E', 'GAC' : 'D', 'GAG' : 'E',
	'GAU' : 'D', 'GCA' : 'A', 'GCC' : 'A', 'GCG' : 'A', 'GCU' : 'A', 'GGA' : 'G',
	'GGC' : 'G', 'GGG' : 'G', 'GGU' : 'G', 'GUA' : 'V', 'GUC' : 'V', 'GUG' : 'V',
	'GUU' : 'V', 'UAA' : '', 'UAC' : 'Y', 'UAG' : '', 'UAU' : 'Y', 'UCA' : 'S', 
	'UCC' : 'S', 'UCG' : 'S', 'UCU' : 'S', 'UGA' : '', 'UGC' : 'C', 'UGG' : 'W', 
	'UGU' : 'C', 'UUA' : 'L', 'UUC' : 'F', 'UUG' : 'L', 'UUU' : 'F'
}

def change(mas):
    result = ""
    for i in mas:
        i = i.replace('T', 'U')
        tmp = RNA.get(i)
        result += tmp
    return result
	
		
		
res = []
text = input()
peptide = input()
comp = ['A', 'G', 'C', 'T']

for i in range(len(text) - len(peptide) * 3 + 1):
    Original = []
    Reverse = []
    pattern = text[i:i + len(peptide) * 3]
    string = pattern
    for i in range(len(string)):
        for j in range(4):
            if (string[i] == comp[j]):
                string = string[:i] + comp[3 - j] + string[i+1:]
                break
    reverse = string[::-1]
    
    for i in range(0, len(peptide) * 3, 3):
        Original.append(pattern[i:i+3])
        Reverse.append(reverse[i:i+3])
		
		
    translOr = change(Original)
    translRev = change(Reverse)
    if (translOr == peptide or translRev == peptide):
        res.append(pattern)

res.sort()
for i in res:
    print(i)
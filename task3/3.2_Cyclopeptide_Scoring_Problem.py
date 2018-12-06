

masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}

def add_mass(_subpeptide, _spec_Masses):
	spec_Mass = 0
	for i in _subpeptide:
		spec_Mass += masses.get(i)
	_spec_Masses += [spec_Mass]

def cyclospectrum(peptide):	
	spec_Masses = [0]

	for i in range(1,len(peptide)):
		for j in range(len(peptide)):
			subpeptide = ""
			tail = i if i <= len(peptide) - j else len(peptide) - j
			stump = i - tail
			subpeptide += peptide[j:j+tail]
			subpeptide += peptide[0:stump]
			add_mass(subpeptide, spec_Masses)
	spec_Masses.sort()
	add_mass(peptide, spec_Masses)
	
	return spec_Masses

peptide = input()
spectrum = [int(elem) for elem in input().split()]
#peptide = "NQEL"	
#spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
pep_spectrum = cyclospectrum(peptide)
spec = spectrum.copy()
score = 0
for mass in pep_spectrum:
	if mass in spec:
		spec.remove(mass)
		score += 1
print(score)
masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}

masses_dict = sorted(set(masses.values()))

def add_mass(_subpeptide, _spMasses):
	spMass = 0
	for i in _subpeptide:
		spMass += i
	_spMasses += [spMass]

def peptide_mass(peptide):
	result = 0
	
	for i in peptide:
		result += i
		
	return result

def Cyclospectrum(peptide):	
	spec_Masses = [0]

	for i in range(1, len(peptide)):
		for j in range(len(peptide)):
			subpeptide = []
			tail = i if i <= len(peptide) - j else len(peptide) - j
			stump = i - tail
			subpeptide += peptide[j:j+tail]
			subpeptide += peptide[0:stump]
			add_mass(subpeptide, spec_Masses)

	spec_Masses.sort()
	add_mass(peptide, spec_Masses)

	return spec_Masses

def expand(peptides):	
	result = []

	if not peptides:
			for i in masses_dict:
				result.append([i])
	else:
		for peptide in peptides:
			for i in masses_dict:
				newpeptide = peptide[:]
				newpeptide.append(i)
				result.append(newpeptide)
	return result	

def consistent(peptide, spectrum):
	peptideSpec = [0]

	for i in range(1, len(peptide)):
		for j in range(len(peptide) - i + 1):
			add_mass(peptide[j:j+i], peptideSpec)
	peptideSpec.sort()
	add_mass(peptide, peptideSpec)
	specCpy = spectrum.copy()
	
	for i in peptideSpec:
		if i in specCpy:
			specCpy.remove(i)
		else:
			return False
	if peptide_mass(peptide) in spectrum:
		return True
	else:
		return False
		
def Cyclopeptide_sequencing(spectrum):
	peptides = []
	peptides = expand(peptides)
	while peptides:	
		delete_elem = []
		for peptide in peptides:
			if peptide_mass(peptide) == (spectrum[ len(spectrum) - 1 ]):
				if Cyclospectrum(peptide) == spectrum:
					for i in range(len(peptide)):
						print(peptide[i], end = "-" if i < len(peptide) - 1 else " ")					
				delete_elem.append(peptide)
			elif not consistent(peptide, spectrum):
				delete_elem.append(peptide)			
		for nd in delete_elem:
			peptides.remove(nd)
		if peptides:
			peptides = expand(peptides)
		
#spectrum = [int(elem) for elem in input().split()]
spectrum = [0, 113, 128, 186, 241, 299, 314, 427]
Cyclopeptide_sequencing(spectrum)
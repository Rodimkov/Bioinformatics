masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}

masses_dict = sorted(set(masses.values()))

def add_mass(_subpeptide, _spec_Masses):
	spec_Mass = 0
	for i in _subpeptide:
		spec_Mass += i
	_spec_Masses += [spec_Mass]

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
	
def mass(peptide):
	result = 0
	for i in peptide:
		result += i	
	return result
	
def linear_scoring(peptide, spectrum):
	if not peptide:
		return 0
	pep_spectrum = [0]
	for i in range(1, len(peptide)):
		for j in range(0, len(peptide) - i + 1):
			add_mass(peptide[j:j+i], pep_spectrum)
	pep_spectrum.sort()
	add_mass(peptide, pep_spectrum)
	spec_copy = spectrum.copy()
	score = 0
	for i in pep_spectrum:
		if i in spec_copy:
			spec_copy.remove(i)
			score += 1
	return score
		
def key(spectrum):
	class Key:
		def __init__(self, obj, *args):
			self.obj = obj
		def __lt__(self, other):
			return (linear_scoring(other.obj, spectrum) - linear_scoring(self.obj, spectrum)) < 0
		def __gt__(self, other):
			return (linear_scoring(other.obj, spectrum) - linear_scoring(self.obj, spectrum)) > 0
		def __le__(self, other):
			return (linear_scoring(other.obj, spectrum) - linear_scoring(self.obj, spectrum)) <= 0
		def __ge__(self, other):
			return (linear_scoring(other.obj, spectrum) - linear_scoring(self.obj, spectrum)) >= 0
		def __ne__(self, other):
			return (linear_scoring(other.obj, spectrum) - linear_scoring(self.obj, spectrum)) != 0
		def __eq__(self, other):
			return (linear_scoring(other.obj, spectrum) - linear_scoring(self.obj, spectrum)) == 0
	return Key	
		
def leaderboardcyclopeptidesequencing(spectrum, n):
	
	board = []
	board = expand(board)
	leader = []
	
	while board:	
		delete_elem = []
		for peptide in board:
			if mass(peptide) == spectrum[ len(spectrum) - 1 ]:
				if linear_scoring(peptide, spectrum) > linear_scoring(leader, spectrum):
					leader = peptide

			elif mass(peptide) > spectrum[ len(spectrum) - 1 ]:
				delete_elem.append(peptide)			
		for i in delete_elem:
			board.remove(i)
		sorted_board = sorted(board, key=key(spectrum))
		board = sorted_board[:n]

		for i in sorted_board[n:]:
			if linear_scoring(i, spectrum) == linear_scoring(board[-1], spectrum):
				board.append(i)
			else:
				break
		if board:
			board = expand(board)
		
	return leader

#N = int(input())
masses_dict = sorted(set(masses.values()))
N = 9
spectrum = [int(elem) for elem in input().split()]
pr = leaderboardcyclopeptidesequencing(spectrum, N)
for i in range(len(pr)):
	print(pr[i], end = "-" if i < len(pr) - 1 else " ")


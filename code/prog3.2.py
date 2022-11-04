#!/usr/bin/python 

from __future__ import with_statement
import re

__title__ = "Secondary structure and pairwise DP profile-profile alignment"
__author__ = "Carlos P Cantalapiedra"
__institution__ = "CSIC AulaDei Bioinformatics Dept."

### MAIN STARTS UNDERNEATH THE FUNCTIONS ###

# Function that parses PSSM files
#	The format of the array is:
#	pssm[
#	{'aa':aa1, 'weights', [w1, w2, ...]},
#	{'aa':aa2, 'weights', [w1, w2, ...]},
#	.
#	.
#	.
#	]
def read_PSSM(pssm_file):
    pssm = [] # Returning dictionary
    aa = ''
    weights = []
    
    # Finds the aminoacid (\w) and his weights ((\s*-?\d*.\d*)+)
    reg_exp = re.compile(r"^\s*\d+\s+(\w)((\s*-?\d*.\d*)+)")
    
    # NOTE: with the with_statement there's no need to close the file
    with open(pssm_file, 'r') as file:
        for line in file:
            result = reg_exp.search(line)
	    
            if result:
                try:
                    aa = result.group(1)
                    weights = str(result.group(2)).split()

                except IndexError:
                    raise IOError("There is a problem with the format of the PSSM file "+str(pssm_file))
		
                pssm.append({'aa' : aa, 'weights' : weights})
    return pssm

# Function that parses "Pred:" line of PSIPRED files,
#	to obtain the predicted secondary structures
def read_PSIPRED(psipred_file):
    psipred = []
    
    reg_exp = re.compile(r"^\s*Pred:\s*(\w+)")
    
    # NOTE: with the with_statement there's no need to close the file
    with open(psipred_file, 'r') as file:
        for line in file:
            result = reg_exp.search(line)
	    
            if result:
                try:
                    [psipred.append(a) for a in result.group(1)]
		    
                except IndexError:
                    raise IOError("There is a problem with the format of the PSIPRED file "+str(psipred_file))
	    
    return psipred

# Function that returns the bonus score associated to secondary structure
def get_secondary_score(st1, st2):
    global secondary_score
    score = 0
    
    if st1 == st2 and st2 != 'C':
        score = secondary_score

    return score

# Function that creates de Dynamic Programming matrix
# 	The format of the matrix is going to be:
# 	matrix[
# 		row(0) [('r', gap), ('r', gap), ..., ('r', gap)] # len(row) = len(prot2) + 1
# 		row(1) [('c', gap), (path, score), ..., (path,score)]
#		row(2) [('c', gap), (path, score), ..., (path,score)]
# 		.
# 		.
# 		.
# 		row(len(prot1)) [('c', gap), (path, score), ..., (path, score)]
# 		# len(col) = len(prot1) + 1
#	]
# 
def create_matrix_DP(pssm1, pssm2, psipred1, psipred2):
    global aa_order
    global gapcost
    
    matrix_DP = [] # Returning matrix
    scores = []
    score = 0
    score1 = 0 # score1 and score2 serve several purposes
    score2 = 0
    aa1_count = 0 # 2 indexes
    aa2_count = 0
    path = '' # 'd': diagonal, 'c': column, 'r': row
    
    try:
	
        # Fisrt row is set up with gap values
        init_row = [('r', i * gapcost) for i in range(0, len(psipred2) + 1)]
        matrix_DP.append(init_row)
	
        for aa1 in pssm1:
            aa1_count+=1
	    
            index1 = aa_order.index(aa1['aa']) # aa1 position in PSSM columns
	    
            scores = []
            aa2_count = 0
	    
            for aa2 in pssm2:
                aa2_count+=1
		
                # First column is set up with gap values
                if aa2_count == 1:
                    scores.append(('c', aa1_count * gapcost))
		
                index2 = aa_order.index(aa2['aa'])
		
                score1 = int(aa2['weights'][index1])
                score2 = int(aa1['weights'][index2])
		
                score = (score1 + score2) / 2.0
                score += get_secondary_score(psipred1[aa1_count-1], psipred2[aa2_count-1])
		    
                # Now does apply the function for matrix positions:
                #	Sij = max (score(-1,-1)+score, score(-1,0)+gap, score(0,-1)+gap)
                score += matrix_DP[aa1_count - 1][aa2_count - 1][1] # [1] is the score in the tuple (path, score)
                score_1 = matrix_DP[aa1_count - 1][aa2_count][1] + gapcost
                score_2 = scores[aa2_count - 1][1] + gapcost
		    
                if score_1 >= score and score_1 >= score_2:
                    path = 'c' # Column
                    score = score_1
			
                elif score_2 >= score:
                    path = 'r' # Row
                    score = score_2
			
                else:
                    path = 'd' # Diagonal
		    
                # Adds the score to the list of current row
                scores.append((path, score))
		    
            # Adds a row of scores
            matrix_DP.append(scores)
	    
    except ValueError as value:
        raise Exception("Error. Maybe there is a rare aminoacid in the PSSM.\n"+value)
    except IndexError as value:
        raise Exception("Error. "+str(value))

    return matrix_DP

# Recursive function that recovers the alignment
def visit_alignment(i, j, output):
    global matrix_DP # This could be changed to be a parameter by reference
    global prot1_pssm, prot2_pssm, prot1_psipred, prot2_psipred
    
    if i == 0 and j == 0: return # END OF RECURSIVE SEARCH
    
    join = ' '
    if prot1_pssm[i - 1]['aa'] == prot2_pssm[j - 1]['aa']: join = '|'
    
    path = matrix_DP[i][j][0]
    score = matrix_DP[i][j][1]
    
    if path == 'd':
        visit_alignment(i - 1, j - 1, output)
        output.append((prot1_psipred[i - 1], prot1_pssm[i - 1]['aa'], join, prot2_pssm[j - 1]['aa'], prot2_psipred[j - 1]))
	
    elif path == 'c':
        visit_alignment(i - 1, j, output)
        output.append((prot1_psipred[i - 1], prot1_pssm[i - 1]['aa'], join, '-', '-'))
	
    elif path == 'r':
        visit_alignment(i, j - 1, output)
        output.append(('-', '-', join, prot2_pssm[j - 1]['aa'], prot2_psipred[j - 1]))
	
    else:
        raise Exception("Invalid path "+path)
    
    return


############################ MAIN ##################################

# Global variables: program parameters
aa_order = ('ARNDCQEGHILKMFPSTWYV'); # This must copy aa order in PSSM columns
gapcost = -8
secondary_score = 2

# File locations: please, change this variables to suit your needs
prot1_pssm_file = './files/1ngk_A.pssm'
prot2_pssm_file = './files/1s69_A.pssm'
prot1_psipred_file = './files/1ngk_A.psipred'
prot2_psipred_file = './files/1s69_A.psipred'

# Printing title and author
print()
print("*** "+__title__+" ***")
print("Author: "+__author__+" at "+__institution__)

# Printing parameters
print()
print("Aminoacids and order (PSSM files): "+aa_order)
print("Gap penalty = "+str(gapcost))
print("Equal secondary structure score = "+str(secondary_score))

### 1) Opening and parsing PSSM and PSIPRED files

prot1_pssm = []
prot2_pssm = []
prot1_psipred = []
prot2_psipred = []

try:
    print()
    prot1_pssm = read_PSSM(prot1_pssm_file)
    prot2_pssm = read_PSSM(prot2_pssm_file)
    print("> PSSM files successfully opened.")
    
    prot1_psipred = read_PSIPRED(prot1_psipred_file)
    prot2_psipred = read_PSIPRED(prot2_psipred_file)
    print("> PSIPRED files successfully opened.")
    
except IOError as value:
    print("There has been an error reading input files:")
    print(value)

### 2) Creating the matrix of DP

matrix_DP = [[]]
len_prot1 = len(prot1_psipred)
len_prot2 = len(prot2_psipred)

try:
    matrix_DP = create_matrix_DP(prot1_pssm, prot2_pssm, prot1_psipred, prot2_psipred)
    
except Exception as value:
    print(value)

### 3) Printing the maximum score

print()
print("Maximum score "+str(matrix_DP[len_prot1][len_prot2][1]))

### 4) Recovering and printing the alignment

output = [] # [(ss1, aa1, align, aa2, ss2)]
# Lines to print
ss1 = ''
aa1 = ''
align = ''
aa2 = ''
ss2 = ''

try:
    # Recursively recovering the alignment
    visit_alignment(len_prot1, len_prot2, output)
    
    # Printing the alignment
    print()
    for nts in output:
        ss1 += str(nts[0])
        aa1 += str(nts[1])
        align += str(nts[2])
        aa2 += str(nts[3])
        ss2 += str(nts[4])
    print(ss1)
    print(aa1)
    print(align)
    print(aa2)
    print(ss2)
    
except Exception as value:
    print("Error while tracing the alignment.")
    print(value)
else: # END OF PROGRAM
    print()
    print("*** Alignment finished successfully ***")

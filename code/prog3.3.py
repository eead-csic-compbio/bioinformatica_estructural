#!/usr/bin/env python
""" prog3.3 Construye un modelo sin gaps ni rotameros una secuencia problema (query) 
en base a las coordenadas del model (pdb2) en base a un alineamiento. 
Genera un fichero PDB con el modelo comparativo resultante."""

__author__  = 'Bruno Contreras-Moreira' 

from math import exp

# 0) parametros del algoritmo: 
query = { 'align':'KVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQIN' +
	'SRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV' };

molde = { 'file':'./files/1gd6.pdb', 
	'align':'KTFTRCGLVHELRKHGFEEN---LMRNWVCLVEHESSRDTSKTNTNR-NGSKDYGLFQIN' +
	'DRYWCSKGASPG--KDCNVKCSDLLTDDITKAAKCAKKIYKR-HRFDAWYGWKNHCQG--SLPDISSC--' };

# 1) subrutinas
def lee_coordenadas_PDB(filename):
	""" Devuelve una lista de residuos, cada uno con las coordenadas de sus atomos. 
	Ejemplo de linea en formato PDB:
	ATOM     42  CA  PHE X   3       6.981  22.274  18.887  1.00  6.72 """
	
	coords = []
	pdbfile = open(filename,'r')
	try:
		res,prev_resID = '',''
		for line in pdbfile:
			if(line[0:3] == 'TER'): break
			if(line[0:4] != 'ATOM'): continue
			resID = line[17:26]
			if(resID != prev_resID):
				if(res != ''): coords.append(res)
				res = line
			else: res += line	
			
			prev_resID = resID
		
		if(res != ''): coords.append(res)		
	finally:
		pdbfile.close()	
	return coords	

def copia_coords_alineadas(align1,align2,coords_molde,PDBname):
	""" Devuelve:
	1) una lista con las coordenadas de coords_molde 
	que se pueden copiar segun el alineamiento align1,align2. 
	2) una estimacion del RMSD segun la curva RMSD(A) = 0.40 e^{l.87(1-ID)} 
	de  Chothia & Lesk (1986) """
	
	aanames = { "A":"ALA","C":"CYS","D":"ASP","E":"GLU","F":"PHE","G":"GLY",
		"H":"HIS","I":"ILE","K":"LYS","L":"LEU","M":"MET","N":"ASN","P":"PRO",
		"Q":"GLN","R":"ARG","S":"SER","T":"THR","V":"VAL","W":"TRP","Y":"TYR" }

	rmsd,identical = 0,0
	total1,total2,total_model = -1,-1,0
	length = len(align1)
	
	if(length != len(align2)): 
		print "# copia_coords_alineadas: alineamientos tienen != longitud",
		return []
	
	pdbfile = open(PDBname, 'w')
	print >> pdbfile, "HEADER comparative model\nREMARK alignment:\n",
	print >> pdbfile, "REMARK query   : %s\n" % (align1),
	print >> pdbfile, "REMARK template: %s\n" % (align2),
	
	for r in range(0, length):
		conserved = False
		res1 = align1[r:r+1]
		res2 = align2[r:r+1]
		if(res1 != '-'): total1+=1
		if(res2 != '-'): total2+=1
		if(res1 == '-' or res2 == '-'): continue # salta los gaps
		total_model += 1.0;
		if(res1 == res2): 
			conserved = True
			identical += 1.0
		for atomo in coords_molde[total2].split("\n"):
			if(atomo == ''): break
			if(atomo[12:16] == ' CA ' or atomo[12:16] == ' C  ' or \
				atomo[12:16] == ' N  ' or atomo[12:16] == ' O  ' \
				or conserved):
				print >> pdbfile, "%s%s%s%4d%s" % \
				(atomo[0:17],aanames[res1],atomo[20:22],total1+1,atomo[26:])	
		
	print >> pdbfile, "TER\n",
	pdbfile.close()	
	
	rmsd = 0.40 * exp(1.87*(1-(identical/total_model)))
	identical = (identical/total_model)
	
	return (total_model,identical,rmsd)
	
# 2) programa principal 

molde['coords'] = lee_coordenadas_PDB( molde['file'] )
		
print "# total residuos en estructura molde : %s\n" % (len(molde['coords'])),

(long_modelo,identidad,rmsd) = copia_coords_alineadas(query['align'],
				molde['align'],molde['coords'],'modelo.pdb' )

print "# archivo PDB = modelo.pdb longitud modelo (residuos) = %d \n" % long_modelo,
print "# identidad = %1.0f%% RMSD estimado = %1.2f ansgtrom\n" % (100*identidad,rmsd),



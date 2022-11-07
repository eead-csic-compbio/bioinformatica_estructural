#!/usr/bin/env python

from __future__ import print_function

""" prog4.3 Toma un complejo proteina-DNA en formato PDB y hace una simulacion de docking,
    devolviendo un archivo PDB.
    Ejemplo inspirado en codigo de https://www.pyrosetta.org/documentation/scripts
    Para mas detalles y para actualizar el codigo segun se actualiza Rosetta ver: 
    https://www.pyrosetta.org/documentation """

__author__  = 'Bruno Contreras-Moreira' 

import os,re
from rosetta import *
from pyrosetta import *

complexfile    = './files/1j1v_withH.pdb'
tmpfile        = 'tmp.rosetta'
prefijo_salida = 'docking_output' # define nombre de archivos generados, ver 2.5
intentos       = 10

## 1) subrutinas
def PDB2Rosetta(ficheroPDB,ficheroRosetta):
	"""Lee un fichero PDB y crea otro con el formato adecuado para Rosetta.
	ATOM    508  OP1 DA    213       0.287  26.129   7.841  1.00  0.00 # original
	ATOM   5389  O5*   A C -10      30.936 109.878 105.387  1.00  0.00 # Rosetta """
	
	coords,num_cambios = [],0
	
	# 1) lee coordenadas PDB
	pdbfile = open(ficheroPDB,'r')
	try:
		for line in pdbfile:
			if(line[0:4] == 'ATOM'):
				if(line[15:16] == "\'"): 
					line = line[0:15] + '*' + line[16:]
					num_cambios += 1
				if(line[17:19] == " D"): 
					line = line[0:18] + ' ' + line[19:]
					num_cambios += 1
				coords.append(line)
			else: coords.append(line)
			
			
	finally:
		pdbfile.close()	
		
	# 2) escribe archivo en formato corregido
	rfile = open(ficheroRosetta, 'w')
	for line in coords: 
		if(line[0:6] == 'HEADER'):
			line += "REMARK reformatted for Rosetta\n"	
		print >> rfile, "%s" % (line),
	rfile.close()	

	return num_cambios

def Rosetta2PDB(ficheroRosetta,ficheroPDB):
	"""Lee un fichero Rosetta y crea otro con formato PDB.
	ATOM    508  OP1 DA    213       0.287  26.129   7.841  1.00  0.00 # original
	ATOM   5389  O5*   A C -10      30.936 109.878 105.387  1.00  0.00 # Rosetta """
	
	coords,num_cambios = [],0
	
	# 1) lee coordenadas de Rosetta
	patronNT = re.compile('  ([A|C|G|T|U])')
	rfile = open(ficheroRosetta,'r')
	try:
		for line in rfile:
			if(line[0:4] == 'ATOM'):
				if(line[15:16] == "*"): 
					line = line[0:15] + "'" + line[16:]
					num_cambios += 1
				
				match = patronNT.match(line[17:20]) 
				if match: 
						line = line[0:18] + 'D' + line[19:]
						num_cambios += 1
				coords.append(line)
			else: coords.append(line)
	finally:
		rfile.close()	
		
	# 2) escribe archivo en formato PDB
	pdbfile = open(ficheroPDB, 'w')
	for line in coords: 
		if(line[0:6] == 'HEADER'):
			line += "REMARK PDB reformatted from Rosetta coordinates\n"	
		print("%s" % (line), file=pdbfile)
	pdbfile.close()	

	return num_cambios


## 2) programa principal 
num_cambios = PDB2Rosetta( complexfile, tmpfile )
print("# convierto complejo %s en %s (%d cambios)\n\n" % (complexfile,tmpfile,num_cambios))

	
# 2.1) inicia Rosetta y lee conformacion de partida
init()
p = Pose()
pose_from_pdb(p,tmpfile)

# 2.2) prepara docking y guarda pose inicial
DockingProtocol().setup_foldtree(p, 'A_BC')
dock_jump = 2 # en las coordenadas la proteina A aparece en tercera posicion,
              # asi especificamos que trate como un todo al DNA (BC) para hacer
			  # docking contra A		
p_entrada = Pose()
p_entrada.assign(p)

# 2.3) define esquema de evaluacion de mecanica molecular
funcion_eval = create_score_function('dna')

# 2.4) calcula perturbacion rigida arbitraria e inicia motores de giro y movimiento
perturbacion = RigidBodyPerturbMover(dock_jump, 2, 15) #traslacion de 3Ansgtrom y rotacion de 8 grados
spin = RigidBodySpinMover( dock_jump )
slide_into_contact = FaDockingSlideTogether( dock_jump )

# 2.5) inicia motor de docking y ejecuta N simulaciones
# docking de alta resolucion, para parejas cercanas en el espacio:
#High-resolution, all-atom based MCM search with rigid-body moves, side-chain packing and minimization
# en contraste con docking de baja resolucion:
# Low-resolution, centroid based MC search (50 RigidBodyPerturbMoves with adaptable step sizes)

print("comienzo docking (%d simulaciones MonteCarlo)..." % (intentos))
docking_highres = DockingHighRes(funcion_eval, dock_jump)
jd = PyJobDistributor(prefijo_salida, intentos, funcion_eval) 
while (jd.job_complete == False):
	
	p.assign(p_entrada) # copia conformacion/pose inicial

	perturbacion.apply(p) # aplica perturbacion rigida calculada en 2.4
	spin.apply(p)
	slide_into_contact.apply(p)
	
	docking_highres.apply(p) # ejecuta algoritmo de docking

	jd.output_decoy(p) # imprime PDB de esta simulacion de docking 


# 2.6) comprueba resultados y reformatea coordenadas generadas a PDb
patron = re.compile('filename:\s+(\S+)\s+total_score:\s+(\S+)')
fichero_resumen = prefijo_salida + '.fasc'

if(os.path.isfile(fichero_resumen) == True):

	print("\n# resultados en %s :\n\n" % (fichero_resumen))

	salida = open(fichero_resumen,'r')
	for line in salida: 
		match = patron.match(line) 
		if match: 
				rosetta_outfile = match.group(1)
				pdb_outfile = rosetta_outfile # sobreescribe archivo de salida de Rosetta
				Rosetta2PDB(rosetta_outfile,pdb_outfile)
				print("> %s valoracion: %f\n" % (pdb_outfile,float(match.group(2))))
			
	salida.close()	


# 2.7) limpieza
os.unlink(tmpfile)

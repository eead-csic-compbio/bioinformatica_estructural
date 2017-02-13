#!/usr/bin/env python
""" Toma un complejo proteina-DNA en formato PDB y pone los H faltantes con open babel."""

__author__  = 'Bruno Contreras-Moreira' 

import os,sys,getopt,subprocess

BABELEXE = '/usr/bin/babel' # get it from http://openbabel.org 
							# edit according to your settings

##################################################################

# 1) subrutinas
def lee_cadenas_ficheroPDB(filename):
	""" Devuelve una lista con las coordenadas de cada una de las cadenas de un PDB
	ATOM      1  O5'  DT B 101      19.688  25.517   6.033 """
	
	cadenas = []
	pdbfile = open(filename,'r')
	try:
		cadena,chainID,prev_chainID = '','',''
		for line in pdbfile:
			if(line[0:4] != 'ATOM'): continue
			chainID   = line[21:22]
			if(cadena != '' and chainID != prev_chainID):
				cadenas.append(cadena)
				cadena = line
			else: cadena += line
			prev_chainID = chainID
		if(cadena != ''): cadenas.append(cadena)	
			
	finally:
		pdbfile.close()	
		
	return (cadenas)
	
def completa_H_cadenas(cadenas):
	"""Completar hidrogenos en cada una de las cadenas de coordenadas PDB, invocando
	open babel, que se encuentra donde dice la variable global BABELEXE. 
	ATOM   1743  H   DA    213      10.209  27.873   5.653 """
		
	Hcadenas,natoms = [],1
		
	for cadena in cadenas:
		Hcadena = ''
		tmpfile = '__' + cadena[21:22]
		tmpfile2= '__' + cadena[21:22] + '.H'
		file1 = open(tmpfile, 'w')
		print >> file1, "HEADER chain coordinates for babel\n",
		print >> file1, "%s" % (cadena),
		file1.close()	
		subprocess.Popen([BABELEXE,'-h','-iPDB',tmpfile,'-oPDB',tmpfile2]).wait()
		
		# lee coordenadas originales, conservan chainID
		coords = {}
		file1 = open(tmpfile,'r')
		try:
			for line in file1:
				if(line[0:4] != 'ATOM'): continue
				resID = line[22:26]
				if(resID in coords): coords[resID] += line
				else: coords[resID] = line
		finally:
			file1.close()	
			
		# lee salida de babel
		Hcoords = {}
		file2 = open(tmpfile2,'r')
		try:
			for line in file2:
				if(line[0:4] != 'ATOM'): continue
				if(line[13:14] != 'H'): continue
				resID = line[22:26]
				if(resID in Hcoords): Hcoords[resID] += line
				else: Hcoords[resID] = line
		finally:
			file2.close()	
		
		# agrupa hidrogenos en sus respectivos residuos y corrige formato PDB
		resIDs = coords.keys()
		resIDs.sort( lambda x,y: int(x)-int(y) )
		for resID in resIDs:
			reschain = coords[resID][17:22]
			
			(res,natoms) = renumera_atomos(coords[resID],natoms)
			Hcadena += res
			
			Hres = ''
			for at in Hcoords[resID].split("\n"):
				if(at == ''): break
				Hatom = at[0:17] + reschain + at[22:] + "\n"
				Hres += Hatom
			
			(res,natoms) = renumera_atomos(Hres,natoms)
			Hcadena += res
					
		Hcadenas.append(Hcadena)
		
		os.unlink(tmpfile)
		os.unlink(tmpfile2)
		
	return Hcadenas	
	
def renumera_atomos(res,total_provisional):
	""" Renumera los atomos de un residuo a partir de total_provisional y
	devuelve una cadena de caracteres con el residuo renumerado y la cuenta
	total actualizada."""
	
	res_renum,updated_total = '',total_provisional
	
	for atomo in res.split("\n"):
		if(atomo == ''): continue
		res_renum += "ATOM   %4d %s\n" % (updated_total,atomo[12:])
		updated_total += 1
	return (res_renum,updated_total)
	
## 2) programa principal
INPinpdb = INPoutpdb = ''
usage = """usage : 
   -h  this help message
   -i  input PDB file with coordinates of protein-DNA complex
   -o  output PDB file with coordinates of protein-DNA complex with added Hs"""

try:                                
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ['help','in_PDB_file','out_PDB_file'])      
		
	if not opts: 
		print usage                     
		sys.exit(0)		
		
	for opt, arg in opts: 
		if opt in ("-h", "--help"):
			print usage                     
        		sys.exit(0)
		elif opt in ("-i", "--in_PDB_file"): INPinpdb = arg
		elif opt in ("-o", "--out_PDB_file"): INPoutpdb = arg

	if(INPinpdb == '' or INPoutpdb == ''): 
		print usage                     
		sys.exit(0)	
	
except getopt.GetoptError:          
	print usage                         
	sys.exit(2)    
	
print "# %s -i %s -o %s\n" % (sys.argv[0],INPinpdb,INPoutpdb)	  

cadenasPDB = lee_cadenas_ficheroPDB( INPinpdb )
print "# %s contiene %d cadenas\n" % (INPinpdb,len(cadenasPDB)),

cadenasH = completa_H_cadenas(cadenasPDB)

outfile = open(INPoutpdb, 'w')
print >> outfile, "HEADER %s renumbered with added hydrogens (open babel)\n" % (INPinpdb),
for cadena in cadenasH:	
	print >> outfile, "%sTER\n" % (cadena),
outfile.close()	

print "# generated outfile %s\n" % (INPoutpdb)

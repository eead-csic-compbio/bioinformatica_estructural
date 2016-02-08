#!/usr/bin/python 

""" prog3.4 Calcula la informacion mutua entre columnas 
de un alineamiento multiple en formato FASTA. """

__author__  = 'Bruno Contreras-Moreira' 

# 0) parametros del algoritmo: 
pdb1 = { 'file':'./files/1gd6.pdb', 
	'align':'KTFTRCGLVHELRKHGFEEN---LMRNWVCLVEHESSRDTSKTNTNR-NGSKDYGLFQIN' +
	'DRYWCSKGASPG--KDCNVKCSDLLTDDITKAAKCAKKIYKR-HRFDAWYGWKNHCQG--SLPDISSC--' };

pdb2 = { 'file':'./files/2nwd.pdb', 
	'align':'KVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQIN' +
	'SRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV' };
	
# 1) subrutinas
def extract_fasta_headers(fasta_path, headers_list, tmp_files_dir):
    new_fasta_path = ""
    
    headers_set = set(headers_list)
    
    input_file = None
    try:
        (file_desc, new_fasta_path) = tempfile.mkstemp(suffix="_m2p_facade", dir=tmp_files_dir)
        input_file = os.fdopen(file_desc, 'w')
        
        seq_found = False
        fasta_headers = get_fasta_headers(fasta_path)
        for line in open(fasta_path):
            if line.startswith(">"):
                seqid = line[1:].strip().split(" ")[0] # To ensure that only identifier (and no fasta comments) are compared:
                if seqid in headers_set:
                    seq_found = True
                    input_file.write(line)
                else:
                    seq_found = False
                    
            elif seq_found:
                input_file.write(line)
                
        input_file.close()
        
    except Exception:
        raise
    finally:
        if input_file:
            input_file.close()
    
    return new_fasta_path



# 2) programa principal ###################################################

MSAsequences = readFASTA_file( pdb1['file'] )

		
print "# total residuos: pdb1 = %s pdb2 = %s\n" % (len(pdb1['coords']),len(pdb2['coords'])),

(pdb1['align_coords'],pdb2['align_coords']) = coords_alineadas(pdb1['align'],pdb1['coords'],\
						pdb2['align'],pdb2['coords'] )

print "# total residuos alineados = %s\n" % (len(pdb1['align_coords'])),

rmsd = calcula_superposicion_SVD(pdb2,pdb1,'original.pdb','align_fit.pdb')

print "\n# coordenadas originales = original.pdb\n# superposicion optima:\n", 
print "# archivo PDB = align_fit.pdb\n# RMSD = %1.2f Angstrom\n" % (rmsd),

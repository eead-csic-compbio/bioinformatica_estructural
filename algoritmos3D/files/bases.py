""" mean coordinates from 2094 bases date=Fri Oct  2 10:50:44 2009 """

__author__  = 'Bruno Contreras-Moreira with help from Vladimir Espinosa Angarica' 

def dna_base_coords(base):
	""" Devuelve una cadena de caracteres con las coordenadas de la
	base nitrogenada de DNA requerida"""
	
	coords_string = ''
	
	if(base == 'A'):
		coords_string = """ATOM     12  N9   DA A   1       0.000   0.000   0.000
ATOM     13  C8   DA A   1      -0.373   1.320   0.000
ATOM     14  N7   DA A   1       0.638   2.156  -0.002
ATOM     15  C5   DA A   1       1.753   1.330  -0.003
ATOM     16  C6   DA A   1       3.133   1.602  -0.005
ATOM     17  N6   DA A   1       3.642   2.836  -0.011
ATOM     18  N1   DA A   1       3.981   0.551  -0.001
ATOM     19  C2   DA A   1       3.469  -0.687   0.002
ATOM     20  N3   DA A   1       2.192  -1.069   0.002
ATOM     21  C4   DA A   1       1.376   0.000   0.000"""
		
	elif(base == 'C'):
		coords_string = """ATOM     12  N1   DC A   1       0.000   0.000   0.000
ATOM     13  C2   DC A   1       1.401   0.000   0.000
ATOM     14  O2   DC A   1       2.004  -1.082  -0.005
ATOM     15  N3   DC A   1       2.060   1.182   0.006
ATOM     16  C4   DC A   1       1.378   2.329   0.010
ATOM     17  N4   DC A   1       2.072   3.469   0.016
ATOM     18  C5   DC A   1      -0.049   2.357   0.006
ATOM     19  C6   DC A   1      -0.690   1.181   0.000"""
		
	elif(base == 'G'):
		coords_string = """ATOM     12  N9   DG A   1       0.000   0.000   0.000
ATOM     13  C8   DG A   1      -0.382   1.320   0.000
ATOM     14  N7   DG A   1       0.627   2.150   0.004
ATOM     15  C5   DG A   1       1.746   1.326   0.004
ATOM     16  C6   DG A   1       3.127   1.652   0.009
ATOM     17  O6   DG A   1       3.650   2.772   0.011
ATOM     18  N1   DG A   1       3.928   0.515   0.011
ATOM     19  C2   DG A   1       3.457  -0.774   0.008
ATOM     20  N2   DG A   1       4.383  -1.743   0.014
ATOM     21  N3   DG A   1       2.171  -1.093   0.000
ATOM     22  C4   DG A   1       1.376   0.000   0.000"""
		
	elif(base == 'T'):
		coords_string = """ATOM     12  N1   DT A   1       0.000   0.000   0.000
ATOM     13  C2   DT A   1       1.380   0.000   0.000
ATOM     14  O2   DT A   1       2.050  -1.019   0.005
ATOM     15  N3   DT A   1       1.957   1.245  -0.004
ATOM     16  C4   DT A   1       1.305   2.461  -0.008
ATOM     17  O4   DT A   1       1.948   3.506  -0.018
ATOM     18  C5   DT A   1      -0.139   2.391  -0.001
ATOM     19  C7   DT A   1      -0.937   3.658   0.009
ATOM     20  C6   DT A   1      -0.714   1.180   0.000"""

	return coords_string

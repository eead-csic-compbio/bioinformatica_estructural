from modeller.automodel import *   

log.verbose()    
env = environ() 

# 1) directorio donde se encuentran los ficheros con coordenadas de moldes/templates, 
# con extension .pdb,.atm,.ent
env.io.atom_files_directory = './templates/'

# 2) prepara el modelado
a = automodel(env,
              alnfile  = 'alineamiento.ali',  # fichero con el alineamiento
              knowns   = '1PDB',              # nombre del template como aparece en alnfile
              sequence = 'query',             # nombre de secuencia problema como aparece en alnfile
              assess_methods=(assess.DOPE))      

a.starting_model= 1                           # define cuantos modelos diferentes quieres
a.ending_model  = 2                 
                  
# 3) accion! 
a.make()

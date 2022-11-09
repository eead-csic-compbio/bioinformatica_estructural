TEORÍA: Fundamentos de estructura de macromoléculas {#macro1}
===================================================

Papel biológico de las macromoléculas: relación entre secuencia, estructura y función
-------------------------------------------------------------------------------------

Los ácidos nucleicos y las proteı́nas son las dos macromoléculas biológicas más importantes. Ambas son los canales principales de los flujos de información genómica dentro de la célula, que convierten en acciones moleculares el legado genético acumulado. Sabemos que el ácido desoxirribonucleico (ADN) puede guardar información genética a largo plazo, mientras que el ácido ribonucleico (ARN) lo hace normalmente a muy corto plazo. Son las proteı́nas, y algunas clases especiales de ARN, quienes convierten en el contexto celular esa información en acción. Para comprender cómo realizan estas funciones es muy importante tener una idea de su estructura molecular. Esto debemos tenerlo siempre en cuenta en el ámbito bioinformático, donde a veces hablamos de genes y proteı́nas como entidades abstractas cuya función es sólo un verbo.

![ [Figura](#fig:flujosinfobio). Flujos moleculares de información en la célula. Los flujos azules solamente se encuentran en algunos seres vivos, las negras son universales. ](fig/flujoinfo.png){#fig:flujosinfobio width="80%"}

La función biológica de estas moléculas está ı́ntimamente ligada a su estructura. Por ejemplo, la estructura en doble hélice del ADN es en si mismo un mecanismo de protección de la información genética, ya que la información está contenida por duplicado, y asimismo es la base de su mecanismo de replicación.

![ [Figura](#fig:dna). Estructura helicoidal del ADN (DNA en inglés) en conformaciones A, B y Z. Figura de dominio público tomada de <https://en.wikipedia.org/wiki/Nucleic_acid_structure>. ](fig/dna.png){#fig:dna width="100%"}

Las macromoléculas naturales deben plegarse, es decir, deben tomar una determinada conformación tridimensional relativamente estable para desempeñar su función biológica. A esta conformación, sostenida por una red de interacciones no covalentes, se le llama *nativa* (ver sección [1.2.3](#macro1:intnocov){reference-type="ref" reference="macro1:intnocov"}). Por el contrario, las moléculas se despliegan al perderse estas interacciones. Cuando una macromolécula pierde su estructura tridimensional nativa, normalmente pierde también su función. O al menos antes lo creíamos así. Ahora conocemos cada vez más proteı́nas intrı́nsecamente desordenadas no plegadas, que participan en complejos proteicos o que sólo se pliegan al unirse a sus ligandos y reducir su entropía [@Flock2014; @Riback2017], que desempeñan funciones celulares importantes [@Dyson1999]. Recientemente hay mucho interés en estudiar estos fenómenos por su relación con la complejidad de los organismos [@Yruela2017] y con proteínas de importancia en medicina como los [priones](http://es.wikipedia.org/wiki/Prion) [@Sabate2015].

![ [Figura](#fig:autoinhdis). Algunas regiones desordenadas tienen un rol autoinhibitorio, como el fragmento en color rosa de la figura. Figura tomada de [@Trudeau2013] y reproducida con permiso de los autores. ](fig/disorderautoinhib.png){#fig:autoinhdis width="70%"}

Componentes y enlaces
---------------------

Proteı́nas y ácidos nucleicos pueden considerarse polı́meros, moléculas generadas por la sucesión de monómeros elegidos de un repertorio limitado. En ambos casos la secuencia de monómeros da la especificidad biológica a cada macromolécula. En el caso de las proteı́nas los monómeros son aminoácidos y el repertorio incluye [generalmente](http://en.wikipedia.org/wiki/Proteinogenic) 20 distintos. Por otro lado, los ácidos nucleicos están compuestos por nucleótidos (ver sección [1.2.2](#nts){reference-type="ref" reference="nts"}).

### El enlace peptı́dico y los aminoácidos

Los 20 aminoácidos que forman parte de las proteı́nas naturales están compuestos por un grupo amino y uno carboxilo unidos por el carbono $\alpha$, del que parten diferentes cadenas laterales (R, ver figura [1.4](#fig:aminostereo){reference-type="ref" reference="fig:aminostereo"}). La cadena lateral R diferencia a los 20 aminoácidos y les confiere propiedades quı́micas especı́ficas [@yruela_inmaculada_2014_1067867].

![ [Figura](#fig:aminostereo}). Estructura quı́mica de los L-aminoácidos. En el panel de la derecha se muestra su polaridad, con grupos con cargas positivas (en azul) y negativas (en rojo). ](fig/amino_stereo.jpg){#fig:aminostereo}

![ [Figura](#fig:aminoclassif). Clasificación de los 20 aminoácidos naturales,tomada de <http://www.russelllab.org/aas>. La selenocisteı́na, que contiene un átomo de Se en vez de S, se considera el aminoácido 21 [@Santesmasses2017; @Granold2018]. ](fig/amino_classif.jpg){#fig:aminoclassif width="50%"}

![ [Figura](#fig:bipA}). L-4,4'-bifenilalanina, un aminoácido no natural empleado en biotecnología. Figura tomada de <http://www.chemicalbook.com>. ](fig/bipA.jpg){#fig:bipA}

Los aminoácidos se encadenan por medio de enlaces peptı́dicos para formar proteı́nas, también llamadas cadenas polipeptı́dicas, como se muestra en la figura [1.7](#fig:peptidebond){reference-type="ref" reference="fig:peptidebond"}. Si excluimos las cadenas laterales R de los aminoácidos de la cadena obtenemos el esqueleto peptı́dico (*backbone*), cuya geometría puede describirse con precisión conociendo los ángulos diedros $\phi$ y $\psi$ (ver sección [1.3.2](#SS){reference-type="ref" reference="SS"}).

![ [Figura](#fig:peptidebond). Estructura del enlace peptı́dico y la cadena polipeptı́dica. Este enlace es rı́gido, plano y no permite el giro. Figura tomada de <https://www.chemistry.ucla.edu>. ](fig/peptide_bond.jpg){#fig:peptidebond width="80%"}

### El enlace fosfodiéster y los nucleótidos {#nts}

Los nucleótidos que forman los ácidos nucleicos se componen a su vez de moléculas: un fosfato, una pentosa y una base nitrogenada. Entre el ADN y el ARN la diferencia fundamental es la pentosa que incluyen: ribosa para el ARN, 2-desoxirribosa para el ADN. Las 4 bases nitrogenadas que pueden unirse a las pentosas dan identidad al nucleótido. La otra diferencia entre ADN y ARN es precisamente su repertorio de bases nitrogenadas. Comparten la adenina, la guanina y la citosina, mientras que la timina es especı́fica del ADN y el uracilo del ARN.

![ [Figura](#fig:basesn}). Las 5 bases nitrogenadas de los ácidos nucleicos, tomadas de superfund.pharmacy.arizona.edu. A y G son purinas, mientras que C, T y U son pirimidinas. ](fig/basesn.png){#fig:basesn}

![ [Figura](#fig:nucleotido}). Ejemplo de nucleótido, tomado de superfund.pharmacy.arizona.edu. ](fig/nucleotido.png){#fig:nucleotido}

![ [Figura](#fig:fosfodiester}). Dibujo de un trinucleótido 5'-TAA-3' mostrando dos enlaces fosfodiéster consecutivos, tomado de <http://www.wikiwand.com/gl/Enlace_fosfodi%C3%A9ster>. Figura reproducida con permiso de los autores. ](fig/fosfodiester.png){#fig:fosfodiester}

Los nucleótidos se enlazan por medio de enlaces fosfodiéster para formar polinucleótidos, es decir, cadenas de ADN o ARN, cuyo sentido viene definido por los 2 carbonos que intervienen en este enlace.

### Interacciones no covalentes en las macromoléculas {#macro1:intnocov}

Además de los enlaces peptı́dico y fosfodiéster, debemos conocer otras interacciones atómicas no covalentes más débiles, pero muy importantes para comprender las macromoléculas [@Lehninger1982]. Son sobre todo de estos tipos:

-   Interacciones hidrofóbicas entre solutos en soluciones acuosas. Se consideran hidrofóbicas aquellas sustancias que son repelidas por el agua o que no se pueden mezclar con ella.

-   [Atracción de van der Waals](http://es.wikipedia.org/wiki/Fuerzas_de_van_der_Waals) entre átomos no cargados, hasta el punto en que casi se solapan sus orbitales externos.

-   [Interacciones electrostáticas](http://es.wikipedia.org/wiki/Electrost%C3%A1tica) inversamente proporcionales a la distancia entre átomos de cargas propias o inducidas. Dentro de las proteínas reciben a veces el nombre de [puentes salinos](http://es.wikipedia.org/wiki/Estructura_de_las_prote%C3%ADnas#Interacciones_carga\-carga), y son más frecuentes entre residuos cercanos en secuencia [@Donald2011].

-   [Puentes de H](http://es.wikipedia.org/wiki/Enlace_por_puente_de_hidr%C3%B3geno), de longitud fija, entre átomos de cargas opuestas que son además parte de enlaces covalentes parciales. En proteı́nas es común entre grupos -NH y O=C-, puesto que en estos casos el H tiene carga parcial positiva y el O negativa. En los ácidos nucleicos encontramos sobre todo los puentes que sostienen los [pares de bases](http://en.wikipedia.org/wiki/Base_pair).

Análisis jerárquico de la estructura de macromoléculas
------------------------------------------------------

La estructura de ácidos nucleicos y proteı́nas puede analizarse de forma jerárquica en 4 niveles, partiendo de la estructura primaria, su secuencia de monómeros, hasta llegar a su estructura cuaternaria, el nivel de asociación de diferentes cadenas.

### Estructura primaria

La estructura primaria de una proteı́na se corresponde con la secuencia lineal de aminoácidos codificada en su correspondiente unidad de transcripción y suele representarse por medio de una cadena donde cada letra identifica a un aminoácido o residuo. Por ejemplo, los primeros 30 aminoácidos de la proteı́na insulina de la mosca *Drosophila melanogaster* son:\
`MFSQHNGAAV HGLRLQSLLI AAMLTAAMAM...`\
donde por ejemplo M es metionina, Q es glutamina o A es alanina. El sentido de la cadena es desde el extremo amino-terminal hacia el carboxilo-terminal.

  --- ----- -------------- -- --- ----- ------------
  A   ALA   Alanina           M   MET   Metionina
  C   CYS   Cisteı́na          N   ASN   Asparagina
  D   ASP   Aspartato         P   PRO   Prolina
  E   GLU   Glutamato         Q   GLN   Glutamina
  F   PHE   Fenilalanina      R   ARG   Arginina
  G   GLY   Glicina           S   SER   Serina
  H   HIS   Histidina         T   THR   Treonina
  I   ILE   Isoleucina        V   VAL   Valina
  K   LYS   Lisina            W   TRP   Triptófano
  L   LEU   Leucina           Y   TYR   Tirosina
  X   \-    desconocido                 
  --- ----- -------------- -- --- ----- ------------

  : Nomenclatura de los 20 aminoácidos esenciales[]{label="tab:amino"}

De igual manera, la estructura primaria de los ácidos nucleicos es su secuencia de nucleótidos, que tiene un sentido dado por la dirección de los enlaces fosfodiéster. De igual modo se suele representar de forma simplificada, asignando una sola letra a cada nucleótido, o mejor dicho, a cada base nitrogenada. Además se suele usar el sentido 5'-3'. Por ejemplo, el principio del gen de la insulina de la mosca *Drosophila melanogaster* tiene una secuencia similar a:\
`5’ atgtttagcc agcacaacgg tgcagcagta 3’`\
donde A es adenina, T timina, C citosina y G guanina. En el caso del ADN, que como veremos suele formar una doble hélice antiparalela, se sobreentiende que hay una secuencia complementaria que corre en sentido opuesto. En este caso serı́a:\
`5’ atgtttagcc agcacaacgg tgcagcagta 3’`\
`3’ tacaaatcgg tcgtgttgcc acgtcgtcat 5’`\
En el caso de secuencias codificantes, la secuencia primaria se puede representar en forma de codones o tríos de pares de bases, donde cada uno codifica para un aminoácido o un codón STOP:\
`5’ atg ttt agc cag cac aac ggt gca tga 3’`\
`3’ tac aaa tcg gtc gtg ttg cca cgt act 5’`\
La estructura primaria en nucleótidos es por tanto el soporte físico de las secuencias codificantes que son posteriormente traducidas a proteı́nas. Por tanto, si ocurren mutaciones en un gen es posible que la secuencia codificante correspondiente se vea alterada. Se pueden dar varios tipos de mutaciones, tanto si son sustituciones de un nucleótido (SNP), inserciones o deleciones:

-   Sustituciones sinónimas que cambian un codón pero no el aminoácido correspondiente.

-   Sustituciones no sinónimas que cambian un codón y el aminoácido correspondiente. En la literatura se llaman mutaciones *missense*.

-   Sustituciones, inserciones o deleciones que introducen un codón STOP prematuro. En la literatura se llaman mutaciones *nonsense*.

-   Inserciones o deleciones que alteran el marco de lectura, o los bordes entre exones e intrones, y por tanto el péptido resultante.

### Estructura secundaria {#SS}

Para neutralizar las cargas polares del esqueleto peptı́dico, las proteı́nas adoptan conformaciones que maximizan la formación de puentes de hidrógeno, gracias a la libertad de giro de los enlaces situados inmediatamente antes y después del enlace peptı́dico. Esto lo hacen principalmente formando $\alpha$-hélices dextrógiras, láminas $\beta$, como se muestra en las figuras [1.11](#fig:est2protH){reference-type="ref" reference="fig:est2protH"}, [1.12](#fig:est2protH2){reference-type="ref" reference="fig:est2protH2"}, [1.13](#fig:est2protE){reference-type="ref" reference="fig:est2protE"} y [1.14](#fig:est2protE2){reference-type="ref" reference="fig:est2protE2"}, y giros de varios tipos, en menor medida.

![ [Figura](#fig:est2protH). Esquema de $\alpha$-hélice en una cadena polipeptı́dica, tomado de <https://www.uoguelph.ca/chemistry>. ](fig/est2protH.png){#fig:est2protH width="80%"}

![ $\alpha$-hélice mostrando cadenas laterales y puentes de hidrógeno entre residuos vecinos (en azul), tomada de <http://structuralbioinformatics.com>. ](fig/est2protH2.jpg){#fig:est2protH2}

![ [Figura](#fig:est2protE}). Esquema de las dos disposiciones posibles (paralelas y anti-paralelas) de láminas beta en cadenas polipeptı́dicas, tomado de <https://www.uoguelph.ca/chemistry>. ](fig/est2protE.png){#fig:est2protE}

![ [Figura](#fig:est2protE2}). Diagrama de láminas beta antiparalelas mostrando la orientación a ambos lados del plano de las cadenas laterales, tomado de <http://structuralbioinformatics.com>. ](fig/est2protE2.jpg){#fig:est2protE2}

La estructura secundaria de las proteínas se puede codificar de manera similar a la secuencia primaria, asignando a cada residuo una letra que identifica el estado de estructura secundaria en que se encuentra. Se suele identificar a los residuos de una $\alpha$-hélice con H, los de una lámina $\beta$ con E y los demás con C, del inglés *coil*. Ésta sería la clasificación simple de 3 estados, que puede afinarse más llegando a [8 estados](https://en.wikipedia.org/wiki/Protein_secondary_structure#DSSP_H-bond_definition):

  --- -----------------------------------------------------------------------------------
  G   hélice $3_{10}$ con vuelta de 3 residuos
  H   $\alpha$-hélice con vuelta de 4 residuos
  I   $\pi$-hélice con vuelta de 5 residuos
  T   giros de 3-5 residuos con puentes de H entre residuos vecinos
  E   conformación extendida de lámina $\beta$
  B   puente $\beta$ entre segmentos de tres residuos en conformación extendida $\beta$
  S   giro de gran curvatura sin puentes de H
  C   resto de conformaciones
  --- -----------------------------------------------------------------------------------

  :  Estados de estructura secundaria definidos por el algoritmo DSSP en base a patrones de puentes de hidrógeno. []{label="tab:SS8"}

La misma secuencia que vimos antes podría tener esta estructura secundaria de 3 estados:

`MFSQHNGAAV HGLRLQSLLI AAMLTAAMAM...`\
`EEEECCEEEE HHHHHHHHHH CCCCCCCCCC...`\
Cuando forman parte de un elemento de estructura secundaria, los aminoácidos adoptan conformaciones características, que se pueden resumir en forma de [diagramas de Ramachandran](http://en.wikipedia.org/wiki/Ramachandran_plot) [@Ramachandran1968], que muestran la distribución de valores de los ángulos $\phi$ y $\psi$ observados a la largo del esqueleto de una proteína:

![ [Figura](#fig:psiphi). Ángulos diedros en el esqueleto proteico, figura tomada de [@Balaji2017]. ](fig/phipsi3.png){#fig:psiphi width="50%"}

![ [Figura](#fig:ramachandran}). Diagrama de Ramachandran tomado de [wikimedia](https://commons.wikimedia.org/wiki/File:Ramachandran%27s_Diagram.jpg). Figura reproducida con permiso de sus autores. ](fig/ramachandranWiki.jpg){#fig:ramachandran}

La estructura secundaria de los ácidos nucleicos está también basada en la formación de puentes de hidrógeno, dada la naturaleza polar de los nucleótidos. Para el caso del ADN, como se muestra en la figura [1.17](#fig:est2adn){reference-type="ref" reference="fig:est2adn"}, el repertorio de puentes de hidrógeno posibles es muy limitado: adenina (A) con timina (T) y guanina (G) con citosina (C).

![ [Figura](#fig:est2adn}). Posibles emparejamientos de bases en el ADN, figura tomada de superfund.pharmacy.arizona.edu. ](fig/est2adn.png){#fig:est2adn}

Estos emparejamientos son la base de la estructura secundaria de los ácidos nucleicos, que suelen ser patrones repetidos helicoidales. En el caso del ADN se suelen formar entre dos polinucleótidos de secuencia complementaria, mientras que en el ARN son estructuras (*stems*,*loops*,\...) que se forman dentro del mismo polinucleótido, como se muestra en la siguiente figura:

![ [Figura](#fig:est2arn). Ejemplo de estructura secundaria de una molécula de ARN mostrando la formación de tallos entre segmentos alejados en secuencia. La secuencia es la del consenso del rRNA 26S mitocondrial de Marchantia, Physcomitrella y otras plantas. Las posiciones coloreadas cambian en algunas especies, como se describe en [@Mower2009]. Figura reproducida con permiso de los autores. ](fig/est2arn.png){#fig:est2arn width="80%"}

### Estructura terciaria y cuaternaria {#estr34}

La mayorı́a de las proteı́nas forman glóbulos compactos al plegarse, compuestos de elementos de estructura secundaria organizados de una forma especı́fica y unidos por lazos (*loops* en inglés). Las unidades globulares de plegamiento pueden llamarse [dominios](http://kinemage.biochem.duke.edu/teaching/anatax/html/anatax.2i.html) [@Porter2012], y tienen en su interior sobre todo cadenas laterales hidrofóbicas [@Isom2010], mostrando hacia el solvente los lazos [@Branden1999]. En raras ocasiones, una proteı́na puede formar nudos al plegarse [@Potestio2010; @King2010] o agregarse como amiloides [@Schnabel2010]. Aunque no es una definición universal, en general un dominio tiene autonomía funcional y termodinámica y una historia evolutiva. Desde el punto de vista de la secuencia primaria, un dominio puede representarse por las secuencias alineadas de las proteı́nas que lo contienen.

Las clasificaciones estructurales de proteı́nas se hacen generalmente a nivel de dominios, como en el caso de <http://www.cathdb.info> o la [taxonomı́a de Richardson](http://kinemage.biochem.duke.edu/teaching/anatax), aunque también se han propuesto otros esquemas, como la tabla periódica de [@Taylor2002], donde la unidad básica de plegamiento es una combinación compacta de elementos de estructura secundaria sostenida por una red de contactos que coevoluciona [@Mackenzie2017; @Granata2017]. Se puede ampliar este tema en @pascual_garcia_alberto_2014_1066350.

![ [Figura](#fig:1bvq}). Estructura terciaria de una proteı́na (tioesterasa), con los elementos de estructura secundaria coloreados (amarillo para la láminas betas, rosa para alfa-hélices y blanco para los lazos). Figura exportada con el programa [RasMol](http://rasmol.org/). ](fig/1bvq.png){#fig:1bvq}

![ [Figura](#fig:1bvq}). Alineamiento de secuencias primarias y secundarias de diferentes dominios de tipo tioesterasa anotados en la base de datos [Pfam](https://pfam.xfam.org/family/Thioesterase). Se colorean con distintos colores las columnas con G, P, las cadenas laterales pequeñas o hidrofóbicas (C,A,V,L,I,M,F,W), residuos con grupo hidroxilo o amina (S,T,N,Q), los cargados (D,E,R,K) y finalmente los residuos H o Y. ](fig/thiosterase.png){#fig:1bvq}

![ [Figura](#fig:1crn}). Representación estilo [CIRCOS](http://circos.ca) de la estructura terciaria de una proteı́na, con los elementos de estructura secundaria coloreados. Figura creada con el programa [PDBCirclePlot](http://sacan.biomed.drexel.edu/pdbcircleplot). ](fig/1crn.png){#fig:1crn}

Otra manera de representar la estructura terciaria es por medio de matrices de contactos, que resumen en forma matricial los contactos observados entre los residuos de una secuencia. Es habitual que las matrices de contactos o *contact maps* se calculen excluyendo los contactos entre residuos inmediatamente vecinos. La siguiente figura muestra de qué manera se reflejan los elementos de estructura secundaria en una matriz de contactos, donde los ejes son los residuos ordenados por su posición en la secuencia.

![ [Figura](#fig:SScontacts}). Elementos de estructura secundaria en una matriz de contactos. Figura reproducida con permiso de <http://en.wikipedia.org/wiki/Protein_contact_map>. ](fig/SScontactMap.jpg){#fig:SScontacts}

Esta manera de condensar una estructura terciaria es literalmente el fundamento de la resolución de estructuras por NMR (ver sección [1.4](#metodosExp){reference-type="ref" reference="metodosExp"}), donde las observaciones experimentales de partida son esencialmente contactos atómicos entre residuos.

![ [Figura](#fig:foldclassif}). Distribución de plegamientos de proteı́nas de las 4 clases principales de [SCOP](http://scop.berkeley.edu) ($\alpha$, $\beta$, $\alpha+\beta$, $\alpha/\beta$) tras reducir la dimensionalidad de los datos originales por escalado multidimensional. Figura tomada de [@Hou2005]. Copyright (2005) National Academy of Sciences. ](fig/foldclassification.jpg){#fig:foldclassif}

![ [Figura](#fig:foldpaths}). Posible camino evolutivo que conecta 5 plegamientos distintos de la clase $\alpha/\beta$ de SCOP. La ruta visita 8 dominios distintos que comparten parte de su topología y estructura. Para cada pareja de dominios se indica el total de residuos alineados, el RMSD y el % similitud de secuencia. Figura tomada de [@Nepomnyachiy2014] con permiso de los autores. ](fig/domain_walk.jpg){#fig:foldpaths}

En cuanto a los ácidos nucleicos, su estructura terciaria es muy distinta según se trate de ADN o ARN.\
El ADN suele formar una doble hélice dextrógira antiparalela donde dos cadenas polinucleotı́dicas, de secuencia complementaria, corren en sentidos opuestos, como se muestra en la figura [1.25](#fig:dna3){reference-type="ref" reference="fig:dna3"}. El grado de enrollamiento del ADN puede variar e incluso sabemos que hay al menos [3 tipos](http://en.wikipedia.org/wiki/DNA_structure#DNA_helix_geometries) de dobles hélices posibles, una de ellas levógira, y una triple hélice.

![ [Figura](#fig:dna3}). Estructura atómica en doble hélice antiparalela del ADN, generada con [RasMol](http://rasmol.org/). ](fig/dna3.png){#fig:dna3}

Las combinaciones de diferentes cadenas de proteı́na y/o ácidos nucleicos para formar una unidad biológica funcional se dan ya al nivel de estructura cuaternaria, como ocurre con la [hemoglobina humana](http://en.wikipedia.org/wiki/Hemoglobin), que funciona como un tetrámero, o con muchos factores de transcripción que ejercen su papel regulador como multímeros, como se muestra en la figura [1.26](#fig:1cgp){reference-type="ref" reference="fig:1cgp"}:

![ [Figura](#fig:1cgp}). Estructura del dı́mero de CRP unido a su ADN operador, generada con el programa <http://www.rcsb.org/pdb/explore.do?structureId=1cgp> del Protein Data Bank. Las cadenas de proteı́na están coloreadas en diferentes tonos de verde. ](fig/1cgp_AB.png){#fig:1cgp}

### Estructura 3D de la cromatina

La cromatina es una fibra formada por asociación de DNA genómico y proteínas, no sólo histonas, y es el constituyente esencial del núcleo celular. Cada vez disponemos de más evidencias de que la estructura de la cromatina es clave para entender las funciones de genes, cromosomas e incluso del genoma entero. Algunos de los algoritmos fundamentales que veremos en este curso, ideados originalmente para el estudio de moléculas individuales, se están reciclando en la actualidad para el estudio de la cromatina, puesto que en cierto modo podemos modelarla como una fibra lineal; algo parecido a un polipéptido al que sólo podemos acceder mediante técnicas de resolución limitada. Se puede ampliar este tema en @bau_davide_2014_1066356.

![ [Figura](#fig:cromatin}). Diagrama de flujo del proceso de modelado en 3D de la cromatina, tomado de [@Dekker2013]. Los paneles, comenzando arriba a la izquierda, muestran etapas sucesivas del modelado de un cromosoma bacteriano. La primera etapa es la captura de datos, que concluye con una matriz de contactos genómicos. la segunda consiste en construir un primer modelo que integre los contactos observados con otros datos disponibles, por ejemplo evolutivos o físicos. En la tercera etapa se prueban diferentes funciones con el fin de optimizar el modelo inicial que representa las conformaciones de la cromatina. La cuarta etapa es el análisis objetivo del modelo refinado. Si los resultados no son satisfactorios es necesario comenzar de nuevo. Copyright (2013) Springer Nature. ](fig/cromatin.png){#fig:cromatin}

### Relación entre estructura primaria y terciaria de las proteı́nas: alineamientos y superposiciones {#3dcons}

[@Chothia1986] analizaron por vez primera la relación entre la secuencia y la estructura de las proteı́nas, que se puede resumir en esta figura:

![ [Figura](#fig:chothialesk). Correlación no lineal entre la conservación de secuencia y estructura de las proteı́nas, tomada de [@Chothia1986] y reproducida con permiso de los autores. ](fig/chothia_lesk.jpg){#fig:chothialesk width="50%"}

Este artículo pionero publica la observación de que a una determinada conservación entre las secuencias A y B, calculada por medio de un alineamiento, le corresponde una mayor o menor divergencia en la comparación de sus estructuras terciarias, medida en términos de [desviaciones (RMSD, en Angstrom)](http://en.wikipedia.org/wiki/Root_mean_square_deviation) en las posiciones de sus residuos, dependiendo de si las mutaciones ocurren en el interior (*core*) o exterior del plegamiento.

$$RMSD = \sqrt \frac{\sum_{i=1}^n dist(C\alpha_{i}^A - C\alpha_{i}^B)^2}{n}$$

Además, éste y otros trabajos posteriores, como @Illergard2009 [@PascualGarcia2010], sugieren que la estructura es una propiedad de las proteínas que se conserva en mayor medida que la secuencia durante la historia evolutiva. Lo excepcional es que secuencias similares tengan grandes diferencias estructurales [@Kosloff2008].

![ [Figura](#fig:thioredoxins}). Conservación de la estructura de tioredoxinas separadas 4 mil millones de años. (A) Árbol filogenético moestrando la distancia evolutiva entre H. sapiens y E. coli y algunos de sus ancestros desaparecidos. (B) Superposición estructural de varias tioredoxinas humanas, de E. coli, y de algunos ancestros precámbricos. (C) Alineamiento múltiple de las secuencias y estructuras secundarias de las tioredoxinas estudiadas. Figura reproducida con permiso de [@InglesPrieto2013]. ](fig/thioredoxins.jpg){#fig:thioredoxins}

El panel C de la figura [1.29](#fig:thioredoxins){reference-type="ref" reference="fig:thioredoxins"} es útil para recordar la correspondencia que se puede establecer entre un **alineamiento** de secuencias y la **superposición** de las correspondientes estructuras. En un alineamiento de secuencia se establece qué residuos de una proteı́na ocupan el mismo lugar en la secuencia que los de otras proteı́nas similares. En cambio, en una superposición buscamos residuos que ocupan el mismo lugar en la estructura, a los que llamamos **residuos equivalentes**. Mientras el primero se puede calcular aun sin tener las estructuras, solamente con la secuencia, la superposición requiere conocer las coordenadas en tres dimensiones de las proteı́nas en cuestión. Con aquellas proteı́nas con estructuras resueltas es posible hacer el siguiente ejercicio, que tiene como objeto explorar esta correspondencia y aprender que un alineamiento de secuencias con baja identidad puede contener errores que se hacen patentes al comprobar la correspondiente superposición.

Tomemos por ejemplo las coordenadas de dos [lisozimas](http://scop.berkeley.edu/sunid=53955) del PDB, como [2NWD](http://www.rcsb.org/pdb/explore/explore.do?structureId=2NWD) y [1GD6](http://www.rcsb.org/pdb/explore/explore.do?structureId=1GD6) ([2nwd.pdb](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/2nwd.pdb), [1gd6.pdb](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1gd6.pdb)), y alineemos sus secuencias:

    2nwd   KVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQIN 60
    1gd6   KTFTRCGLVHELRKHGFEEN---LMRNWVCLVEHESSRDTSKTNTNR-NGSKDYGLFQIN 56

    2nwd   SRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRD 120
    1gd6   DRYWCSKGASPG--KDCNVKCSDLLTDDITKAAKCAKKIYKR-HRFDAWYGWKNHCQG-- 111

    2nwd   VRQYVQGCGV 130
    1gd6   SLPDISSC-- 119

En este alineamiento las columnas alineadas son parejas de residuos equivalentes o inserciones/deleciones sin alinear (**indels**).

Mediante un algoritmo similar al descrito en este Mediante un algoritmo similar al descrito en este trabajo de @McLachlan1979, que hace uso de la [descomposición en valores singulares](http://books.google.es/books?id=I2TEgd8-yfsC&lpg=PR1&pg=PA73#v=onepage&q&f=false), podemos calcular la superposición correspondiente. El siguiente programa, que importa el módulo [SVD](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/SVD.py), lo implementa: verbatiminput./code/prog3.1.py

Al cambiar el alineamiento cambia la superposición, demostrando la importancia que tiene la variable 'calidad de los alineamientos' si vamos a hacer inferencias estructurales. Sabrías editar el código para replicar el algoritmo de superposición de [@Chothia1986]?

Métodos experimentales para el estudio de la estructura y dinámica de macromoléculas {#metodosExp}
------------------------------------------------------------------------------------

Los principales métodos experimentales para determinar la estructura de macromoléculas son:

-   Microscopı́a electrónica, para el estudio de grandes complejos moleculares. Dentro de esta familia, la microscopı́a crio-electrónica (crio-EM) es la aproximación más prometedora porque ha permitido resolver con alta resolución grandes complejos moleculares, como ribosomas, inasequibles por cristalografı́a de rayos-X [@Callaway2015].

-   Cristalografı́a de rayos-X, aplicable a todas las macromoléculas, permite obtener las descripciones estructurales estáticas de más calidad a partir de cristales. Un buen libro para leer sobre esto es [@Rhodes2000]. Las fuentes de radiación de rayos X de láser de electrones libres (XFEL) permiten estudiar cristales pequeños y proteı́nas de membrana [@Marx2014].

-   Dispersión de rayos X a bajos ángulos (SAXS), que no requiere la obtención de cristales y se ha utilizado para el estudio de proteı́nas desordenadas.

-   Análisis de espectros de resonancia magnética nuclear (NMR), aplicable a todas las macromoléculas, permite estudiar comportamientos dinámicos, como uniones entre moléculas y movimientos moleculares [@Jiang2017]. La construcción de modelos de proteı́nas a partir de datos de NMR se ha logrado automatizar en casos sencillos [@Rosato2012; @Liu2017]. Un libro de referencia sobre esta metodología es [@Cavanagh2000].

-   Análisis de espectros de dicroísmo circular (CD), que permite estimar de manera sencilla en el laboratorio el porcentaje de residuos de una secuencia que adquieren estructura secundaria. Los espectros obtenidos se pueden comparar con los de estructuras conocidas [@Mavridis2016].

-   Espectrometrı́a de masas de moléculas entrecruzadas, que ha permitido obtener información estructural para modelar complejos de proteı́nas [@Rappsilber2011].

-   Captura de conformaciones cromosómicas, que permiten analizar la organización especial de la cromatina celular. Esta [familia de métodos](https://en.wikipedia.org/wiki/Chromosome_conformation_capture) cuantifican las interacciones entre loci cercanos en el espacio pero alejados en la secuencia del cromosoma [@bau_davide_2014_1066356].

Además de estos métodos, enfocados a obtener información estructural directamente, hay otras aproximaciones basadas en la biología molecular que permiten extraer información estructural indirectamente. Por ejemplo, la ultrasecuenciación se usa para diseñar proteı́nas y estudiar mutantes [@Wrenbeck2017; @Rocklin2017; @Butterfield2017]. Tambien se han empleado ensayos en paralelo para el descubrimiento de regiones desordenadas transactivadoras [@Ravarani2018].

En cualquier caso, los métodos experimentales de obtención de estructuras de macromoléculas producen descripciones atómicas de variada calidad y resolución que se suelen describir de manera cuantitativa por medio de formatos como el formato [PDB](http://www.wwpdb.org/documentation/file-format.php), utilizado por el repositorio [Protein Data Bank](http://www.rcsb.org) (PDB, ver sección [1.5](#PDBformat){reference-type="ref" reference="PDBformat"}).

En ocasiones puede ser necesario comprobar los datos experimentales crudos sobre los que se construye una estructura del PDB, para lo cual podemos recurrir a software como [Coot](http://en.wikipedia.org/wiki/Coot_%28program%29). Para evaluar independientemente la calidad de una estructura del PDB podemos usar la plataforma [MolProbity](http://molprobity.biochem.duke.edu).

En el PDB la mayor parte de las estructuras se derivan de cristales o espectros de NMR, y de hecho hay una buena colección de proteínas que se han resuelto con ambas metodologías, lo que ha permitido concluir que son complementarias y que construyen descripciones moleculares muy parecidas, pero no idénticas [@Brunger1997; @Sikic2010; @Leman2018]. De hecho, comparar estructuras resueltas con ambas metodologías permite identificar fragmentos [@Hrabe2016] y proteínas intrínsecamente desordenadas [@Ota2013], así como proteínas que cambian de plegamiento [@Porter2018].

![ [Figura](#fig:mioglobina}). Primer modelo en la historia de una proteı́na, la mioglobina a 6Å de resolución [@Kendrew1958]. Figura reproducida con permiso de <https://www2.mrc-lmb.cam.ac.uk/about-lmb/archive/scientific-models> ](fig/mioglobina.png){#fig:mioglobina}

El Protein Data Bank y sus formatos {#PDBformat}
-----------------------------------

En las siguientes secciones utilizaremos el formato clásico [PDB](http://www.wwpdb.org/documentation/file-format.php) (con sus hermanos PDBML y PDBx/mmCIF), el estándar histórico para codificar la estructura tridimensional de macromoléculas biológicas, sobre todo proteı́nas y ácidos nucleicos, por medio de las coordenadas cartesianas de sus átomos. El fichero [1LFU](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1lfu.html) muestra el contenido de uno de estos archivos.

Estos archivos pueden visualizarse de forma interactiva usando programas como [RasMol](http://rasmol.org), [Jmol](http://jmol.sourceforge.net), [PyMOL](http://www.pymol.org), [Chimera](https://www.cgl.ucsf.edu/chimera), o interfaces web como [AQUARIA](http://aquaria.ws).

Desde 2022 el Protein Data Bank adoptó por defecto el formato [PDBx/mmCIF](https://mmcif.wwpdb.org) porque supera al PDB a la hora de representar estructuras cuaternarias complejas con muchas cadenas. El software [gemmi](https://github.com/project-gemmi/gemmi) permite convertir entre estos formatos.

Hasta 2022 las estructuras del PDB se han nombrado con una combinación de 4 caracteres, empezando por un número, pero el espacio de nombres posibles se agotará pronto y se plantea que las nuevas estructuras tengan nombres con la estructura `pdb_00017fgz`.

Finalmente, aunque en este curso usaremos coordenadas cartesianas, conviene recordar que en muchas aplicaciones se prefiere usar [coordenadas internas](http://es.wikipedia.org/wiki/Matriz_Z) para hacer operaciones geométricas con moléculas de manera eficiente.

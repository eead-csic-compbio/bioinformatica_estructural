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

**Tabla**. Nomenclatura de los 20 aminoácidos esenciales[]{label="tab:amino"}

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

![ $\alpha$-hélice mostrando cadenas laterales y puentes de hidrógeno entre residuos vecinos (en azul), tomada de <http://structuralbioinformatics.com>. []{label="fig:est2protH2"}](fig/est2protH2.jpg){#fig:est2protH2}

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

**Tabla**. Estados de estructura secundaria definidos por el algoritmo DSSP en base a patrones de puentes de hidrógeno. []{label="tab:SS8"}

La misma secuencia que vimos antes podría tener esta estructura secundaria de 3 estados:

`MFSQHNGAAV HGLRLQSLLI AAMLTAAMAM...`\
`EEEECCEEEE HHHHHHHHHH CCCCCCCCCC...`\
Cuando forman parte de un elemento de estructura secundaria, los aminoácidos adoptan conformaciones características, que se pueden resumir en forma de [diagramas de Ramachandran](http://en.wikipedia.org/wiki/Ramachandran_plot) [@Ramachandran1968], que muestran la distribución de valores de los ángulos $\phi$ y $\psi$ observados a la largo del esqueleto de una proteína:

![ Ángulos diedros en el esqueleto proteico, figura tomada de [@Balaji2017]. []{label="fig:psiphi"}](fig/phipsi3.png){#fig:psiphi width="50%"}

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

### Relación entre estructura primaria y terciaria: alineamientos y superposiciones {#threedeecons}

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

Mediante un algoritmo similar al descrito en este Mediante un algoritmo similar al descrito en este trabajo de @McLachlan1979, que hace uso de la [descomposición en valores singulares](http://books.google.es/books?id=I2TEgd8-yfsC&lpg=PR1&pg=PA73#v=onepage&q&f=false), podemos calcular la superposición correspondiente. El siguiente programa, que importa el módulo [SVD](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/SVD.py), lo implementa: <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog3.1.py" style="color: black; text-decoration: underline;">[fuente: prog3.1.py]</a>

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

En las siguientes secciones utilizaremos el formato clásico [PDB](http://www.wwpdb.org/documentation/file-format.php) (con sus hermanos PDBML y PDBx/mmCIF), el estándar histórico para codificar la estructura tridimensional de macromoléculas biológicas, sobre todo proteı́nas y ácidos nucleicos, por medio de las coordenadas cartesianas de sus átomos. El fichero [1LFU](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1lfu.pdb) muestra el contenido de uno de estos archivos.

Estos archivos pueden visualizarse de forma interactiva usando programas como [RasMol](http://rasmol.org), [Jmol](http://jmol.sourceforge.net), [PyMOL](http://www.pymol.org), [Chimera](https://www.cgl.ucsf.edu/chimera), o interfaces web como [AQUARIA](http://aquaria.ws).

Desde 2022 el Protein Data Bank adoptó por defecto el formato [PDBx/mmCIF](https://mmcif.wwpdb.org) porque supera al PDB a la hora de representar estructuras cuaternarias complejas con muchas cadenas. El software [gemmi](https://github.com/project-gemmi/gemmi) permite convertir entre estos formatos.

Hasta 2022 las estructuras del PDB se han nombrado con una combinación de 4 caracteres, empezando por un número, pero el espacio de nombres posibles se agotará pronto y se plantea que las nuevas estructuras tengan nombres con la estructura `pdb_00017fgz`.

Finalmente, aunque en este curso usaremos coordenadas cartesianas, conviene recordar que en muchas aplicaciones se prefiere usar [coordenadas internas](http://es.wikipedia.org/wiki/Matriz_Z) para hacer operaciones geométricas con moléculas de manera eficiente.

TEORÍA: Plegamiento y dinámica de macromoléculas {#macro2}
================================================

Ahora que conocemos de qué están hechas las macromoléculas y sabemos lo importantes que son en biologı́a, haremos un pequeño repaso sobre las ideas centrales del proceso de plegamiento (*folding*), responsable de que estas moléculas adquieran la estructura tridimensional que les confiere su función.

Plegamiento y desnaturalización {#desnat}
-------------------------------

El interés sobre el plegamiento de las macromoléculas se despertó al estudiar sus reacciones de desnaturalización. Si tenemos proteı́nas o ácidos nucleicos en disolución y cambiamos de forma notable las condiciones en que suelen encontrarse en su medio biológico, pierden su estructura y función nativas. Este proceso, llamado reacción de desnaturalización, puede ser reversible en ciertas condiciones y los cambios pueden ser por ejemplo de temperatura, por encima de su temperatura de fusión ($T_{m}$), o en la naturaleza del solvente.\
@Anfinsen1961 mostró experimentalmente que la desnaturalización es reversible al menos para proteı́nas pequeñas, añadiendo y retirando agentes desnaturalizantes a disoluciones de enzimas que ganaban y perdı́an su actividad. Ası́ demostró que el plegamiento de una proteı́na depende exclusivamente de su secuencia, aunque hoy sabemos que algunas necesitan la ayuda de chaperoninas [@Hartl2002].\
Todavía hoy el proceso de plegamiento no se comprende bien debido a su complejidad (ver secciones [2.3](#complejidad){reference-type="ref" reference="complejidad"} y [2.4](#complejidad2){reference-type="ref" reference="complejidad2"}), aunque llevemos 50 años estudiándolo [@Dill2012].

![ [Figura](#fig:desnatADN}). Reacción de desnaturalización y renaturalización (hibridación) de una molécula de ADN, tomada de @HernandezLemus2012 y reproducido con permiso de los autores. ](fig/desnatADN.png){#fig:desnatADN}

La $T_{m}$ de los ácidos nucleicos es proporcional al contenido en bases GC de su secuencia, ya que estos pares de bases (ver figura [1.17](#fig:est2adn){reference-type="ref" reference="fig:est2adn"}) establecen entre sı́ 3 puentes de hidrógeno, mientras que los AT/AU sólo 2. Si la temperatura supera $T_{m}$, las moléculas de ADN se separan en dos hebras polinucleotı́dicas (como se muestra en la figura [2.1](#fig:desnatADN){reference-type="ref" reference="fig:desnatADN"}), pero si la bajamos lentamente ambas hebras vuelven a unirse de forma complementaria en una reacción llamada hibridación. De nuevo vemos cómo en este caso la secuencia es suficiente para guiar el plegamiento, al menos para moléculas pequeñas.\

Fuerzas que influyen en el proceso de plegamiento de macromoléculas
-------------------------------------------------------------------

Se han reconocido varias propiedades e interacciones fı́sicas que guı́an al proceso de plegamiento, como las que mencionamos en la sección [1.2.3](#macro1:intnocov){reference-type="ref" reference="macro1:intnocov"}. Algunas son especı́ficas del plegamiento de proteı́nas, como la formación de enlaces disulfuro entre cisteı́nas o la formación de puentes salinos entre aminoácidos básicos y ácidos, pero en general se acepta que las principales son la hidrofobicidad en un medio acuoso y la formación de puentes de hidrógeno [@Dill1990; @Lehninger1982; @Mathews1999].

Algunas de estas propiedades pueden estimarse directamente desde la secuencia. Por ejemplo, se han propuesto escalas de hidrofobicidad como la de la tabla siguiente, que quedan englobadas en clasificaciones de aminoácidos como la de sección [1.5](#fig:aminoclassif){reference-type="ref" reference="fig:aminoclassif"}.

  --- ------ --- ------
  A   1.8    M   1.9
  C   2.5    N   -3.5
  D   -3.5   P   -1.6
  E   -3.5   Q   -3.5
  F   2.8    R   -4.5
  G   -0.4   S   -0.8
  H   -3.2   T   -0.7
  I   4.5    V   4.2
  K   -3.9   W   -0.9
  L   3.8    Y   -1.3
  --- ------ --- ------

**Tabla**. Escala de hidrofobicidad de los 20 aminoácidos, con valores positivos para los residuos hidrofóbicos y negativos para los demás [@Kyte1982].[]{label="tab:hidrof"}

Como resultado del proceso de plegamiento en medios acuosos, las macromoléculas se empaquetan mostrando hacia el solvente superficies hidrofı́licas y ocultando los componentes más hidrofóbicas. En el interior las interacciones de van der Waals dan estabilidad al conjunto. Como siempre, hay excepciones notables [@Sun2014]. En el caso de las proteı́nas otro factor que condiciona el plegamiento es su tendencia natural a formar multı́meros [@Garcia2017].

Complejidad algorı́tmica del plegamiento {#complejidad}
---------------------------------------

Sabemos que bajo condiciones fisiológicas el proceso de plegamiento es termodinámicamente favorable, es decir, que las macromoléculas son más estables en su conformación nativa que en otras posibles conformaciones. Y conocemos al menos los factores más importantes que afectan y guı́an al proceso de plegamiento. Por último, sabemos que el plegamiento es un proceso rápido, que tarda a lo sumo tiempos del orden de segundos. A pesar de esto, a dı́a de hoy no sabemos predecir de forma precisa cómo se plegará una proteı́na o un ácido nucleico partiendo solamente de su secuencia.

Cuáles son las dificultades? Esto lo veremos tomando como ejemplo las proteı́nas, que se han estudiado mucho más a este nivel. Son fundamentalmente dos:

-   el enorme número de posibles conformaciones que puede tomar una cadena polipeptı́dica

-   la necesidad de cuantificar la estabilidad en condiciones fisiológicas de cada una de ellas

El proceso de plegamiento puede entonces verse como una exploración en un embudo (*funnel*) como el de la figura [2.2](#fig:foldfunnel){reference-type="ref" reference="fig:foldfunnel"}, donde observamos un máximo de estabilidad que se corresponde con un mínimo de energía libre (conformaciones nativas), y otros máximos secundarios o locales denominados estados metaestables. En ciertas condiciones las proteínas pueden quedarse atrapadas en estos estados y perder funcionalidad o agregarse, de ahí la importancia de las chaperonas [@pascual_garcia_alberto_2014_1066348].

![ [Figura](#fig:foldfunnel}). Superficie energética del plegamiento de proteı́nas desde su sı́ntesis hasta su estado final plegado o agregado. Algunas conformaciones metaestables deben superar barreras energéticas para retomar su ruta de plegamiento favorable, en ocasiones con ayuda de chaperonas (izquierda). Cuando varias moléculas se pliegan en el mismo compartimento pueden formar contactos que propicien la acumulación de agregados amorfos, oligómeros tóxicos o fibrillas amiloides (derecha). Figura tomada de @Amm2014 y reproducida con permiso de los autores. ](fig/funnel2.jpg){#fig:foldfunnel}

![ [Figura](#fig:perresiduefolding). Contribuciones de cada uno de los residuos de una proteı́na camaleónica, que puede adoptar un plegamiento $\alpha$ (izquierda) u otro $\alpha + \beta$ (derecha) con muy pocos cambios en la secuencia. Arriba: los residuos que favorecen el plegamiento se empaqueten en la estructura globular correspondiente. Medio: las medidas de energı́a libre por residuo revelan las partes de la secuencia que favorecen el plegamiento. Abajo: la energı́a libre por residuo puede generalmente atribuirse a la secuencia (GA30 o GB30) que favorece cada plegamiento. Figura tomada de @Roy2014 y reproducida con permiso de los autores. ](fig/per_residue_folding.jpg){#fig:perresiduefolding width="40%"}

![ [Figura](#fig:foldfunnelRNA}). Embudo de plegamiento de una ribozima. Figura de @Behrouzi2012 y reproducida con permiso de los autores. ](fig/ribozymeFolding.png){#fig:foldfunnelRNA}

Desde este punto de vista, la búsqueda de la conformación nativa es como buscar una aguja en un pajar. Cómo es el espacio de conformaciones? Lo veremos por medio de la paradoja de Levinthal.

Paradoja de Levinthal {#complejidad2}
---------------------

En una proteı́na los enlaces peptı́dicos son rı́gidos pero hay 2 enlaces libres de girar por cada aminoácido, a parte de que cada cadena lateral puede orientarse de diferentes maneras. Parece por tanto que realmente es una cadena muy flexible, que puede adoptar muchas conformaciones diferentes. [Cyrus Levinthal](http://en.wikipedia.org/wiki/Levinthal's_Paradox), en 1969, fue el primero en hacer una estimación. El razonamiento es la siguiente:

-   digamos que cada aminoácido de una cadena puede tomar $X$ estados diferentes

-   una proteı́na de tamaño medio tiene, digamos, 100 aminoácidos

-   digamos que cada cambio de estado en un medio fisiológico tarda un tiempo $t$

-   entonces el tiempo $T_{expl}$ que llevarı́a explorar todos los estados serı́a de $t X^{100}$

Para $X$ pequeños, como $10$, y tiempos muy cortos, como $10^{-13} s$, $T_{expl} = 10^{-13} 10^{100} = 10^{87}s$. Ahora compárese este valor con los $5s$ que tarda la bacteria *Escherichia coli* en sintetizar una proteı́na de 100 residuos completamente funcional.

Levinthal concluyó que las proteı́nas naturales no se pliegan siempre, pues no tienen tiempo de explorar extensivamente todas las conformaciones. Propuso que hay otras conformaciones cercanas igualmente funcionales en términos fisiológicos. En la actualidad esto se ha interpretado además como una evidencia de que el plegamiento no es totalmente aleatorio, sino que es un proceso por etapas, que reduce en muchos órdenes de magnitud la búsqueda de conformaciones [@Mathews1999; @Burra2009; @Sali1994].

Aproximaciones a la velocidad de plegamiento de proteı́nas {#hora2:K}
---------------------------------------------------------

Desde un punto de vista químico podríamos definir el proceso de plegamiento (P) como una reacción, opuesta a la desnaturalización (D), en estos términos (donde $k$ es la constante de equilibrio): $$k_{d}/k_{p}=[prot_{D}]/[prot_{P}] = k$$

Independientemente de que no sepamos todavı́a plegar proteı́nas con precisión, sı́ que podemos en ciertos casos estimar cuanto tardarán en plegarse a partir de su secuencia. @Plaxco1998 demostraron que la velocidad de plegamiento ($k_{p}$) de dominios está estrechamente correlacionada con el *orden de contactos* (CO), es decir, la media de separación en secuencia entre residuos del dominio ya plegado que están en estrecho contacto. En la siguiente ecuación N son los contactos totales, $S_{ij}$ es la separación en secuencia entre los residuos $i,j$ y $L$ es lo longitud de la secuencia. Se da un contacto cuando dos átomos pesados (no H) de dos residuos se encuentran a menos de 6Å:

$$CO = LN \sum_{i=1}^{L} \sum_{j=1}^{L} N S_{ij}$$

Por otro lado, @SSfoldingrate2003 encontraron otra fuerte correlación entre el contenido en estructura secundaria de una secuencia de aminoácidos, su longitud, y su velocidad de plegamiento. La función que definen tiene esta forma (donde H, T y B son fracciones de residuos en esos estados de estructura secundaria y $L$ es la longitud de la secuencia):

$$ln(k_{p}) = 8{.}9T + 14H + 5{.}5B + \frac{121{.}4}{L} - 2{.}8$$

donde $k_{p}$ se mide en $1/s^{6}$. Estas correlaciones sugieren que el factor limitante del proceso de plegamiento es la formación de elementos de estructura secundaria.

El problema de estos métodos es que exigen conocer la estructura de la proteı́na en cuestión, aunque se podrı́an aplicar usando predicciones de estructura secundaria y de orden de contactos.

![ [Figura](#fig:goldentriangle). La velocidad de plegamiento medida experimentalmente para muchas proteı́nas se ciñe a una región triangular. $L$ es la longitud en residuos de cada secuencia estudiada. Figura de @Garbuzynskiy2013, reproducida con permiso de los autores. ](fig/goldentriangle.png){#fig:goldentriangle width="50%"}

Algoritmos de dinámica molecular y plegamiento {#macro3}
----------------------------------------------

Llegados a este punto ya podemos estudiar los principales algoritmos que se han aplicado al problema del plegamiento y la predicción de estructura de macromoléculas. Podemos clasificarlos por el nivel de detalle que utilizan. La escala va desde métodos que modelan cada uno de los átomos de las macromoléculas en cuestión y del solvente en que se encuentran, hasta métodos donde se manejan aminoácidos o incluso elementos de estructura secundaria como un todo indivisible y se ignora o modela de forma implı́cita el solvente. Se pueden ampliar estos contenidos en [@pascual_garcia_alberto_2014_1066348].

### Modelos bidimensionales de plegamiento de proteı́nas

Los primeros modelos bidimensionales [@Dill1995; @MorenoHernandez2012; @Shakhnovich1993], que usan un alfabeto reducido donde los aminoácidos son polares (P) o hidrofóbicos (H) y donde las cadenas se pliegan en una malla bidimensional, sirvieron para aproximarse al plegamiento de una forma simplificada. En general se acepta que estos modelos reproducen las caracterı́sticas más importantes del proceso de plegamiento real con la ventaja de ser más manejables:

-   se forman estructuras secundarias, que limitan la velocidad del proceso

-   el plegamiento se hace por etapas y está dominado por la hidrofobicidad

Vamos a definir más formalmente este modelo, porque ilustra de forma sencilla los algoritmos de dinámica molecular que mencionaremos en la siguiente sección:

-   dado el alfabeto {H,P}, una proteı́na es una secuencia de longitud N, tal como `HHHPPPHHPPPPPHHHPPPPHHH`.

-   las proteı́nas viven en una malla bidimensional, como la de la figura [2.6](#fig:dillmodel){reference-type="ref" reference="fig:dillmodel"}, donde cada posición no puede estar ocupada por más de un residuo.

-   cada celda de la malla tiene 4 vecinos: N, S, E y O.

-   cada residuo está dado en coordenadas internas empezando por el extremo, por ejemplo el residuo 2 está al N del 1.

-   hay por lo tanto un máximo de $4^{N}$ conformaciones posibles.

-   no se admiten cruces en la secuencia.

-   cuando dos residuos no contiguos en secuencia ocupan celdas vecinas se dice que interaccionan.

-   la energı́a de cada interacción se evalúa usando la matriz de la tabla siguiente.

-   la conformación nativa es aquella que minimiza la energı́a total, maximizando la estabilidad.

![ [Figura](#fig:dillmodel}). Plegamiento en dos dimensiones en el modelo HP de @Dill1995. Copyright (1995) Protein Science. ](fig/dillmodel.png){#fig:dillmodel}

  --- ---- ----
      P    H
  P   0    -1
  H   -1   -3
  --- ---- ----

**Tabla**. Matriz de interacción $M_{ij}$ en un modelo HP, que favorece explícitamente las interacciones polares.[]{label="tab:matrizHP"}

![ [Figura](#fig:snakefold}). Ampliación del modelo de Dill a tres dimensiones implementada en el juego SNAKE de @Nido2016. Debajo se muestran matrices de contactos correspondientes a algunos de los plegamientos. Figura reproducida con permiso de los autores. ](fig/snake.jpg){#fig:snakefold}

### Modelos tridimensionales de mecánica molecular {#DM}

Los modelos tridimensionales de la [mecánica molecular](http://es.wikipedia.org/wiki/Modelado_molecular) son conceptualmente similares al modelo HP, pero en espacios tridimensionales, normalmente considerando al solvente de forma explı́cita o implı́cita y los enlaces entre átomos (o grupos de átomos) como muelles gobernados por la ley de [Hooke](http://es.wikipedia.org/wiki/Ley_de_elasticidad_de_Hooke). En estos modelos, la energía asociada a la conformación de una molécula se calcula en un [campo de fuerzas](http://en.wikipedia.org/wiki/Force_field_(chemistry)). De esta manera, para cada conformación molecular se puede calcular su energía potencial por medio de funciones que incluyen términos que consideran las longitudes y ángulos de los enlaces, las torsiones entre grupos vecinos (diedros) y las interacciones no covalentes entre átomos (Van der Waals, Coulomb y puentes de H por ejemplo):

$$potencial(r_{N}) = w_{1} \cdot enlaces(r_{N}) + w_{2} \cdot \acute{a}ngulos(r_{N}) + w_{3} \cdot torsiones(r_{N}) + w_{4} \cdot interacciones(r_{N})
\label{eq:PnR}$$

donde $w_{1},w_{2},w_{3},w_{4}$ son los pesos de cada término y $r_{N}$ las coordenadas de $N$ átomos de la molécula.

Derivando la energía potencial entre conformaciones obtenemos la fuerza. Por tanto, una simulación de dinámica molecular (MD) es un experimento que evalúa la fuerza resultante sobre cada átomo de una molécula a lo largo de un tiempo finito. Durante el tiempo simulado la molécula va cambiando de conformación en intervalos consecutivos muy cortos, del orden de picosegundos. Actualmente se consiguen simular hasta milisegundos [@Shaw2010]. Éstos son experimentos muy costosos en cuanto a recursos de cómputo, pero permiten estudiar procesos poco accesibles experimentalmente, como en el trabajo de @Golosov2010, donde se explora el mecanismo de translocación de la RNA polimerasa. Este problema se presta muy bien a la computación distribuida, por su elevado coste, como en el experimento [Folding\@Home](http://folding.stanford.edu/) o el juego [Foldit](http://fold.it/portal/).

Este tipo de simulaciones van siendo cada vez más realistas, por ejemplo por medio de mejores modelos de solventes [@Lee2013], y se ha demostrado que predicen de manera reproducible el plegamiento de algunas proteínas de pequeño tamaño [@Lindorff-Larsen2011]. Sin embargo sigue siendo complicado aplicar MD a moléculas y complejos de gran tamaño, que requiren de simulaciones muy largas y por tanto enormes recursos computacionales. Un buen texto para ampliar estos conceptos es @Leach2001 y en español @bueren_calabuig_juan_a_2014_1066360.

![ [Figura](#fig:MDfastfolding}). Plegamientos experimentales de 12 proteínas pequeñas (rojo) superpuestas sobre estados plegados por dinámica molecular (azul), junto con sus tiempos de plegamiento. Figura de [@Lindorff-Larsen2011] reproducida con permiso. ](fig/MDfastfolding2011.png){#fig:MDfastfolding}

### Modelos aproximados

En contraste con los algoritmos de dinámica molecular, que no se pueden ejecutar en cualquier hardware, tenemos a nuestro alcance otros métodos más simples que no modelan necesariamente el proceso de plegamiento pero permiten obtener inferencias estructurales, a partir de la secuencia, de calidad suficiente para muchas aplicaciones biológicas. Al ser heurísticas, estas estrategias suelen tener un nicho de aplicación muy restringido, y su validación es normalmente empírica. A pesar de ello muchos de estos métodos han tenido y tienen un gran impacto y tienen la ventaja de que, en general, se pueden realizar en cualquier computador. Los siguientes capítulos del curso se centran en algunos de estos métodos.

Para proteı́nas podemos mencionar algunos ejemplos:

-   Observación de los patrones de sustitución de aminoácidos en familias de proteı́nas a lo largo de la evolución, que pueden explotarse para aplicaciones tan variadas como:

    -   Predicción de estructura secundaria por aprendizaje automático, normalmente por medio de redes neuronales [@Jurtz2017], como se describe en la sección [4.2](#protSS){reference-type="ref" reference="protSS"}.

    -   Algoritmos de predicción de regiones intrı́nsecamente desordenadas [@Dunker2008] y de amiloides [@Bryan2011; @Agostini2012]. Se mencionan en la sección [4.2](#protSS){reference-type="ref" reference="protSS"}.

    -   Modelos topológicos de proteı́nas de membrana, que predicen hélices transmembrana e infieren qué partes de la secuencia son citoplásmicas y exteriores [@PerezAguilar2012; @Nugent2012].

    -   Predicción de efectos y fenotipos de mutaciones no sinónimas en proteı́nas (sección [5.6](#pointmut){reference-type="ref" reference="pointmut"}).

    -   Definición de modelos evolutivos especı́ficos de familias de proteı́nas [@Arenas2017], que son la base de los protocolos de *fold recognition* de la sección [5.2](#FRsection){reference-type="ref" reference="FRsection"} y de predicción de contactos de la sección [5.5](#contactosPred){reference-type="ref" reference="contactosPred"}. Estos algoritmos están a medio camino de los de modelado estructural que se mencionan a continuación.

-   Aproximación a la estructura nativa, y a su función, a partir de otras estructuras conocidas:

    -   modelado de estructura terciaria por comparación con proteı́nas de estructura conocida (sección [5.3](#CM){reference-type="ref" reference="CM"}).

    -   protocolos de modelado de estructura terciaria a base de fragmentos, que simulan el proceso de plegamiento (normalmente denominados *ab initio*, sección [5.4](#abinitio){reference-type="ref" reference="abinitio"})

Dentro del ámbito de los ácidos nucleicos:

-   Algoritmos de predicción de estructura secundaria de ARN (sección [4.1](#SSRNA){reference-type="ref" reference="SSRNA"}).

-   Métodos de predicción de estabilidad de la doble hélice de ADN y predicción de promotores (sección [3.1](#dna1){reference-type="ref" reference="dna1"}).

-   Predicción de la estructura tridimensional de un genoma (sección [1.4](#metodosExp){reference-type="ref" reference="metodosExp"}).

![ [Figura](#fig:DNApapel}). Modelo recortable de la doble hélice de ADN. ](fig/DNApapel.png){#fig:DNApapel}

Foldit: jugando a plegar proteínas {#foldit}
----------------------------------

Una forma divertida y amena de poner en práctica muchos de los conceptos teóricos que acabamos de repasar es jugar a [*Foldit*](http://fold.it/portal/), un juego que incluye un tutorial donde se pueden aprender de manera intuitiva las reglas del plegamiento de proteínas y cómo se empaquetan los elementos de estructura secundaria para formar dominios que cumplen una función. Una vez superado el tutorial se puede jugar en comunidad resolviendo problemas de plegamiento reales [@Eiben2012; @Khatib2011; @Cooper2010]. El juego se actualiza regularmente desde el [2008](http://fold.it/portal/files/Foldit_5thanniversary.png) e incorpora ya interfaces para [Kinect](http://en.wikipedia.org/wiki/Kinect) y [Leap](http://en.wikipedia.org/wiki/Leap_Motion).

Muestro algunas capturas de pantalla del tutorial, donde se pueden deshacer choques estéricos o favorecer la formación de puentes de hidrógeno:

![ [Figura](#fig:foldit}). Capturas de pantalla del juego Foldit en su versión para Linux. ](fig/foldit.png){#fig:foldit}

![ [Figura](#fig:standalonefoldit}). Capturas de pantalla del software standaloneFoldit en su versión para Windows, libre para uso académico. A diferencia del juego, que es un cliente online, esta aplicación permite importar y exportar moléculas en formato PDB y por tanto puede usarse como herramienta de modelado interactiva [@Kleffner2017]. ](fig/standaloneFoldIt.png){#fig:standalonefoldit}

StandaloneFoldit está disponible en <https://fold.it/dist/external/standalone/quickstart.html> para Linux, MacOS y Windows.

Familiarizarse con las operaciones habituales para manipular y modificar estructuras moleculares de proteínas, por ejemplo con Foldit, facilita el aprendizaje de plataformas especializadas como <https://sbl.inria.fr>.

Estructura primaria o secuencia {#secuencia}
===============================

En estas secciones veremos dos ejemplos de algoritmos que utilizan secuencias de DNA y proteı́nas con el objeto de estudiar procesos que dependen de propiedades estructurales.

Estabilidad y deformación de un dúplex de ADN: predicción de promotores {#dna1}
-----------------------------------------------------------------------

El modelo *Nearest Neighbor* (NN) aproxima la estabilidad termodinámica de un ácido nucleico en disolución a partir de su secuencia, que se analiza como una secuencia de dinucleótidos solapantes de interacciones aditivas, cuyas energías se han determinado experimentalmente [@Breslauer1986; @SantaLucia1998].

![ [Figura](#fig:NN}). Cálculo de estabilidad (energía libre de Gibbs, $\Delta G$) a temperatura fisiológica en base al modelo NN, incluyendo un término de iniciación de dúplex, tomado de [@SantaLucia1998]. Copyright (1998) National Academy of Sciences. ](fig/NN.jpg){#fig:NN}

Inspirándose en estructuras moleculares conocidas, este tipo de modelos se han empleado para describir la lectura indirecta del DNA, por su forma, por parte de nucleosomas [@Heijden2012] o factores de transcripción [@Gromiha2004; @Espinosa2008].

![ [Figura](#fig:MGW}). (A) Estructura de un homodímero de Fis unido a un sitio de alta afinidad (PDB: [3IV5](http://www.rcsb.org/structure/3IV5)), insertando dos hélices en dos surcos mayores consecutivos. (B) Ancho del surco mayor (magenta) y menor (MGW, azul) a lo largo de la secuencia de DNA medido entre los fosfatos más cercanos. Las lineas punteadas representan los valores canónicos para B-DNA. Figura adaptada de @Hancock2013 y reproducida con permiso de los autores. ](fig/MGW.jpeg){#fig:MGW}

![ [Figura](#fig:BPgeometry}). Propiedades de pares de bases (izquierda) y dinucleótidos (derecha) que se pueden estimar a partir de la estructura. Figura tomada de [x3dna.org](http://x3dna.org/articles/seeing-is-understanding-as-well-as-believing). ](fig/BPgeom.png){#fig:BPgeometry}

Otros modelos amplían el número de vecinos considerados hasta llegar, por ejemplo, a pentámeros:

![ [Figura](#fig:NN5}). Aproximación de propiedades estructurales (MGW=minor groove width) de un dúplex de ADN por solapamiento de pentámeros, base del algoritmo [DNAshape](http://rohsdb.cmb.usc.edu). Reproducido con permiso de @Zhou2013. Este tipo de aproximaciones se están usando para enriquecer motivos de DNA reconocidos por factores de transcripción [@Yang2015]. ](fig/DNApentamers.jpg){#fig:NN5}

En esta sección aplicaremos el modelo NN a la predicción de promotores:

-   **PROBLEMA:** disponemos de coordenadas genómicas de una colección de marcos de lectura ([*Open Reading Frames, ORFs*](http://es.wikipedia.org/wiki/Marco_abierto_de_lectura)), pero desconocemos la posición de sus secuencias promotoras

-   **SOLUCIÓN PROPUESTA:** buscar los promotores en la secuencia del DNA por su menor estabilidad termodinámica

Este problema ha tenido mayor importancia en procariotas por la gran velocidad con que se han ido obteniendo sus secuencias genómicas, y el algoritmo de [@Kanhere2005] es un ejemplo de como emplear una estrategia estructural para atacar este problema. El algoritmo consiste en estimar la estabilidad helicoidal del ADN cromosómico, que se supone es menor en las regiones promotoras, donde la maquinaria transcripcional se asienta para comenzar la síntesis de ARN. En concreto este método estima la estabilidad de una (ventana de) secuencia de ADN a ambos lados de una coordenada y define como posibles posiciones promotores aquellas donde la diferencia de estabilidad en torno a una coordenada es significativa.

![ [Figura](#fig:window}). Ejemplos de ventanas de 6 y 11 nucleótidos, que sirven para promediar propiedades a lo largo de la secuencia. ](fig/window.png){#fig:window}

Este algoritmo incluye varios parámetros libres y en el artículo original se muestra como entrenarlo para obtener valores adecuados para todos ellos.

![ [Figura](#fig:Kanhere}). Algoritmo de [@Kanhere2005], que se basa en calcular la diferencia de $\Delta G$ entre dos ventanas en torno a una posición $n$. Figura reproducida con permiso de los autores. ](fig/flowKanhere.jpg){#fig:Kanhere}

Se han propuesto otras aproximaciones estructurales, como la de [@Gogni2007], que identifica regiones promotoras en base a la capacidad de deformación de los [pares de bases](http://nar.oxfordjournals.org/content/31/17/5108/F1.large.jpg), estimada por medio de extensas simulaciones moleculares precalculadas.

El repertorio de métodos para predicción de promotores en base a inferencias estructurales es limitado, pero incluye al menos: <http://bioinformatics.psb.ugent.be/software/details/ProSOM> o el algoritmo de @Song2012. Otras opciones recientes se basan en combinar diferentes fuentes por medio de algoritmos de aprendizaje [@Eser2016].

El ejercicio de esta sección consiste en completar el siguiente programa, usando los parámetros unificados de [@SantaLucia1998], para calcular la diferencia de estabilidad $D(n)$ entre dos fragmentos de 50bp y 100bp $E1(n)$ y $E2(n)$ que flanquean una región central (de 50bp) que podría albergar el promotor. A su vez, estos framentos se calculan sobre valores de estabilidad calculados sobre ventanas de secuencia de longitud 15pb en el artículo de [@Kanhere2005]:

$$E1(n) = \frac{\sum_{n}^{n+49}\Delta G}{50}$$

$$E2(n) = \frac{\sum_{n+99}^{n+199}\Delta G}{100}$$

$$D(n) = E1(n) - E2(n)$$

Como conjunto de datos para la predicción de promotores usaremos las secuencias del fichero [K12\_400\_50\_sites](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/K12_400_50_sites), que contiene coordenadas de ORFs de *Escherichia coli* con coordenadas -400,+50, con el 0 centrado cerca del codón de inicio. Qué observas al cambiar el tamaño de la ventana? <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog1.1.pl" style="color: black; text-decoration: underline;">[fuente: prog1.1.pl]</a>

Diseño de primers para PCR {#dna2}
--------------------------

La reacción en cadena de la polimerasa ([PCR](http://es.wikipedia.org/wiki/Reacci%C3%B3n_en_cadena_de_la_polimerasa)) es una metodología estándar en cualquier laboratorio de biología molecular y consta fundamentalmente de 3 fases que se repiten un número de ciclos dentro de un tubo de ensayo que se encuentra en un baño:

![ [Figura](#fig:PCR}). Diagrama de flujo de una reacción de PCR, que consiste en ciclos donde se repiten 3 fases: desnaturalización, apareamiento y elongación. En la primera el ADN se desnaturaliza separándose las dos hebras. En la segunda los cebadores o primers se hibridan con las hebras de ADN en posiciones donde las secuencias son complementarias y se forman puentes de H entre bases enfrentadas. Es una renaturalización parcial que se hace ajustando la temperatura a la secuencia de los cebadores. Finalmente, en la tercera etapa se ajusta la temperatura para favorecer la extensión de la nueva hebra a partir de los cebadores por parte de la polimerasa. El tiempo de extensión es proporcional a la longitud del producto de PCR (o amplicón) esperado en función de los cebadores diseñados por el usuario y el genoma en cuestión. Figura de [@Konietzny2003] reproducida con permiso de los autores. ](fig/PCR.gif){#fig:PCR}

Para cada aplicación de la PCR es necesario ajustar las condiciones y el diseño de la reacción, por ejemplo:

-   la duración de las fases de apareamiento y elongación

-   el tipo de cebadores o *primers* empleados y sus temperaturas de fusión $T_{m}$ (ver sección [2.1](#desnat){reference-type="ref" reference="desnat"})

-   el tipo de polimerasa utilizada

-   las cantidad de los reactivos y de ADN molde

-   la longitud del amplicón o producto de PCR obtenido

En esta sección veremos algunos de los algoritmos habituales para el diseño de cebadores, que deben cumplir al menos tres condiciones:

-   Una pareja de cebadores debe tener temperaturas de alineamiento muy cercanas para maximizar el rendimiento, lo cual suele traducirse en un contenido en GC similar, entre 50% y 60%.

-   Los primers no deben favorecer horquillas (*hairpins*) ni ser complementarios. El siguiente esquema muestra un cebador con una horquilla potencial a la izquierda y un par de cebadores que se aparean a la derecha:

                  5'GGGAAA                    5' GGGAAAATTCCAGGATCTAT 3'
                     |||| )                       ||||  ||||
         3' TATCTAGGACCTTA            3' TATCTAGGACCTTAAAAGGG 5'     

-   Tras analizar una gran colección de primers publicados en la literatura, parece que conviene evitar secuencias que terminen en GGG,GGT,ATT,CGA,TAA o TTA [@Onodera2007].

Hay muchos programas que pueden ayudar en el diseño de primers en la web, como por ejemplo:

-   [primer3](http://bioinfo.ut.ee/primer3/)

-   [Vector NTI](http://en.wikipedia.org/wiki/Vector_NTI)

-   *in silico* PCR en [procariotas](http://insilico.ehu.es/PCR/) y en [animales](http://genome.ucsc.edu/cgi-bin/hgPcr)

o estos otros para diseñar primers degenerados, que permiten reconocer y por tanto amplificar varias secuencias similares

-   [amplicon](http://amplicon.sourceforge.net/)

-   [primers4clades](http://maya.ccg.unam.mx/primers4clades/) (específico para aplicaciones filogenéticas, utiliza CODEHOP)

Sin embargo, más allá del software elegido, es importante saber cómo se calculan ciertas propiedades moleculares de los primers, para poder analizar con criterio los resultados obtenidos.

Por ejemplo, nos puede interesar calcular la $T_{m}$, que es la temperatura a la que la mitad de los primers se han hibridado con el ADN molde, o la cantidad de ADN bicatenario a cualquier temperatura, por ejemplo a la temperatura de apareamiento, la más crítica, que a menudo se aproxima como $T_{m} - 5$.

Una aproximación burda es llamada regla de Wallace, que se basa solamente en la secuencia, donde GC y AT son el número de nucleótidos G/C y A/T en la secuencia del cebador, respectivamente [@Santalucia2007]: $$T_{m} \sim 4GC + 2AT$$

Otra alternativa más precisa es la siguiente ecuación, que relaciona exactamente la temperatura con la proporción de ADN bicatenario, donde $[A]$ es la concentración de hebras en exceso (los primers), $[B]$ el ADN molde que queremos amplificar, $\Delta H$ el cambio de entalpía, $\Delta S$ el cambio de entropía y $R$ la [constante de Boltzmann](http://en.wikipedia.org/wiki/Boltzmann_constant) (R=1.987 cal/mol K): $$T_{m} = \frac{1000 \Delta H}{\Delta S + Rln([A]-\frac{[B]}{2})} - 273.15$$

En la práctica combinamos esta ecuación con el modelo *Nearest Neighbor* (NN, sección [3.1](#dna1){reference-type="ref" reference="dna1"}), usando valores experimentales de entalpía y entropía obtenidos para dinucleótidos.

Con el objetivo de probar estas recetas el siguiente ejercicio incluye:

-   usar cualquier software que conozcas (o de los citados arriba) para diseñar varios primers

-   con ayuda del siguiente código Python evaluar parejas de primers teniendo en cuenta su $T_{m}$ de fusión y su potencial de formación de horquillas

-   compara las $T_{m}$ obtenidas con las que resultan de aplicar la regla de Wallace

-   prueba a modificar el código para calcular temperaturas de alineamiento donde la proporción de primer hibridado sea por ejemplo del 95% <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog1.2.py" style="color: black; text-decoration: underline;">[fuente: prog1.2.py]</a>

Estructura secundaria {#ss}
=====================

Estructura secundaria de RNA {#SSRNA}
----------------------------

En contraste con las moléculas de DNA, que en sus papeles más comunes actúan como dobles hélices, las moléculas de RNA pueden adoptar una mayor variedad de conformaciones, igual de complejas que las de las proteínas, que a su vez les permiten tener diferentes funciones , ya sea mensajero, RNA de transferencia, ribosomal, regulador o enzima. Por primera vez en este curso vamos a ir un poco más allá de lo que expresa una secuencia lineal:

-   **PROBLEMA:** desconocemos la estructura de una molécula de hebra sencilla de RNA pero conocemos su secuencia

-   **SOLUCIÓN PROPUESTA:** predecir su estructura secundaria en base a las subsecuencias complementarias que contiene

![ [Figura](#fig:RNAss}). Estructura secundaria de un RNA (A) correspondiente a la estructura (B), tomada de [@Noller2004] y reproducida con permiso. ](fig/RNAss.png){#fig:RNAss}

La estructura secundaria de una molécula de RNA, sostenida por medio de puentes de hidrógeno (de tipo Watson-Crick y [Hoogsteen](http://en.wikipedia.org/wiki/Hoogsteen_base_pair)) entre nucleótidos, puede aproximarse a partir del conocimiento de la secuencia, aunque obviamente se pierde parte de la complejidad del plegamiento, como sugiere la figura [4.1](#fig:RNAss){reference-type="ref" reference="fig:RNAss"}. Para qué sirven este tipo de predicciones? Por ejemplo, para descubrir RNAs no codificantes, que a menudo tienen funciones biológicas importantes, como se discute en el artículo de [@Washietl2005]. Hay muchos programas disponibles que pueden ayudarnos en este tipo de tareas, como [MC-Fold \| MC-Sym](http://www.major.iric.ca/MC-Pipeline), [UNAFold](http://www.unafold.org), [Vienna](http://www.tbi.univie.ac.at/~ivo/RNA/), [RNAz](http://www.tbi.univie.ac.at/~wash/RNAz/), [infernal](http://infernal.janelia.org/).

Un programa complementario, que asigna elementos de estructura secundaria dadas unas coordenadas en formato PDB, es [DSSR](https://x3dna.org).

Aquí nos vamos a centrar en ilustrar el algoritmo de @Nussinov1978 para predecir estructura secundaria de RNA por medio de alineamientos, que usa una estrategia de [programación dinámica](http://es.wikipedia.org/wiki/Programaci%C3%B3n_din%C3%A1mica_(inform%C3%A1tica)) (DP) para maximizar el número de puentes de hidrógeno que se forman dentro de la secuencia. Éste puede decirse que es el algoritmo fundamental para resolver este problema aunque tiene algunas limitaciones. Por ejemplo, no considera la posibilidad de pseudonudos ([*pseudoknots*](http://en.wikipedia.org/wiki/Pseudoknot)) ni tiene en cuenta el apilamiento de bases (*base stacking*), un tipo de interacción que favorece la estabilidad de estas estructuras, elementos que sí son proyectados en el [software actual](http://en.wikipedia.org/wiki/List_of_RNA_structure_prediction_software) [@dotu_ivan_2014_1066354].

El código fuente que se muestra implementa este algoritmo, evaluando recursivamente hasta 4 situaciones en cada posición de la matrix DP [@Eddy2004b]:

-   caso1: nuevo par de bases alineado

-   caso2: indel en un extremo, se conserva score anterior

-   caso3: indel en extremo opuesto, se conserva score

-   caso4: bifurcación en base $k$ si hay distancia suficiente

<a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog2.1.pl" style="color: black; text-decoration: underline;">[fuente: prog2.1.pl]</a>

![ [Figura](#fig:RNAdotplot}). Estructura secundaria de una molécula de RNA y matriz (dot plot) que esquematiza sus puentes de hidrógeno. Figura tomada de [@Bernhart2006] y reproducida con permiso. ](fig/RNAdotplot.jpg){#fig:RNAdotplot}

(Des)estructura secundaria de proteı́nas {#protSS}
---------------------------------------

La estructura secundaria es una propiedad de las proteı́nas naturales en solución, que se explica por medio de una red (dinámica) de puentes de hidrógeno que conectan diferentes partes del polipéptido a escala más o menos local, formando hélices y láminas que quedan conectadas por lazos (*loops*) y regiones desordenadas, como ya recordamos en la sección [1.3.2](#SS){reference-type="ref" reference="SS"}.

Si disponemos de las coordenadas atómicas de una proteína podemos medir sus ángulos diedros para generar nuestros propios diagramas de Ramachandran, con dos fines:

-   Comprobar qué residuos de la secuencia se encuentran en conformaciones (regiones) favorables, como medida de calidad de la estructura.

-   Averiguar en base a la geometría del esqueleto proteico el estado de estructura secundaria de segmentos de residuos.

El procedimiento, dado unas coordenadas en formato PDB ([1LFU](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1lfu.pdb)), es relativamente sencillo, haciendo un poco de álgebra y trigonometría: <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog2.2.pl" style="color: black; text-decoration: underline;">[fuente: prog2.2.pl]</a>

![ [Figura](#fig:signodiedro1}). Definición de ángulo diedro, figura tomada de <http://structuralbioinformatics.com>. ](fig/signo_diedro1.jpg){#fig:signodiedro1}

Otras definiciones de estructura secundaria se basan en encontrar patrones de puentes de hidrógeno entre grupos $-CO$ y $-NH$ del esqueleto peptídico, como por ejemplo hace el software [DSSP](https://swift.cmbi.umcn.nl/gv/dssp) [@Kabsch1983] de acuerdo con esta definición energética, donde un puente válido debe tener $E<-0{.}5 kcal/mol$, $q_{1}=0.42e$, $q_{2}=0.20e$ y $r$ es una distancia interatómica en Angstroms: $$E = q_{1} q_{2} \left[ \frac{1}{r_{ON}} + \frac{1}{r_{CH}} - \frac{1}{r_{OH}} - \frac{1}{r_{CN}} \right] \cdot 332 \ \mathrm{kcal/mol}
\label{eq:dssp}$$

El software [STRIDE](http://webclu.bio.wzw.tum.de/stride/) [@Frishman1995] es otro programa para este fin que en experimentos de validación mejora las asignaciones de estructura secundaria de DSSP.

Sin embargo, frecuentemente el problema es todavía más complicado:

-   **PROBLEMA:** tenemos una secuencia proteica pero no conocemos su estructura

-   **SOLUCIÓN PROPUESTA:** reconocer en la secuencia segmentos que formen hélices y láminas, y lazos para caracterizar su topología o estructura secundaria

Si calculamos alineamientos múltiples de secuencias de proteínas homólogas, las columnas del alineamiento resultante permiten deducir patrones de sustitución de aminoácidos que son específicos de posición. Esta fuente de información evolutiva, combinada con algoritmos basados en [redes neuronales](https://en.wikipedia.org/wiki/Artificial_neural_network) más o menos [profundas](https://bioinfoperl.blogspot.com/2020/04/redes-neuronales-profundas.html), permite predecir con una precisión cercana al 75% la estructura secundaria en 3 estados (H=hélice alfa, E=lámina beta y C=coil). Es evidente que se pierde información con este alfabeto, pero la estructura inferida puede tener muchas aplicaciones a la hora de diseñar experimentos y algoritmos que trabajen sobre la estructura terciaria.

Hay una buena exposición de este tema en [@Jones1999], donde se presenta el algoritmo [PSIPRED](http://bioinf.cs.ucl.ac.uk/psipred) y se evalúa la precisión de las asignaciones de estructura secundaria de varias maneras, incluyendo la función: $$Q_{3} = \frac{\sum\limits_{i=H,E,C}{corrpred_{i}}}{\sum\limits_{i=H,E,C}{obs_{i}}} \times 100$$

En @Jurtz2017 se explica en mayor detalle cómo funcionan este tipo de predictores, incluyendo [código fuente en python2.7](https://github.com/vanessajurtz/lasagne4bio) para programar uno.

![ [Figura](#fig:psipred}). Ejemplo de predicción de estructura secundaria de PSIPRED, obtenida en el servidor [PSIPRED](http://bioinf.cs.ucl.ac.uk/psipred). ](fig/ss1.png){#fig:psipred}

PSIPRED es aceptado como uno de los mejores predictores, pero hay muchos otros algoritmos de predicción de estructura secundaria y la mejor manera de compararlos es por medio de evaluaciones automáticas a ciegas. Desgraciadamente, este tipo de iniciativas, como [LiveBench](http://en.wikipedia.org/wiki/LiveBench) o EVA, que recolectan datos de distintos algoritmos a medida que crece el PDB, son financiadas por poco tiempo y mueren.

Tras la aparición de los primeros predictores de estructura secundaria empezó a ser evidente que muchas proteínas, sobre todo de vertebrados, no tenían aparentemente una estructura ordenada, al menos en ciertos estados fisiológicos (ver por ejemplo el repositorio [Disprot](http://www.disprot.org) [@Sickmeier2007; @yruela_inmaculada_2014_1066352]). Hoy sabemos que muchas proteínas ordenadas pueden contener segmentos desordenados o dúctiles [@Lobanov2010]. Como resultado se diseñaron predictores para un cuarto estado, el de desorden intrínseco, y se han creado recursos para la anotación de estas secuencias como [D2P2](http://d2p2.pro).

En el caso de PSIPRED, la evolución es un software de nombre [DISOPRED](http://bioinfadmin.cs.ucl.ac.uk/downloads/DISOPRED) [@Ward2004], que además de reconocer elementos de estructura secundaria estima la probabilidad de que cada residuo esté desordenado, sin pertenecer a ninguna clase de estructura secundaria.

La mayoría de predictores de estructura secundaria y desorden tienen mejores resultados cuando extraen información evolutiva de secuencias homólogas. Sin embargo, esto implica que estos algoritmos son sensibles al contenido de las bases de datos de secuencias públicas, como se muestra en la siguiente figura:

![ [Figura](#fig:disopredTime}). Comparación de predicciones de PSIPRED (estructura secundaria) y DISOPRED2 (desorden) para la secuencia NAC81 de Arabidopsis thaliana calculadas sobre versiones de 2010 y 2014 de la colección de secuencias [uniref90](https://www.uniprot.org/help/uniref). Se marcan en rojo los segmentos desordenados, las hélices en azul y las láminas $\beta$ en verde. Figura de @Yruela2014. ](fig/disopredTime2.png){#fig:disopredTime}

Otros predictores que combinan estructura secundaria y otras propiedades son [s2D](http://www-mvsoftware.ch.cam.ac.uk/) o o [SSpro](http://scratch.proteomics.ics.uci.edu/), rayando el %90 en las validaciones de sus autores [@Magnan2014]. Probablemente se alcanzado ya el techo para predicciones de 3 estados, pero queda espacio para mejorar las predicciones de los 8 estados de DSSP [@Yang2018].

De acuerdo con meta-análisis recientes los mejores predictores de desorden son [DISOPRED](http://bioinf.cs.ucl.ac.uk/psipred/?disopred=1) y [PrDOS](http://prdos.hgc.jp/cgi-bin/top.cgi) [@Wang2016; @Meng2017]

El ejercicio de esta sección consiste en calcular la estructura secundaria de una proteı́na del [Protein Data Bank](https://www.rcsb.org) de 3 maneras distintas, con el fin de compararlas:

-   por medio de PSIPRED, que en realidad es un predictor,

-   modificando el código [fuente: prog2.2.pl](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog2.2.pl), calculando segmentos de secuencia que tengan el mismo estado de estructura secundaria según el diagrama de Ramachandran y

-   por medio del programa STRIDE, simplificando segmentos de estructura secundaria (H=G,H,I; E=E,B y C=resto de estados)

-   alinea las estructuras secundarias en alfabeto simplificado de tres letras y describe las diferencias observadas

-   debes obtener los ejecutables necesarios por tu cuenta

Estructura terciaria {#s3}
====================

De ahora en adelante nos metemos un poco más en el laberinto de la estructura molecular y dejamos definitivamente atrás las representaciones de proteínas o ácidos nucleicos como secuencias lineales, puesto que no sirven para capturar las relaciones espaciales entre diferentes partes o elementos de estructura secundaria de una misma molécula.

Comparación de estructura terciaria entre proteínas {#compS3}
---------------------------------------------------

El hecho de que la estructura terciaria está más conservada que la secuencia (ver sección [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"}) podemos aprovecharlo para buscar posibles relaciones filogenéticas remotas entre proteínas:

-   **PROBLEMA:** disponemos de las coordenadas de dos proteínas A y B y queremos calcular cuánto se parecen sus estructuras

-   **SOLUCIÓN:** buscar las subestructuras de máximo tamaño subA y subB que minimizan la distancia entre átomos equivalentes (ver sección [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"})

Repasemos algunos algoritmos fundamentales para calcular la similitud estructural entre parejas de proteínas (hay alguno más en la [WikipediA](http://en.wikipedia.org/wiki/Structural_alignment)):

-   Conversión de información estructural en secuencias usando un alfabeto a medida para acelerar la comparación ([Foldseek](https://search.foldseek.com/search))

-   Alineamiento estructural iterativo ([STAMP](http://www.compbio.dundee.ac.uk/downloads/stamp/)). El primer borrador de alineamiento se calcula con ayuda de matrices de sustitución de aminoácidos como [BLOSUM](https://en.wikipedia.org/wiki/BLOSUM). Éste sirve para calcular la superposición correspondiente y permite refinar el conjunto de residuos equivalentes, aquellos por debajo de cierto umbral de distancia. Estas iteraciones de alineamiento y definición de sobconjuntos de residuos equivalentes se repiten hasta que convergen y el RMSD no mejora (ver @Chothia1986 y sección [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"}).

-   Doble programación dinámica para primero) establecer fragmentos localmente similares entre ambas estructuras y segundo) estimar el subconjunto de fragmentos que producen una superposición óptima ([SSAP](http://sillitoe.cathdb.info/tools/cath-ssap)). Más detalles en este [enlace](http://en.wikipedia.org/wiki/Structural_alignment#SSAP).

-   Comparación de matrices de contactos/distancias ([DALI](http://ekhidna.biocenter.helsinki.fi/dali_server)). En vez de trabajar con péptidos en 3D, algo que requiere calcular rotaciones y transforamciones, esta familia de métodos primero convierten cada estructura a su matriz de distancias correspondiente, para luego compararlas entre si.

-   Minimización de la información requerida para reconstruir las coordenadas de una estructura dadas las de la otra ([mmligner](http://lcb.infotech.monash.edu.au/mmligner)). La virtud de este aproximación es que prescinde de la elección subjetiva de umbrales y define de manera precisa la superposición óptima.

-   Superposición de factores de transcripción para deducir el alineamiento correcto de sus sitios *cis* ([TFcompare](https://hub.docker.com/r/eeadcsiccompbio/tfcompare))

Puedes ampliar detalles de estos algoritmos en @pascual_garcia_alberto_2014_1066346.

![ [Figura](#fig:dali}). Tres estrategias (rígida, flexible y elástica) para comparar la estructura terciaria de dos proteínas con dos dominios (círculos) con 4 residuos cada uno, separados por una secuencia de longitud variable. Arriba derecha: la superposición rígida tiene dos opciones: alinear un total de 5 residuos equivalentes ($Ne$) con RMSD bajo o alinear todos ($Ne=8$) con un RMSD alto. Abajo izquierda: una superposición flexible rompe la estructura larga en dos subestucturas para optimizar el RMSD sobre 4 residuos en cada dominio. Abajo derecha: la comparación de matrices de distancias permite alinear ambos dominios maximizando $Ne$. Figura tomada de @Hasegawa2009 y reproducida con permiso. ](fig/3Dsuper.jpg){#fig:dali}

![ [Figura](#fig:tfcompare}). Superposiciones de dominios de unión a DNA (DBD) de factores de transcripción, que ponen de manifiesto su mecanismo, no siempre conservado, de reconocimiento de sus cis-elementos (DBS). Figura tomada de @Sebastian2013. ](fig/tfcompare.png){#fig:tfcompare}

Hay disponibles muchos otros programas disponibles para la comparación estructural de proteínas, y cada usuario tiene el suyo preferido. A qué se debe esto? La razón es que no existe una definición totalmente satisfactoria del alineamiento estructural correcto, que es en definitiva la función que todos estos algoritmos tratan de optimizar. De hecho, ni siquiera está claro si las taxonomías estructurales clásicas, como [CATH](http://www.cathdb.info) o [SCOP](http://scop.berkeley.edu) [@Csaba2009], son compatibles con la evidencia disponible sobre la evolución de los plegamientos (*folds*), que actualmente se imagina como un proceso discreto sólo hasta cierto punto [@Taylor2002; @Pascual2009; @Sadowski2010; @Andreeva2014]. De hecho [SCOP2](http://scop2.mrc-lmb.cam.ac.uk/) se hizo para superar esas limitaciones. Otra complicación adicional es que algunos plegamientos pueden verse como permutaciones circulares de elementos de estructura secundaria de otros [@Schmidt-Goenner2010].

A pesar de estas dificultades, en general aceptamos que cada superfamilia de proteínas es un **clúster** de estructuras muy similares, que se pueden superponer aunque su secuencia sea muy diferente, y que cada plegamiento es un subconjunto de superfamilias que comparten una topología de estructura secundaria.

Lo habitual cuando se publica un nuevo método es compararlo con otros preexistentes. Estas comparaciones, si son rigurosas y reproducibles, pueden ayudar en la tarea de seleccionar un programa idóneo para esta tarea. El algoritmo MAMMOTH, con el que vamos a trabajar, se resume en estos pasos, en palabras textuales de sus autores [@Ortiz2002]:

> 1.- From the Calpha trace, compute the unit-vector U-RMS between all pairs of heptapeptides of both model and experimental structure. The U-RMS is described in: Kedem, Chew & Elber (1999) Proteins 37(4):554-64, and in Chew, Huttenlocher, Kedem & Kleinberg (1999) J.Comp.Biol. 6, 313-325. This is a measure sensitive to the local structure.
>
> 2.- Use the matrix derived in step 1 to find and alignment of local structures that maximizes the local similarity of both the model and the experimental structure. For that, use a global alignment method with zero end gaps, as described in Needleman & Wunsch (1970) J.Mol.Biol. 48, 443-453.
>
> 3.- Find the maximum subset of similar local structures that have their corresponding Calphas close in cartesian space. \"Close\" is considered here as a distance less or equal than 4.0 A. The method to find this subset is a small variant of the MaxSub algorithm from the Fischer group: Siew, Elofsson, Rychlewski & Fischer (2000) Bioinformatics, in press.
>
> 4.- Obtain the probability of obtaining the given proportion of aligned residues (with respect to the shortest protein model) by chance. This metric (E-value) is then used as the final score (or the corresponding Z-score, both are equivalent for gaussian distri- butions, however the Z-score is a more manegable index). In order to obtain this value, an approach similar to that of Levitt & Gerstein (1998) PNAS 95, 5913 is used, as described in Abagyan & Batalov (1997) J.Mol.Biol. 273, 355-368. The E-value estimation is based on extreme-value fitting. In a test set with the SCOP database, it shows rather good performance.

MAMMOTH fue comparado con varios métodos, como se ve en esta figura:

![ [Figura](#fig:mammoth}). Semejanza de MAMMOTH respecto a otros algoritmos de comparación de estructura de proteínas, incluyendo el criterio de un experto humano (Murzin). Figura tomada de @Ortiz2002. Copyright (2002) Protein Science. ](fig/mammoth_bench.jpg){#fig:mammoth}

MAMMOTH es junto con DALI de los mejores programas, porque además de generar superposiciones y alineamientos satisfactorios, sus medidas numéricas de similitud devuelven valores que se ajustan a la evaluación visual de la superposición obtenida. En concreto, MAMMOTH devuelve para cada alineamiento una puntuación y su valor esperado asociado (*E-value*), que podemos interpretar de manera análoga a los valores esperados de BLAST, superando las limitaciones del RMSD para comparar estructuras que solamente se parecen en algunas regiones [@Siew2000]. Además, hay una versión de MAMMOTH que permite calcular [alineamientos múltiples](https://ub.cbm.uam.es/software/mammothm.php).

Para superar las limitaciones del RMSD, que da el mismo peso a regiones del core que a regiones divergentes, @Zhang2004 propusieron otra función, el TM-score, que disminuye el peso de las parejas alineadas a mayor distancia, es menos sensible a la longitud de las estructuras comparadas y toma valores entre 0 y 1:

$$TMscore = max[  \frac{1}{L_{Q}}  \sum_{i=1}^{L_{T}} \frac{1}{ 1 + (\frac{d_{i}}{d_{0}})^{2} } ]$$

Aquí $max$ es el valor máximo obtenido en todas las superposiciones calculadas, $L_{Q}$ es la longitud de la estructura Q o *query*, $L_{T}$ es el total de residuos alineados a la estructura T o *template*, $d_{i}$ es la distancia entre la pareja $i$ de residuos y $d_{0}$ el factor de escala para normalizar por longitud de secuencia.

Para calcularlo de manera óptima podemos usar su algoritmo TM-align [@Zhang2005], cuyo código fuente esta disponible en [TMalignc.tar.gz](http://zhanglab.ccmb.med.umich.edu/TM-align/TM-align-C/TMalignc.tar.gz). La función TM-score se ha convertido en el estándar para medir el parecido entre estructuras, ya que se acepta que un valor de 0.5 garantiza un plegamiento similar.

De todos modos, hay una gran variedad de software para esta tarea, como se muestra por ejemplo en esta [lista de la WikipediA](http://en.wikipedia.org/wiki/Structural_alignment_software).

Para aprender a hacer alineamientos/superposiciones estructurales, y a interpretarlos, podemos hacer este ejercicio:

-   Visita [SCOPe](http://scop.berkeley.edu), elige una clase (ver figura [1.23](#fig:foldclassif){reference-type="ref" reference="fig:foldclassif"}) y selecciona un grupo de 5 estructuras de proteı́nas que pertenezcan a la misma superfamilia, para después

    -   descargar los archivos PDB correspondientes,que contienen las coordenadas atómicas, del [Protein Data Bank](https://www.rcsb.org/pdb) y

    -   compara al menos una pareja de estructuras con MAMMOTH

    -   compara al menos una pareja de estructuras con MAMMOTH e inspecciona los archivos de salida generados (`maxsub_sup.pdb,maxsub_sup2.pdb,rasmol.tcl`)

    -   (el ejecutable se encuentra en `/home/compu2/algoritmos3D/soft/mammoth-1.0-src`)

-   Visualiza la superposición generada, con Rasmol (usando la opción ` -script rasmol.tcl`) y con PyMOL

-   Puedes probar a superponer estructuras directamente en [PyMOL](https://pymol.org/dokuwiki/doku.php?id=command:align)

-   Prueba MAMMOTH con el fin de comparar una estructura problema (una de las 5) contra una biblioteca de estructuras en formato PDB (las otras 4), como si fuera BLAST. Cuál de las 4 estructuras sería el mejor molde o *template*) Cuál es el límite esperado de precisión, en términos de RMSD, que alcanzaríamos con cada molde?

-   Calcula para algunas de las superposiciones el [TM-score](http://zhanglab.ccmb.med.umich.edu/TM-score/).

*Protein fold recognition* {#FRsection}
--------------------------

Al analizar secuencias genómicas frecuentemente encontraremos marcos de lectura (teóricos) que codifican para proteínas que aparentemente no se parecen a ninguna otra (llamadas a veces *orphans* en la literatura), o que sólo tienen similitudes obvias con proteínas de función desconocida. Esto puede deberse a que de veras son moléculas observadas por primera vez, o como vimos en [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"}, a que la evolución ha conservado en mayor grado la estructura y topología de las proteínas homólogas que sus secuencias.

La segunda posibilidad ha justificado una familia de métodos llamados genéricamente de *Fold Recognition* (FR), que tienen como objeto reconocer a qué tipo de plegamiento (de los conocidos) se debe asignar una secuencia problema, especialmente cuando búsquedas más convencionales con [BLAST](http://blast.ncbi.nlm.nih.gov/Blast.cgi) o [FASTA](http://www.ebi.ac.uk/Tools/fasta/index.html) han fracasado. Históricamente algunos de estos métodos se han llamado de [*threading*](http://en.wikipedia.org/wiki/Threading_%28protein_sequence%29), ya que ciertos algoritmos literalmente enhebran la secuencia problema en patrones de coordenadas conocidas, normalmente un subconjunto no redundante del PDB, para ver si es compatible con alguno, como en la siguiente figura:

![ [Figura](#fig:threading}). Diagrama de flujo de los algoritmos de reconocimiento de plegamiento (FR). Figura tomada de [@Guo2008]. Copyright (2008) Frontiers in Bioscience. ](fig/threading.jpg){#fig:threading}

El problema de FR lo podemos plantear así:

-   **PROBLEMA:** conocemos la secuencia de una proteína, pero desconocemos su tipo de plegamiento y su función

-   **SOLUCIÓN PROPUESTA:** comparar la secuencia con todos los plegamientos conocidos, calcular el grado de parecido/compatibilidad con cada uno de ellos y devolver una lista ordenada

Se han publicado muchos algoritmos diferentes de FR; en todos ellos de alguna manera se asigna una estructura T a una secuencia A:

-   Por medio de búsquedas PSI-BLAST bidireccionales transitivas [@Koretke2002]. La idea es que si buscamos secuencias homólogas a partir de A llegamos a encontrar, en alguna iteración, la secuencia T entre los resultados con cierta significancia estadística. De la misma manera, a partir de la secuencia de T llegamos a la secuencia A.

-   Representando cada plegamiento o *fold* por medio de las secuencias conocidas que se pliegan en esa conformación y comparten estructura secundaria. Esto se puede hacer por medio de perfiles de secuencia [@Gribskov1987], que son matrices sustitución de aminoácidos específicas de posición, o [modelos ocultos de Markov](http://en.wikipedia.org/wiki/Hidden_Markov_model), que modelan explícitamente con qué probabilidad se pueden emitir secuencias compatibles con ese plegamiento.

-   Por medio de alineamientos secuencia-perfil

-   Por medio de alineamientos secuencia-perfil o los más sensibles perfil-perfil [@Soding2005] o los más sensibles perfil-perfil [@Soding2005] que son la razón del éxito del servidor [HHpred](https://toolkit.tuebingen.mpg.de/#/tools/hhpred).

-   Usando potenciales estadísticos para evaluar la cercanía de los residuos de una secuencia dado un plegamiento (lo que llamamos *threading* [@Threader1992]). Estos métodos requieren precalcular, sobre una colección de plegamientos no redundantes, con qué frecuencia y a qué distancia se forman parejas de residuos en las estructuras conocidas.

Probablemente la mejor manera de evaluar objetivamente y elegir un método de FR son experimentos colectivos a ciegas con secuencias cuyas estructuras experimentales se hacen públicas tras las entrega de las predicciones. Hay dos tipos de experimentos de este tipo: [CASP](http://predictioncenter.org/index.cgi?page=public_serv), que mide bianualmente la competencia de los algoritmos de los grupos participantes, y [CAMEO](https://www.cameo3d.org), que hace evaluaciones continuas no supervisadas.

En palabras de @Kelley2015, desarrollador principal de [Phyre2](http://www.sbg.bio.ic.ac.uk/phyre2), uno de los más completos, los mejores predictores tienen resultados indistinguibles en la mayor parte de los casos, pero en los casos mas complejos desde hace tiempo destaca por su consistencia y superiores resultados [I-TASSER](http://zhanglab.ccmb.med.umich.edu/I-TASSER).

Estas herramientas web son adecuadas para estudiar unas pocas secuencias, pero si queremos hacer un experimento de FR a gran escala, entonces buena idea instalar localmente el software elegido, como por ejemplo [hh-suite](https://github.com/soedinglab/hh-suite), el software que da vida a [HHpred](https://toolkit.tuebingen.mpg.de/#/tools/hhpred).

El siguiente programa es un prototipo de alineamiento perfil-perfil que usa además predicciones de estructura secundaria (ver figura [4.4](#fig:psipred){reference-type="ref" reference="fig:psipred"}) para guiar el alineamiento. Es un algoritmo de programación dinámica, que puedes comprender mejor con ayuda del [*Sequence Alignment Teacher*](http://protein.bio.puc.cl/websoftware/web/?sid=3) [@Ibarra2010].

Para probarlo necesitaras descargar los archivos de entrada ([1ngk\_A.pssm](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1ngk_A.pssm), [1s69\_A.pssm](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1s69_A.pssm), [1ngk\_A.psipred](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1ngk_A.psipred), [1s69\_A.psipred](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1s69_A.psipred)): <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog3.2.pl" style="color: black; text-decoration: underline;">[fuente: prog3.2.pl]</a>

Modelado de proteı́nas por homología {#CM}
-----------------------------------

Con las herramientas que hemos estado manejando ya estamos preparados para modelar proteı́nas. En este contexto modelar significa hacer una predicción de cómo se disponen los átomos de una proteı́na conocida su secuencia, con el fin de estudiar su función molecular, su historia evolutiva o, si el modelo es bueno, diseñar o muestrear ligandos e incluso calcular sus afinidades [@Singh2010]. Asimismo este tipo de modelos se usan mucho para estudiar el efecto de mutaciones puntuales [@Kellogg2011].

-   **PROBLEMA:** disponemos de la secuencia de una proteína A y quisiéramos conocer, aunque sea de manera aproximada, su estructura tridimensional

-   **SOLUCIÓN PROPUESTA:** estimar coordenadas cartesianas para la mayoría de los átomos de A, en base a la estructura conocida de proteínas similares, que llamamos plantillas, moldes, o *templates*

Esta metodología se llama modelado comparativo o por homología y se describe en profundidad en este artı́culo de @Fiser2003. artı́culo de @Fiser2003. Hay fundamentalmente dos estrategias, que en general requieren alineamientos entre la secuencia problema y los posibles moldes:

-   Ensamblaje de grandes fragmentos rígidos, incluso el plegamiento entero, obtenidos de estructuras similares alineadas por medio de su secuencia primaria y secundaria ([SWISS-MODEL](http://swissmodel.expasy.org) o [ROBETTA](http://robetta.bakerlab.org). Esta metodología corta y pega literalmente fragmentos del esqueleto peptídico de estructuras conocidas.

-   Modelado por satisfacción de restricciones (distancias, ángulos) moleculares extraídas de bases de datos y estructuras similares alineadas ([MODELLER](https://salilab.org/modeller/)). Este método, conceptualmente similar a la resolución por NMR (ver sección [1.4](#metodosExp){reference-type="ref" reference="metodosExp"}), produce un conjunto de estructuras para la secuencia A, todas ellas compatibles con las restricciones observadas en los *templates*.

El algoritmo genérico de modelado comparativo puede dividirse en varios pasos, ilustrados en la figura [5.6](#fig:CMflow){reference-type="ref" reference="fig:CMflow"}:

-   1\. Identificar por similitud de secuencia dominios $D_{1..d}$ en la proteı́na $S$ que queremos modelar.

-   2\. Buscar y alinear estructuras molde $M_{1..m}$ que nos sirvan para modelar uno o más dominios de $S$. Cada dominio con al menos un molde es potencialmente modelable.

-   3\. Para cada dominio $D_{i}$ modelable:

    -   3.1. Refinar el alineamiento local de cada segmento alineado del molde.

    -   3.2. Tomar las coordenadas peptídicas (o descriptores moleculares) de la estructura molde alineada.

    -   3.3. Copiar los [rotámeros](https://en.wikipedia.org/wiki/Backbone-dependent_rotamer_library) de las cadenas laterales de los aminoácidos conservados en el alineamiento.

    -   3.4. Modelar los rotámeros de los residuos que mutan respecto al molde, con ayuda de una [biblioteca](http://dunbrack.fccc.edu/lab/bbdep2010).

        ![ Ángulos que definen los rotámeros de las cadenas laterales. []{label="fig:rotamer"}](fig/rotamer.jpg){#fig:rotamer}

    -   3.4. Añadir los segmentos, normalmente lazos o loops,

    -   3.4. Añadir los segmentos, normalmente lazos o loops, correspondientes a *gaps* en la secuencia alineada del molde.

    -   3.5. Refinar 1 ó más modelos completos $P_{n}$ con el objeto de eliminar errores obvios de estructura, como impedimentos o choques estéricos.

    -   3.6. Evaluar los modelos $P_{n}$ y estimar su calidad, por medio de aplicaciones como [ProQ3](http://proq3.bioinfo.se), [Verify3D](http://services.mbi.ucla.edu/Verify_3D) o [FiltRest3D](http://filtrest3d.genesilico.pl/filtrest3d/index.html).

El paso 2 es el más determinante sobre la calidad del modelo y de hecho marca el techo de precisión de la metodología [@ContrerasMoreira2005]. Es además un paso crítico en el sentido de que si el alineamiento $M_{i}$ es malo, el modelo resultante será malo, como ya vislumbramos en la sección [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"}. Para modelos complicados será necesario explorar diferentes combinaciones de moldes y alineamientos para encontrar la mejor solución. Si la secuencia problema es multidominio o multimérica puede ser necesario modelar su estructura cuaternaria [@Tramontano2017], con herramientas especiales como [BAM](http://dunbrack.fccc.edu/lab/bam).

Con el objeto de explicar en mayor detalle el algoritmo, el siguiente código implementa los pasos 3.1 y 3.2, quizás los más fundamentales tras el el paso 2. El programa usa como ejemplo secuencias y estructuras ya utilizadas en el apartado [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"} ([1gd6.pdb](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1gd6.pdb)): <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog3.3.py" style="color: black; text-decoration: underline;">[fuente: prog3.3.py]</a>

Como en otros campos de la biología computacional, el repertorio de software para modelar proteínas es muy extenso, y constantemente incluye nuevas herramientas que sustituyen a otras que envejecen. Un buen punto de partida para elegir la mejor solución son los *rankings* que actualiza cada dos años [CASP](http://predictioncenter.org/index.cgi?page=public_serv), aunque probablemente los programas de modelado preferidos por los usuarios son SWISS-MODEL en la Web y MODELLER como instalable.

![ [Figura](#fig:CMflow}). Algoritmo genérico de modelado comparativo. Figura tomada de @Fiser2003. Copyright (2003) Methods in Enzymology. ](fig/CMflow.png){#fig:CMflow}

![ [Figura](#fig:CMbench}). Los errores en modelado comparativo se disparan al usar estructuras molde con identidades bajas. Este comportamiento se observa con diferentes herramientas de modelado, incluyendo SWISS-MODEL. Figura de @Contreras-Moreira2002b. ](fig/figure_3_contrera_review_final.png){#fig:CMbench}

En la práctica podemos hacer nuestros modelos por homología, con la opción de controlar todos los pasos del procedimiento, por medio del programa [MODELLER](https://salilab.org/modeller) [@Sali1993], disponible sin costo para usuarios académicos. El programa tiene [múltiples posibilidades](https://salilab.org/modeller/tutorial/), pero en este ejemplo nos centramos en el caso más sencillo consistente en hacer un modelo a partir de un sólo molde o *template*, estimando su calidad del modelo por medio de la función DOPE [@Shen2006]:

-   Secuencia problema: [FNR](http://www.expasy.org/uniprot/FNR_ECOLI), regulador transcripcional de *Escherichia coli*.

-   Busca, por ejemplo usando PSI-BLAST, secuencias similares (probablemente homólogas) cuya estructura esté en el PDB (moldes o *templates*).

-   Para cada uno de los *templates* interesantes sigue estos pasos:

    -   descarga el fichero de coordenadas del [PDB](https://www.rcsb.org/pdb) y extrae la secuencia S contenida en los campos `ATOM`

    -   alinea la secuencia S de las coordenadas con la secuencia problema (FNR, por ejemplo con [clustal-omega](https://www.ebi.ac.uk/Tools/msa/clustalo) o usando el mismo alineamiento de BLAST) y crea un archivo con extensión `.ali` con este formato, donde `structureX` es el molde, `sequence` es la secuencia problema o *query* y los demás campos definen el rango de residuos alineados del *template*, y su resolución:

            C; Alineamiento de muestra en formato PIR
            >P1;1PDB
            structureX:1PDB:1    :A:106  :A:nombre_template:: 1.90: 
            AFVVTDNCIKCKYTDCVEVCPVDCFYEGPNFLVIHPDECIDCALCEPECPAQAIFSEDEVPEDMQEFIQLNAELA
            EVWPNITEKKDPLPDAEDWDGVKGKLQHLER*
            >P1;query
            sequence:query:::::::0.00: 0.00
            AYVINDSC--IACGACKPECPVNIIQGS--IYAIDADSCIDCGSCASVCPVGAPNPED-----------------
            -------------------------------*

    -   genera un guión o *script* para MODELLER como `guion_nombre_template.py`:

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

    -   ahora ejecuta MODELLER (por ejemplo poniendo en el terminal: `$ mod9v8 guion_template.py` y al terminar revisa `guion_nombre_template.log` para comprobar la evaluación empírica del modelo o modelos obtenidos

Modelado de proteı́nas *ab initio* {#abinitio}
---------------------------------

Hablamos de protocolos *ab initio* cuando tratamos de modelar el plegamiento de un polipéptido solamente a partir de su secuencia y de la fı́sica [@Baker2001]. Sin embargo, los métodos de este tipo más exitosos hasta la fecha reconstruyen la estructura terciaria a base de pequeños fragmentos cortados de estructuras conocidas y seleccionados por similitud de secuencia.

El mejor ejemplo es el algoritmo Rosetta [@Simons1997], implementado en el servidor web [ROBETTA](http://robetta.bakerlab.org), que permite modelar secuencias cortas cuando no hay moldes que alineen con la secuencia problema, ni siquiera por *fold recognition* (ver sección [5.2](#FRsection){reference-type="ref" reference="FRsection"}). Usa fragmentos de 9 aminoácidos de longitud. En este caso podemos definir el problema tipo de esta manera:

-   **PROBLEMA:** disponemos de la secuencia de una proteína A y quisiéramos conocer, aunque esa de manera aproximada, su estructura tridimensional

-   **SOLUCIÓN PROPUESTA:** combinar fragmentos tomados de estructuras del PDB, generar conformaciones alternativas y seleccionar las mejores

![ [Figura](#fig:Rosetta}). Resumen del protocolo Rosetta, tomado de @Kaufmann2010. A) Se seleccionan de una biblioteca los fragmentos con secuencias mas parecidas a los $K$-meros de la secuencia problema ($K=9$). B) Combinación de fragmentos solapantes para generar muchas conformaciones alternativas. C) Optimización de conformaciones con funciones que evalúan interacciones no locales. Copyright (2010) Biochemistry. ](fig/rosetta.jpg){#fig:Rosetta}

Este tipo de algoritmos requieren tener precalculada una biblioteca de fragmentos de longitud $K$ de estructura conocida, funciones para seleccionar los mejores fragmentos para cada $K$-mero de la secuencia problema, funciones de evaluación que permitan descubrir conformaciones que se parezcan a las nativas, y muchos recursos computacionales, dado que todos estos pasos son costosos. Otro algoritmo que funciona tanto para *fold recognition* como para modelado *ab initio* es [I-TASSER](http://zhanglab.ccmb.med.umich.edu/I-TASSER):

![ [Figura](#fig:ITASSER}). Resumen del protocolo TASSER. Figura de @Wu2007, reproducida con permiso de los autores. ](fig/ITASSER.jpg){#fig:ITASSER}

Modelado de proteínas por predicción de contactos {#contactosPred}
-------------------------------------------------

Las matrices de contactos (ver sección [1.3.3](#estr34){reference-type="ref" reference="estr34"}) han sido durante mucho tiempo una fuente de inspiración de métodos de predicción estructural, con la idea subyacente de \"si somos capaces de predecir con información evolutiva qué residuos de una secuencia contactan, entonces podremos resolver su estructura\" [@Gobel1994; @deJuan2013].

La información evolutiva en cuestión es normalmente un alineamiento múltiple de secuencias homólogas, que se espera capturen de forma implícita las limitaciones que impone la estructura terciaria de un dominio a las sustituciones de aminoácidos que contactan. La función matemática que se emplea habitualmente para estudiar esto es la [información mutua](http://es.wikipedia.org/wiki/Informaci%C3%B3n_mutua) (MI), que mide la dependencia entre dos variables, en este caso columnas de un alineamiento.

![ [Figura](#fig:EVfold1}). Las mutaciones correlacionadas entre columnas de un alineamiento múltiple se pueden emplear para predecir contactos entre residuos en el plegamiento. Figura tomada de [@Marks2011] y reproducida con permiso de los autores. ](fig/EVfoldcorr.png){#fig:EVfold1}

Por tanto, el problema de la predicción de contactos se puede plantear así:

-   **PROBLEMA:** conocemos la secuencia de una proteína y las de muchas secuencias homólogas

-   **SOLUCIÓN PROPUESTA:** alineamos las secuencias, buscamos posiciones que muestren evidencia de coevolución y buscamos plegamientos compatibles con esos contactos

El algoritmo [EVfold](http://EVfold.org) emplea estos elementos para hacer predicciones de contactos de alta calidad, ya que es capaz de distinguir entre posiciones de la secuencia que directamente contactan (causativas) de las que correlacionan simplemente porque contactan con un mismo residuo (transitivas). Usando su terminología, MI es un modelo local de probabilidad de contactos, que ellos son capaces de corregir y convertir en un modelo global usando conceptos de la mecánica estadística y la maximización de la entropía. El modelo global se llama de Información Directa (DI) [@Marks2011].

![ [Figura](#fig:EVfold1.1}). Definición de contactos entre residuos (A,B,C,D) y de correlaciones directas y transitivas. Figura tomada de [@Marks2012]. Copyright (2012) Nature Biotechnology. ](fig/EVfold22.jpg){#fig:EVfold1.1}

![ [Figura](#fig:EVfold2}). La inferencia de contactos entre residuos es mejor con el modelo global (DI, ver texto) que con el modelo local MI. La figura muestra predicciones de contactos para las proteínas ELAV4 (derecha) y RAS (izquierda). Las predicciones globales se reparten uniformemente por la secuencia y se solapan mejor con los contactos observados en estructuras experimentales. Figura tomada de [@Marks2011] y reproducida con permiso de los autores. ](fig/EVfold3.jpg){#fig:EVfold2}

La siguiente figura muestra el diagrama de flujo completo del método [EVfold](http://EVfold.org), que ha sido posteriormente adaptado para proteínas transmembrana [@Hopf2012] y también para complejos cuaternarios [@Hopf2014]:

![ [Figura](#fig:EVfold3}). Algoritmo de plegamiento de proteínas en base a observaciones de mutaciones correlacionadas, que se transforman en predicciones de contactos, tomado de [@Marks2012]. Copyright (2012) Nature Biotechnology. ](fig/EVfold21.jpg){#fig:EVfold3}

La siguiente figura muestra los resultados de un experimento de validación de EVfold:

![ [Figura](#fig:EVfold4}). Calidad de las mejores predicciones de EVfold en un conjunto de 15 proteínas con diferentes composiciones de estructuras secundaria. Entre paréntesis se muestran el número de residuos del dominio modelado y el número de residuos sobre los que se calculó el RMSD entre el modelo y la estructura experimental. Figura tomada de [@Marks2011] y reproducida con permiso de los autores. ](fig/EVfoldbenchA.png){#fig:EVfold4}

Esta familia de métodos se está desarrollando todavía y sigue habiendo avances importantes [@Buchan2017]. El más notable es que el uso de secuencias metagenómicas permite ampliar el universo de secuencias lo suficiente para mejorar las predicciones de contactos (usando por ejemplo [GREMLIN](http://gremlin.bakerlab.org/submit.php)) y obtener así estructuras, de momento bacterianas, de numerosos plegamientos desconocidos [@Ovchinnikov2017]. Además, @Ovchinnikov2017 proponen una función para estimar la calidad de los modelos si hay suficientes secuencias para abordar este tipo de modelado:

$$N_{f} = \frac{clusters_{nr80}}{\sqrt L}$$

En esta función el numerador representa el total de clusters de secuencias homólogas no redundantes al 80% encontradas con [HHblits](https://toolkit.tuebingen.mpg.de/#/tools/hhblits) y el numerador es la longitud de la secuencia problema. Cuando $N_{f} > 64$ se obtienen modelos de buena calidad.

Para poner en práctica estos algoritmos se puede realizar el siguiente ejercicio:

-   Visita [UniProt](http://www.uniprot.org/), elige una proteína y extrae su secuencia S.

-   Busca secuencias similares a S y guárdalas en un archivo.

-   Calcula un alineamiento múltiple A que incluya a S con sus homólogos, elimina las secuencias muy cortas y guarda el resultado en un fichero FASTA.

-   Con ayuda de los [métodos suplementarios](https://doi.org/10.1371/journal.pone.0028766.s017) de [@Marks2011] modifica el código [fuente: prog3.4.pl](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog3.4.pl) para calcular el peso de las secuencias en base a su identidad y sumar pseudoconteos y de esa manera calcular con mayor precisión MI en tu alineamiento A. Hay también código fuente disponible en [GitHub](https://github.com/debbiemarkslab/EVcouplings).

-   Construye un modelo 3D para S.

-   Edita el archivo PDB del modelo y marca algunas parejas de residuos con valores altos de MI. Para ello puedes usar la columna del factor B, dejando a '00.00' el resto de residuos.

-   Visualiza el modelo editado y discute los resultados obtenidos.

<a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog3.4.pl" style="color: black; text-decoration: underline;">[fuente: prog3.4.pl]</a>

Mutaciones puntuales de proteínas {#pointmut}
---------------------------------

Un problema que se presenta con cada vez mayor frecuencia desde que llegaron las tecnologías de ultrasecuenciación es el de estimar el fenotipo molecular de un polimorfismo genético, por ejemplo un SNP que cambia la secuencia de aminoácidos de una proteína al provocar una sustitución no sinónima (*missense*). Esto es necesario porque hay muchos más genotipos que fenotipos observados, y porque cuánto más se secuencia se hace patente que los individuos de una especie son portadores de múltiples mutaciones de diferente naturaleza [@Peterson2013].

Esto se relaciona con los resultados de @Chothia1986, presentados en la sección [1.3.5](#threedeecons){reference-type="ref" reference="threedeecons"}, que observaron que los efectos de las mutaciones sobre la estructura (y por tanto la función) dependen en parte de dónde se produzcan. No tiene el mismo efecto cambiar un aminoácido enterrado que uno en un *loop*, o uno que coevoluciona con otro de un lazo vecino. Del mismo modo, una sustitución en el interior de una hélice no se puede comparar con la eliminación de un residuo catalítico [@Berrondo2011] o de otro clave para interaccionar con otras proteínas [@deJuan2013]. El muestreo a gran escala de @Rocklin2017 estudió la estabilidad de miles de miniproteínas (hasta 50aa) sintéticas y unas 500 naturales del PDB nos ha proporcionado los mejores datos hasta la fecha. En esencia lo que hacen es medir la estabilidad de miles de secuencias de aminoácidos expresándolas y exponiéndolas a proteasas en levadura. De esa manera estiman el efecto que tienen mutaciones individuales dependiendo de su contexto de estructura secundaria, ya sea una alfa-hélice, una lámina beta o un lazo o loop:

![ [Figura](#fig:miniprotstab}). Efecto sobre la estabilidad de mutaciones en diferentes contextos estructurales. Los valores negativos, como los de la prolina en general, son desestabilizadores. Adaptada de @Rocklin2017. Copyright (2017) Science. ](fig/stabilityTable.jpg){#fig:miniprotstab}

![ [Figura](#fig:ppiinterface}). Grafo de la interfaz entre una histona-deacetilasa (en rojo) y tres parejas distintas. Figura tomada de @Cukuroglu2014 y reproducida con permiso de los autores. ](fig/ppi_interface.png){#fig:ppiinterface}

Como se muestra en la figura [5.17](#fig:SNPpredictors){reference-type="ref" reference="fig:SNPpredictors"}, hay una gran variedad de métodos para la inferencia del fenotipo molecular de mutaciones puntuales en proteínas, y solamente algunos usan información estructural. Probablemente el más universal de todos sea SIFT [@Kumar2009], que usa como evidencia la historia evolutiva de cada familia de proteínas, que integra entre otras cosas determinantes estructurales siempre y cuando haya suficientes secuencias homólogas conocidas [@Saunders2002]. Sin embargo, como ocurre a menudo en biología computacional, no es sencillo averiguar a partir de un análisis de la literatura qué métodos son mejores. Hay que probarlos y escoger, y entre los disponibles haya cada vez más alternativas que hacen un uso explícito de información estructural, en concreto del contexto del residuo sustituido, como PolyPhen-2 [@Adzhubei2010], SusPect [@Yates2014] o mCSM [@Pires2014].

![ [Figura](#fig:SNPpredictors}). Clasificación de métodos de inferencia de fenotipos de mutaciones no sinónimas en base a los tipos de datos que emplean. Figura tomada de @Peterson2013 y reproducida con permiso. ](fig/SNPpredictors.png){#fig:SNPpredictors}

![ [Figura](#fig:SNPperformance}). Comparación del rendimiento de SusPect prediciendo mutaciones humanas deletéreas frente a otros predictores. Figura tomada de [@Yates2014] y reproducida con permiso. ](fig/SNP_performance.jpg){#fig:SNPperformance}

Para explorar la predicción de fenotipos de mutaciones no sinónimas planteo este ejercicio:

-   Visita una base de datos de mutantes, como [OMIM](http://www.omim.org), y elige una proteína P (ejemplo: OPCML).

-   Obtén la secuencia silvestre de aminoácidos S y al menos otra M con una mutación deletérea.

-   Construye un modelo comparativo de M y S.

-   Haz predicciones de fenotipo para S y M con ayuda, por ejemplo, de: [SIFT](https://sift.bii.a-star.edu.sg/), [PolyPhen-2](http://genetics.bwh.harvard.edu/pph2/) y [SusPect](http://www.sbg.bio.ic.ac.uk/~suspect).

-   Compara las predicciones obtenidas e interprétalas a la luz de las estructuras modeladas. Qué limitaciones del modelado comparativo afloran?

Estructura cuaternaria {#s4}
======================

Interfaces moleculares
----------------------

El mismo tipo de análisis que hicieron @Chothia1986 sobre la relación entre la conservación de secuencia y estructura en las proteı́nas, resumido en la figura [1.28](#fig:chothialesk){reference-type="ref" reference="fig:chothialesk"}, se ha aplicado posteriormente al estudio de las interfaces moleculares. Por ejemplo, [@Aloy2002a] las interfaces moleculares. Por ejemplo, [@Aloy2002a] analizaron la conservación de las interfaces entre proteı́nas; otros trabajos se han centrado en las interfaces proteína-DNA, encontrando tendencias análogas [@ContrerasMoreira2006]. Estamos ya en los dominios de la estructura cuaternaria (ver sección [1.3.3](#estr34){reference-type="ref" reference="estr34"}), donde unas moléculas interaccionan con otras para llevar a cabo funciones importantes en el contexto celular. Dado que las proteı́nas comparten espacios celulares seguramente su estado habitual es en complejo con otras moléculas. Al darse estas interacciones se forman interfaces tan relevantes como las de reconocimiento de ligandos por parte de receptores, en el caso de las imunoglobulinas por ejemplo, o de secuencias reguladoras por parte de factores de transcripción.

![ [Figura](#fig:prot2protI}). Interfaz entre dos proteı́nas que forman un heterodímero y conservación de secuencia de los que establecen contactos. Figura tomada de @Aloy2002a. Copyright (2002) National Academy of Sciences. ](fig/prot2prot_interface.jpg){#fig:prot2protI}

![ [Figura](#fig:prot2protcons}). Relación entre la conservación de secuencia y estructura en las interfaces entre proteı́nas. Figura tomada de @Aloy2003 y reproducida con permiso de los autores. ](fig/simint.jpg){#fig:prot2protcons}

![ [Figura](#fig:protdnacons}). Relación entre la conservación de secuencia y estructura en las interfaces entre proteı́nas (P) y ácidos nucleicos (N). Figura tomada de @ContrerasMoreira2006 y reproducida con permiso de los autores. ](fig/protDNA_interface_cons.png){#fig:protdnacons}

Estas observaciones pueden resumirse en esta generalización: proteínas con secuencias parecidas suelen tener interfaces similares cuando forman complejos. Los algoritmos que vamos a ver a continuación, que se justifican (al menos en parte) por estas observaciones, se han aplicado para el diseño de proteínas y sus interfaces, puesto que muchas de sus funciones conocidas dependen de interacciones con otras moléculas. Su diagrama de flujo genérico podría ser éste:

![ [Figura](#fig:design}). Protocolo genérico de diseño de proteínas. ](fig/design.png){#fig:design}

De todas maneras hay que ser conscientes de que no deja de ser una simplificación centrarse solamente en la interfaz, pues sabemos que a veces los cambios en zonas lejanas de la proteína son más importantes para su función biológica, por ejemplo entre factores de transcripción parálogos [@Hudson2016].

Optimización de cadenas laterales en interfaces {#scwrl}
-----------------------------------------------

En ocasiones podemos asumir que el esqueleto peptídico de una proteína no va a variar mucho al cambiar su secuencia, en particular cuando la similitud global de secuencia es alta. Si se cumple esta condición es posible tratar de optimizar una secuencia de aminoácidos con el fin de modificar su estabilidad, su actividad enzimática o su especificidad. Por ejemplo, en este artı́culo de @Reina2002, en este artı́culo de @Reina2002, los autores rediseñan una proteı́na para cambiar su afinidad por un ligando. En este caso, el algoritmo de diseño se basa en sustituir(mutar) de manera exhaustiva ciertas posiciones de la secuencia, por medio de una biblioteca de rotámeros, que son posteriormente evaluadas.

![ [Figura](#fig:JMJD2A}). Fotogramas de simulaciones de dinámica molecular (ver sección [2.6.2](#DM){reference-type="ref" reference="DM"}) mostrando los rotámeros de residuos de la histona demetilasa JMJD2A involucrados en el reconocimiento de péptidos H3K4me3 (A), H4K20me3 (B), H4K20me2 (C) y H3K9me3 (D). Figura tomada de @Ozboyaci2011 y reproducida con permiso de los autores. ](fig/JMJD2A-H3K3me3.png){#fig:JMJD2A}

Para entender en mayor detalle este experimento podemos aprender a utilizar el programa [SCWRL](http://dunbrack.fccc.edu/lab/scwrl) [@Bower1997] (en inglés se pronuncia algo ası́ como 'ardilla') que calcula las conformaciones de cadenas laterales (rotámeros) de una proteı́na dada la geometría local (en concreto los ángulos $\phi$ y $\psi$) del esqueleto y las conformaciones de los residuos vecinos. SCWRL explora una biblioteca de cadenas laterales precompiladas, extraı́das del Protein Data Bank.

-   Identifica y descarga las estructuras PDB utilizadas en el artı́culo de @Reina2002, cuál de ellas incluye las coordenadas de un péptido? Selecciona ésa.

-   Mediante SCWRL calcula los rotámeros más adecuados para el péptido y compáralos con los de las coordenadas experimentales obtenidas del PDB. Observas diferencias importantes?

-   Con SCWRL muta el péptido ligando usando algunas de las secuencias del artı́culo (opción `-s`).

-   Para cada péptido mutante calcula con SCWRL los rotámeros más adecuados de los residuos del dominio [PDZ](http://pfam.xfam.org/family/PF00595) que lo reconoce. Ves qué residuos han cambiado de rotámero?

Puede parecer razonable asumir que la geometría del esqueleto de la proteı́na se ve poco afectada al sustituir de manera aleatoria rotámeros. Sin embargo, hay estudios que observan que al muestrear cadenas laterales de aminoácidos se producen pequeños cambios conformacionales locales, que se pueden reproducir usando el algoritmo de *backrub* de @Davis2006.

Modelando nucleótidos dentro de una doble hélice de DNA {#modelnt}
-------------------------------------------------------

Al igual que con SCWRL es posible explorar los rotámeros de ciertas posiciones de una estructura proteica (ver [6.2](#scwrl){reference-type="ref" reference="scwrl"}), con el siguiente código, parte del algoritmo DNAPROT de @Espinosa2008, podemos sustituir bases nitrogenadas a lo largo de una doble hélice de DNA en formato PDB, importando el módulo [bases](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/bases.py) y descargando las coordenadas cristalográficas de la proteína dnaA ([PDB 1J1V](http://www.rcsb.org/pdb/explore.do?structureId=1j1v)):

![ [Figura](#fig:nucleotides}). Nomenclatura y numeración de los nucleótidos y sus átomos, tal como se emplea en el formato PDB, tomada de [Wikipedia](http://en.wikipedia.org/wiki/Nucleotide) y reproducida con permiso. ](fig/nucleotides.png){#fig:nucleotides}

<a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog4.1.py" style="color: black; text-decoration: underline;">[fuente: prog4.1.py]</a>

Para este tipo de manipulaciones moleculares de ácidos nucleicos es muy recomendable el software [3DNA](http://x3dna.org), que puedes descargar o usar desde una interfaz web [@Lu2008].

Interacciones no covalentes: puentes de hidrógeno en la interfaz {#Hbonds}
----------------------------------------------------------------

El estudio experimental y teórico de las interacciones entre proteínas ([*protein-protein interactions*](http://en.wikipedia.org/wiki/Protein-protein_interaction)) sembró el interés por entender los mecanismos que explicaban la especificidad de su reconocimiento. Obviamente éste es un proceso termodinámico complejo, donde se conjugan [afinidades](http://en.wikipedia.org/wiki/Chemical_affinity) y especificidades, pero en muchas ocasiones los protagonistas son los puentes de hidrógeno de la interfaz, que naturalmente dependen de la secuencia o estructura primaria, puesto que no todos los aminoácidos pueden actuar como donadores o aceptores [@Kortemme2003].

![ [Figura](#fig:Hbondgeo}). Geometría ideal de un puente de hidrógeno, donde A es el grupo aceptor, D el donador, AA es el grupo antecedente a A y H es el hidrógeno. Figura de @McDonald1994 reproducida con permiso de los autores. ](fig/Hbondgeo.png){#fig:Hbondgeo}

En las secciones anteriores hemos probado algoritmos para muestrear, por un lado, rotámeros de cadenas laterales de aminoácidos y, por otro, bases nitrogenadas de nucleótidos, bajo la misma premisa de que la geometría del esqueleto peptídico y de la doble hélice de DNA va a variar muy poco al sustituir un número pequeño de cadenas laterales y bases nitrogenadas. En esta sección vamos un paso más allá, puesto que además de muestrear es necesario evaluar la especificidad del reconocimiento de las interfaces modeladas, por ejemplo estimando la formación de puentes de hidrógeno.

![ [Figura](#fig:dnaA}). La proteína [dnaA](http://floresta.eead.csic.es/3dpwm/complexes/1j1v_A.html) en complejo con ADN. Figura tomada de [@Fujikawa2003]. Copyright (2003) Nucleic Acids Research. ](fig/dnaA.jpg){#fig:dnaA}

El punto de partida para presentar este algoritmo es la estructura del complejo de dnaA y su sitio operador, tras añadir con [Open Babel](http://openbabel.org/wiki/Main_Page) los átomos de hidrógeno que puedan faltar de un fichero en formato PDB (ver [*script*](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/add_hydrogens.py)). Por ejemplo, partiendo del complejo capturado en el archivo [PDB 1J1V](http://www.rcsb.org/pdb/explore.do?structureId=1j1v), que ya usamos en el apartado [6.3](#modelnt){reference-type="ref" reference="modelnt"}, obtenemos [1j1v\_withH.pdb](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/1j1v_withH.pdb). Una vez realizado este paso preliminar, por medio del siguiente código podemos identificar los puentes de la interfaz proteína-DNA, como haríamos con el programa [HBPLUS](http://www.ebi.ac.uk/thornton-srv/software/HBPLUS) [@McDonald1994]: <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog4.2.py" style="color: black; text-decoration: underline;">[fuente: prog4.2.py]</a>

Interfaces entre proteína, DNA y RNA: endonucleasas CRISPR-Cas guiadas por RNA {#CRISPR}
------------------------------------------------------------------------------

A veces no necesitamos modelar una interfaz molecular, pero sí comprenderla, para diseñar experimentos. Esto ocurre con las endonucleasas [CRISPR-Cas](http://wwwuser.cnb.csic.es/~montoliu/CRISPR), herramientas de edición genómica en principio más sencillas de emplear que las proteínas TALEN o las endonucleasas fusionadas con dominios Zinc Finger (ZFN).

![ [Figura](#fig:ZFNTALEN}). Dominios Zinc Finger (ZF, izq) y transcription activator-like effector (TALEN, dcha) fusionados con endonucleasas FokI. En ambos casos se muestran en cajas los nucleotidos reconocidos por cada dominio. Mientras cada ZF reconoce en general 3 bases, cada TALEN reconoce solamente una. Figura de [@Gaj2013] reproducida con permiso. ](fig/ZFNTALEN.jpg){#fig:ZFNTALEN}

Estos sistemas se han usado, por ejemplo, para inducir mutaciones heredables en loci seleccionados de plantas, incluso en especies poliploides como el trigo panadero [@Wang2014; @Lawrenson2015]. Para ello es preciso hacer análisis de secuencias con el fin de elegir las secuencias adecuadas, normalmente únicas en el genoma. En el caso de las endonucleasas Cas [@Stella2017], polipéptidos de más de 1000 aminoácidos, las secuencias diana deben elegirse respetando la arquitectura de la interfaz entre proteína, DNA y RNA, que requiere un motivo de entre 3 y 5b adyacente a la diana, llamado PAM (*protospacer adjacent motif*). Además de la estructura de estos complejos, normalmente es necesario determinar experimentalmente *in vitro* e *in vivo* la tasa de cortes no deseados o qué partes del RNA guía (sgRNA) son más sensibles en la hibridación [@Cisse2012; @Zheng2017]. Se han empleado asimismo modelos de dinámica molecular para estudiar la mecánica de estos complejos [@Zheng2017w].

![ [Figura](#fig:Cas}). Estructura del complejo Cas9-sgRNA-dsDNA. A) Dominios de Cas9 de Streptococcus pyogenes. B) Esquema del complejo sgRNA-DNAdiana. La hebra DNA diana se muestra en azul oscuro, la secuencia PAM se subraya, y sgRNA se muestra en naranja. Los sitios de corte no se muestran, ver @Stella2017. C,D) Estructuras del complejo ternario. Figura de [@Jiang2016] reproducida con permiso. ](fig/Cas9.jpg){#fig:Cas}

Modelando interfaces moleculares por homología {#dockhom}
----------------------------------------------

Podemos aprovechar las observaciones de las figuras [6.2](#fig:prot2protcons){reference-type="ref" reference="fig:prot2protcons"} y [6.3](#fig:protdnacons){reference-type="ref" reference="fig:protdnacons"} para estudiar u optimizar una interfaz molecular en base a la estructura de otras moléculas similares.

Hay muchas herramientas disponibles para modelar interfaces entre proteínas, desde herramientas sencillas como [InterPreTS](http://www.russelllab.org/cgi-bin/tools/interprets.pl) o [PPI3D](http://bioinformatics.ibt.lt/ppi3d), que no cambian la geometría de la estructura molde usada como punto de apoyo, a protocolos más complejos que ajustan el acoplamiento por *docking*. Hay también herramientas especializadas en el estudio de interfaces en el contexto de enfermedades asociadas a mutaciones ([InteractomeINSIDER](http://interactomeinsider.yulab.org)) o en el diseño de anticuerpos [@Lapidoth2015; @Baran2017].

En este apartado combinamos algunas de las herramientas empleadas en otras secciones para estudiar, por ejemplo, tres diferentes [factores sigma70](http://en.wikipedia.org/wiki/Sigma_factor) de la bacteria *Rhizobium etli CFN42*, como son [SigA](http://www.uniprot.org/uniprot/Q2K619), [rpoH1](http://www.uniprot.org/uniprot/Q2K4Y1) y [rpoH2](http://www.uniprot.org/uniprot/Q2K316). De ninguna de ellas conocemos actualmente su estructura en complejo con ADN, pero sí sabemos que SigA reconoce con cierta especificidad el consenso `CTTGACN[16-23]TATNNT`, como se explica en detalle en este trabajo de [@RamirezRomero2006], donde entre otras cosas también estiman la estabilidad de las regiones promotoras, como vimos en la sección [3.1](#dna1){reference-type="ref" reference="dna1"}.

Para seleccionar estructuras molde que nos sirvan para construir modelos podemos, como vimos en la sección [5.3](#CM){reference-type="ref" reference="CM"}, buscar directamente en el [PDB](https://www.rcsb.org/pdb). Sin embargo, en este caso iremos más rápido si consultamos el repositorio [3D-footprint](https://floresta.eead.csic.es/3dfootprint) [@ContrerasMoreira2010], que contiene solamente el conjunto actualizado de complejos proteína-DNA. Si pegamos en el motor de búsqueda de 3D-footprint las secuencias de estas 3 proteínas nos encontramos con que el complejo [1rio\_H](http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html) parece ser el mejor molde en todos los casos, ya que [3iyd\_F](http://floresta.eead.csic.es/3dfootprint/complexes/3iyd_F.html) es un complejo resuelto por microscopía con muy poca resolución:

<table border="0" cellspacing="10">
<tbody><tr><th>factor</th><th>logo</th><th>E-value</th><th>\%IID</th><th>\%Isim</th><th>\%Icover</th><th>organism</th><th>complex</th></tr>
<tr><td>SigA:</td><td>
<img src="http://floresta.eead.csic.es/3dfootprint/pics/1rio_H_trimmedPWM_50_logo.png" height="50" alt="cTTGACT"></td><td>4e-23</td><td>100</td><td>100.0</td><td>100</td><td style="font-size: 70%" align="center">THERMUS AQUATICUS</td><td><a href="http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html" title="Sigma3_and_sigma4_domains_of_RNA_polymerase_sigma_factors;">1rio_H</a>:STRUCTURE OF BACTERIOPHAGE LAMBDA C...</td></tr>
</tbody></table>

<pre>
><a href="http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html">1rio_H</a>:Sigma3_and_sigma4_domains_of_RNA_polymerase_sigma_factors;
           title=STRUCTURE OF BACTERIOPHAGE LAMBDA CI-NTD IN COMPLEX WITH SIGMA-REGION4 OF THERMUS AQUATICUS BOUND TO
           DNA organism=THERMUS AQUATICUS | interface=43,44,45,46,48,49

  Expect = 4e-23, Identities = 34/59 (57%)
  <b>Interface:</b> identity = 6/6 (100%) , similarity = 6.0/6 (100%) , coverage = 6/6 (100%)

Query: 614 ETTTRVLASLTPREERVLRMRFGIGMNTDHTLEEVGQQFSVTRERIRQIEAKALRKLKH 672
           E   + L+ L+ RE  VL++R G+    +HTLEEVG  F VTRERIRQIE KALRKLK+
Sbjct: 2   EELEKALSKLSEREAMVLKLRKGLIDGREHTLEEVGAYFGV<font color="red"><b><u>T</u></b></font><font color="red"><b><u>R</u></b></font><font color="red"><b><u>E</u></b></font><font color="red"><b><u>R</u></b></font>I<font color="red"><b><u>R</u></b></font><font color="red"><b><u>Q</u></b></font>IENKALRKLKY 60
</pre>

<table border="0" cellspacing="10">
<tbody>
<tr><td>rpoH1:</td><td><img src="http://floresta.eead.csic.es/3dfootprint/pics/1rio_H_trimmedPWM_50_logo.png" height="50" alt="cTTGACT"></td><td>3e-17</td><td>83</td><td>87.5</td><td>100</td><td style="font-size: 70%;" align="center">THERMUS AQUATICUS</td><td><a href="http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html" title="Sigma3_and_sigma4_domains_of_RNA_polymerase_sigma_factors;">1rio_H</a>:STRUCTURE OF BACTERIOPHAGE LAMBDA C...</td></tr>
</tbody></table>
<pre>
><a href="http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html">1rio_H</a>:Sigma3_and_sigma4...

  Expect = 3e-17, Identities = 24/56 (42%)
  <b>Interface:</b> identity = 5/6 (83%) , similarity = 5.2/6 (88%) , coverage = 6/6 (100%)

Query: 228 LAKAMSVLNERERRIFEARRLAED--PVTLEDLSAEFDISRERVRQIEVRAFEKVQ 281
           L KA+S L+ERE  + + R+   D    TLE++ A F ++RER+RQIE +A  K++
Sbjct: 4   LEKALSKLSEREAMVLKLRKGLIDGREHTLEEVGAYFGV<font color="red"><b><u>T</u></b></font><font color="red"><b><u>R</u></b></font><font color="red"><b><u>E</u></b></font><font color="red"><b><u>R</u></b></font>I<font color="red"><b><u>R</u></b></font><font color="red"><b><u>Q</u></b></font>IENKALRKLK 59
</pre>

<table border="0" cellspacing="10">
<tbody>
<tr><td>rpoH2:</td><td><img src="http://floresta.eead.csic.es/3dfootprint/pics/1rio_H_trimmedPWM_50_logo.png" height="50" alt="cTTGACT"></td><td>2e-18</td><td>67</td><td>77.5</td><td>100</td><td style="font-size: 70%;" align="center">THERMUS AQUATICUS</td><td><a href="http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html" title="Sigma3_and_sigma4_domains_of_RNA_polymerase_sigma_factors;">1rio_H</a>:STRUCTURE OF BACTERIOPHAGE LAMBDA C...</td></tr>
</tbody></table>
<pre>
><a href="http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html">1rio_H</a>:Sigma3_and_sigma4...

  Expect = 2e-18, Identities = 26/56 (46%)
  <b>Interface:</b> identity = 4/6 (67%) , similarity = 4.7/6 (78%) , coverage = 6/6 (100%)

Query: 220 LASALKHLNEREMKIISARRLAEDGA--TLEELGADLGISKERVRQIESRAMEKLR 273
           L  AL  L+ERE  ++  R+   DG   TLEE+GA  G+++ER+RQIE++A+ KL+
Sbjct: 4   LEKALSKLSEREAMVLKLRKGLIDGREHTLEEVGAYFGV<font color="red"><b><u>T</u></b></font><font color="red"><b><u>R</u></b></font><font color="red"><b><u>E</u></b></font><font color="red"><b><u>R</u></b></font>I<font color="red"><b><u>R</u></b></font><font color="red"><b><u>Q</u></b></font>IENKALRKLK 59
</pre>
Asimismo podemos observar que el logo de [1rio\_H](http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html) se corresponde bastante bien con la caja -35 descrita en el artículo de [@RamirezRomero2006]:

`cTTGACT`\
`||||||+`\
`CTTGACN`\

lo cual no es sorprendente dado que SigA tiene un conjunto de residuos de interfaz, aquellos que contactan con las bases nitrogenadas, conservado respecto al de [1rio\_H](http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html). Sin embargo, no ocurre lo mismo con rpoH1 y rpoH2, que presentan mutaciones en la interfaz.

El ejercicio de esta sección consiste en:

-   Construir modelos por homología de [rpoH1](http://www.uniprot.org/uniprot/Q2K4Y1) y [rpoH2](http://www.uniprot.org/uniprot/Q2K316), en presencia de la molécula de ADN de [1rio\_H](http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html). Puedes probar MODELLER, como avanzamos en la sección [5.3](#CM){reference-type="ref" reference="CM"}, siguiendo el [tutorial avanzado](http://salilab.org/modeller/tutorial/advanced.html), que contiene una parte sobre *Modeling ligands in the binding site*, la herramienta web [TFmodeller](http://www.ccg.unam.mx/tfmodeller/), o cualquier método que se te ocurra, pero es esencial que el modelo contenga las coordenadas de ADN del molde.

-   Escribir un programa, que puede aprovechar código de otras secciones de este curso, para analizar las interfaces moleculares de los modelos rpoH1 y rpoH2, con el fin de elucidar si se conservan las interacciones no covalentes de reconocimiento de bases nitrogenadas.

-   Si cambiase alguna de las interacciones, qué posiciones del consenso de [1rio\_H](http://floresta.eead.csic.es/3dfootprint/complexes/1rio_H.html) esperas que cambien?

Modelando interfaces moleculares mediante docking
-------------------------------------------------

En la sección [6.6](#dockhom){reference-type="ref" reference="dockhom"} aprovechábamos las coordenadas de un complejo molecular conocido para aproximar la interfaz de una secuencia homóloga. Cuando no disponemos de estructuras de referencia, el estudio de las conformaciones que adoptan las macromoléculas cuando interaccionan de forma transitoria es aun más difícil, con costes computacionales poco asumibles. La razón de esto es que hay muchos grados de libertad y un gran número de átomos del sistema pueden moverse. Por tanto, los algoritmos de [*docking*](http://en.wikipedia.org/wiki/Macromolecular_docking) suelen emplear estrategias para ahorrar recursos, como por ejemplo el uso de transformadas de Fourier en vez del empleo explícito de matrices de rotación y traslación [@Katchalski1992].

Un subproblema específico es el acoplamiento entre una enzima y su sustrato, una tarea para la que la información genómica (operones) puede ser muy valiosa [@Zhao2013].

Además de bancos de pruebas publicados por algunos desarrolladores [@Yu2016], desde el año 2001 hay en marcha un experimento colectivo ([CAPRI](https://www.ebi.ac.uk/pdbe/complex-pred/capri)) donde regularmente se ponen a prueba los diferentes algoritmos existentes para predecir, antes de su publicación, las poses de complejos proteicos cuyas estructuras se han resuelto experimentalmente (normalmente por cristalografía).

La lista de programas de acoplamiento molecular o *docking* es muy amplia, por lo que puede ser buena idea consultar los resultados recientes de CAPRI para seleccionar el software adecuado para nuestras necesidades. Un problema añadido es que en mi experiencia éstos son programas hechos por definición para usuarios avanzados, que requieren de cierta experiencia sobre todo a la hora de interpretar los resultados.

![ [Figura](#fig:docking}). Algunas predicciones de dímeros en CAPRI. Se muestran superposiciones de complejos predichos (azul) y resueltos experimentalmente por rayos X (rojo y naranja). En verde se destaca una cadena lateral que se reorienta al formarse el complejo. Figura tomada de <https://boinc.bakerlab.org/rosetta/rah/rah_docking.php>. ](fig/docking3.gif){#fig:docking}

Una buena manera de empezar a jugar con software de *docking* puede ser instalando el software [PyRosetta](http://pyrosetta.org) [@Chaudhury2010]. Este software nos permite hacer, de forma programática, una simulación *docking* en miniatura, en este caso entre un dúplex de ADN y el factor de transcripción DnaA , algo que puede plantearse simultáneamente como un problema clásico de *docking* y como un problema de especificidad de reconocimiento: <a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog4.3.py" style="color: black; text-decoration: underline;">[fuente: prog4.3.py]</a>

Como resultado de las simulaciones de *docking* tendremos una serie de complejos, que pueden o no mostrar interfaces relevantes en términos biológicos, dependiendo de la profundidad del muestreo realizado y el análisis posterior de los resultados, que obviamente requiere de cierta experiencia y sobre todo conocimiento de las moléculas implicadas. En concreto en el ejemplo 4.3, posiblemente como consecuencia del limitado muestreo (N=10), ninguna de las interfaces resultantes de mis simulaciones [docking\_output.tgz](https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/files/docking_output.tgz) consigue reconstruir la interfaz descrita experimentalmente:

![ [Figura](#fig:dnaAintf}). Esquema del reconocimiento específico de ADN en la interfaz de DnaA ([PDB 1J1V](http://www.rcsb.org/pdb/explore.do?structureId=1j1v)), tomado del repositorio [3D-footprint](http://floresta.eead.csic.es/3dfootprint/complexes/1j1v_A.html). ](fig/1j1v_A_interface_thumb.png){#fig:dnaAintf}

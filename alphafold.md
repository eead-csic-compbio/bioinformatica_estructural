AlphaFold y la revolución del aprendizaje automático {#alphafoldAA}
===================================================================

Las metodologías descritas en los capítulos anteriores son el resultado de décadas de trabajo de la comunidad científica.
A hombros de estos gigantes, y aprovechando el enorme número de secuencias (~10E8) y estructuras (~10E5) conocidas en la actualidad, 
se han ido publicando desde 2020 herramientas basadas en el 
[aprendizaje automático](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico) 
(AU, _machine learning_ (ML) en inglés) 
que han permitido dar un salto cualitativo en la predicción de la estructura de las proteínas. 
La más famosa de todas es [AlphaFold](https://alphafold.ebi.ac.uk) (AF), pero hay muchas otras, y las que vendrán. 
Vayamos por partes.


La revolución del aprendizaje automático {#AA}
----------------------------------------------

El experimento bianual CASP, del que ya hablamos en la sección de [Fold recognition](#FRsection), 
ha permitido medir de manera objetiva el impacto del AA en la predicción estructural.
En las siguientes figuras se puede ver el salto que supuso la aparición de AlphaFold y otros métodos de AA:

![ [Figura](#fig:CASPAU). Calidad de los mejores modelos evaluados en CASP a lo largo de los años usando la métrica GDT_TS [@Zemla2002]. Los evaluadores de CASP13 achacaron la mejoría a que algunos de los mejores algoritmos fueron capaces de estimar distancias entre aminoácidos a partir de información evolutiva implícita en alineamientos múltiples de secuencia muy profundos [@Abriata2019]. Figura tomada de <https://www.sib.swiss/about/news/10307-deep-learning-a-leap-forward-for-protein-structure-prediction>. ](fig/CASPProgression.png){#fig:CASPAU}

![ [Figura](#fig:CASPAF). Calidad de los mejores modelos evaluados en CASP hasta la participación del predictor AlphaFold2 (AF2). Figura tomada de [@Callaway2020]. Puedes leer más detalles en el [blog](https://bioinfoperl.blogspot.com/2020/11/alphafold-resuelve-plegamiento-proteinas.html).](fig/casp_history.png){#fig:CASPAF}

Es evidente que los nuevos métodos de AA han aumentado de manera significativa nuestra capacidad de predecir la estructura de las proteínas. Como decía al principio de este capítulo, los investigadores de la compañia DeepMind han avanzado a hombros de gigantes y han tenido a su disposición enormes recursos de cálculo. Pero ojo, aunque el algoritmo AF haga predicciones de alta calidad en muchos casos, esto no significa que sepamos simular el proceso de plagamiento de proteínas todavía.


Cómo funciona AlphaFold2 {#alphafold}
-------------------------------------

Las redes neuronales se han estado aplicando en nuestro campo desde hace décadas para la predicción de [estructura secundaria](#protSS) o para predecir [contactos entre aminoácidos](#contactosPred) de proteínas plegadas. En ambas aplicaciones aprovechamos que para muchas familias de proteínas conocemos tantas secuencias diferentes que podemos usar esa información evolutia para inferir qué partes de la estructura plegada se tocan entre sí y por tanto restringen el espacio de mutaciones. 

AF2 usa el mismo tipo de información de partida, la secuencia de aminoácidos problema P y un alineamiento múltiple de P con otras secuencias no redundantes de proteínas homólogas, pero va más allá por que en vez de predecir contactos extrae información estructural más concreta cómo distancias y ángulos. Su sistema comprende varios módulos que se ejecutan secuencialmente y realizan las siguientes tareas:

 * Extración de correlaciones evolutivas entre residuos de una proteína a partir de perfiles de secuencias homólogas obtenidas con PSIBLAST o HHblits con el algoritmo CCMpred [@Seemayer2014], similar a otros presentados en la sección [5.5](#contactosPred).
 
 * Predicción de información estructural con redes neuronales [profundas](https://bioinfoperl.blogspot.com/2020/04/redes-neuronales-profundas.html), con al menos dos variantes:
 
   + Predicción de distancias reales entre C-$beta$, no contactos, a partir de histogramas precalculados en el rango de 2 a 22 Ansgtrom, inspirado en [RaptorX](https://en.wikipedia.org/wiki/RaptorX). Las distancias estimadas les permiten asignar estructura secundaria con una precisión Q3 del 84% usando datos de CASP11.
  
   + Predicción de ángulos diedros $phi$ y $psi$ (ver sección [1.3.2](#SS)).

 * Diferenciación del potencial de distancias/ángulos por métodos de minimización de gradientes con la secuencia entera.
 
 * Relajación del esqueleto obtenido con el campo de fuerzas AMBER (ver sección [2.6](#DM)), seguido de modelado de cadenas laterales completas con Rosetta, aunque esto no mejore el modelo de manera significativa.
 
 
En resumen, el modelo AF2 consta de 4 etapas, resumidas en la figura siguiente:

 * Secuencia problema P /**input sequence** en formato FASTA.
 
 * Búsqueda de bases de datos. 
 
   + Para cada P se construye un alineamiento múltiple (MSA) con las secuencias similares encontradas en colecciones como [Mgnify](https://www.ebi.ac.uk/metagenomics/) , UniRef90 y [UniClust30](https://uniclust.mmseqs.com).
   
   + Además se hace una búsqueda de estructuras molde / **template** que se pueden usar como punto de partida para los modelos.
   
 * Predicción de 5 modelos con el mismo **input** y cinco redes profundas entrenadas de manera independiente.
 
 * Relajación y evaluación de los modelos.

![ [Figura](#fig:AFflow). Arquitectura del modelo AlphaFold2 (AF2), donde se describe que los datos de partida se representan de dos formas  complementarias: alineamiento múltiple de secuencias (MSA) y parejas de residuos correlacionados. Estas dos representaciones sirven de entrada para dos tipos de redes profundas diferentes. La red Evoformer hace inferencia directa de relaciones espaciales y evolutivas usando mecanismos de atención [@DotCSV2021] y triángulos entre residuos. A continuación el módulo estructural sirve para modelar en 3D de manera explícita por medio de matrices de rotación y traslación cada aminoácido. Las flechas muestran el flujo de información y las dimensiones de las matrices se dan como $s$ (número de secuencias), $r$ (número de residuos) y $c$ (número de canales). El proceso se repite tres veces para ir refinando/reciclando las predicciones y producir los modelos finales. Figura tomada de [@Jumper2021]. El proceso se explica en detalle en un vídeo creado por los autores de AF2 [@Tunyasuvunakool2022].](fig/AF2flow.png){#fig:AFflow} 

 
### Métricas de calidad de AlphaFold2 (AF2) {#AFmetrics}

Los modelos 3D producidos por AF2 se ordenan por su puntuación pLDDT (*predicted Local Distance Difference Test*).
Es una predicción por residuo de la función lDDT-C$alpha$, una medida de confianza para cada residuo basada en el porcentaje de distancias interatómicas que caen dentro de valores esperados. Por tanto es una medida que informa de la calidad local.

Como se muestra eb la siguiente figura, toma valores de 0 a 100 que se guardan como factores B en los modelos generados en formato PDB. Los valores [70-90] se interpretan como de alta confianza y los mayores de 90 de muy alta confianza. Valores por debajo de 50 se consideran propios de estructuras desordenadas, como pasa frecuentemente en los extremos de los  polipéptidos.

![ [Figura](#fig:pLDDT). Ejemplos de pLDDT de modelos AF2. El esquema de arriba muestra una proteínas con varios dominios. La gráfica de abajo muestra los valores en un dominio solo. Figura adaptada de [@Tunyasuvunakool2022] .](fig/pLDDT.png){#fig:pLDDT} 

Otra medida independiente de la calidad de un modelo AF2 es PAE (*Predicted Aligned Error*), que se mide en Angstrom.
Esta métrica mide el error de las posiciones de los residuos de un modelo si se pudiera superponer con la estructura experimental. Se usa sobre todo para evaluar las posiciones de los diferentes dominios de una proteína multidominio.
 

Evaluación de calidad de las predicciones de AlphaFold2 (AF2) {#AFQC}
---------------------------------------------------------------------

Entre las **fortalezas** de AF2 destaca su notable precisión promedio de 1.5 Å de RMSD para todos los átomos modelados, no sólo carbonos $\alpha$, tanto en CASP14 como en un conjunto de 3144 estructuras recientemente publicadas en el Protein Data Bank tras descartar las estructuras conocidas con identidad de secuencia > 40%. Además, AF2 es capaz de estimar bien la calidad los modelos que genera:

![ [Figura](#fig:AF2bench). Banco de pruebas de AF2 sobre un conjunto de 3144 estructuras del PDB: a) RMSD del esqueleto peptídico modelado comparado con la estructura experimental. b) Correlación entre la precisión del esqueleto, calculada con la función lDDT [@Mariani2013], y la correcta elección de rotámeros de la cadenas laterales. Figura tomada de [@Jumper2021].](fig/AF2bench.png){#fig:AF2bench}

Otra fortaleza de AF2 según sus usuarios en [Twitter](https://twitter.com/sokrypton/status/1417935552905728006) es que tiene buenas prestaciones observadas para predecir estructuras cuaternarias de homómeros.

Entre las **limitaciones** destacan:

 + La calidad de las predicciones cae de manera significativa si el alineamiento múltiple de secuencias homólogas a la de interés tiene una profundidad < 30 (ver sección de [predicción de contactos](#contactosPred))

 + Las estructuras de AF2 son de menor calidad para dominios poco compactos, con pocos contactos, como los dominios puente. 
 
Además, el análisis de las 365.184 estructuras de AF2 disponibles para un total de 21 especies en UniProt [@Varadi2022; @Bordin2022], incluyendo 4 plantas (*Arabidopsis thaliana*, soja, arroz y maíz), ha permitido hacer varias **observaciones**:

 + Las especies que han ganado más anotaciones estructurales de proteínas en proporción son plantas (soja, arroz y maíz)
 
 + Tras seleccionar modelos de AF2 de buena calidad (tras eliminar los desordenados por ejemplo), el 92% se pueden asignar a superfamilias ya existentes en la clasificación de plegamientos CATH. Por tanto, hay indicios de que AF2 podría haber descubierto nuevos plegamientos. Puedes ver más detalles en el [blog](https://bioinfoperl.blogspot.com/2022/09/plantas-beneficiadas-alphafold.html).
 
 + Los modelos de AF2 enriquecen de manera significativa (36%) las conformaciones de las superfamilias de plegamientos conocidas en CATH
 
![ [Figura](#fig:AF2CATH). Crecimiento en conocimiento estructural en número de dominios (izquierda) y en proporción (derecha) para 21 especies. Figura tomada de [@Bordin2022].](fig/AF2CATH.jpg){#fig:AF2CATH}

TODO: https://www.nature.com/articles/s41594-022-00849-w



Otros algoritmos alternativos a AF {#beyondAF}
----------------------------------------------

El fenómeno que ha supuesto la llegada de AF va más allá y prueba de ello es que otros autores están publicando 
soluciones similares, lo cual nos dice mucho del potencial actual del AA en este campo. 

El principal algoritmo alternativo publicado hasta la fecha creo que es 
[RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold), descrito en detalle en [@Baek2021].
Como contamos en su día en el [blog](https://bioinfoperl.blogspot.com/2021/07/rosettafold-modelado-open-source-proteinas.html), su rendimiento es superior a los predictores clásicos pero inferior a AF2. Al igual que AF2 usa redes neuronales profundas y require de mucha potencia de cálculo.

Otra alternativa interesante es el algoritmo [RGNA2](https://github.com/aqlaboratory/rgn2), una red geométrica recurrente descrita en [@Chowdhury2022].
A diferencia de AF2 y RoseTTAFold, RGN2 no calcula alineamientos múltiples y por tanto se puede aplicar a cualquier secuencia, incluso a aquellas que llamamos huérfanas porque no tienen secuencias similares homólogas en las bases de datos.
En cambio, RGN2 es un modelo de lenguaje, derivado de los que se usan cotidianamente para procesar lenguaje natural o para completar una frase cuando escribes en tu móvil. Aunque los autores recomiendan AF2 para los casos que sí tienen homólogos,
sus resultados muestran que RGN2 supera a AF2 y RoseTTAFold en secuencias huérfanas gastando cien veces menos tiempo de cálculo.

Aplicaciones de AlphaFold2 {#AFapps}
------------------------------------

Para los que queráis probarlo hay varias opciones:

i) El contenedor Docker descrito en https://github.com/deepmind/alphafold que ojo, requiere 2.2TB de espacio si instalas todas las bases de datos. 

ii) Un cuaderno Colab con un predictor simplificado en https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb

iii) Las predicciones ya disponibles en UniProt y AlphaFold db para un total de 21 especies (https://alphafold.ebi.ac.uk/download)


https://bioinfoperl.blogspot.com/2022/06/openfold-open-source-alphafold.html




Ejercicios













<!-- relajacion de modelos AF
https://twitter.com/sokrypton/status/1585284793792602113?s=20&t=P2RSWfIRWnJOPzulsRE49Q
-->

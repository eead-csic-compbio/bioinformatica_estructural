
# Resumen {-}

La Bioinformática Estructural se ocupa del estudio de la estructura molecular de proteínas y ácidos nucleicos con el fin de reconstruir su historia evolutiva e inferir sus posibles funciones. El objetivo de este material es ayudar a comprender las diferentes estrategias y algoritmos que se utilizan habitualmente con este fin. El curso no incluye la disección formal de la eficiencia de cada algoritmo; en cambio, se apoya en validaciones empíricas publicadas en la literatura para describir los puntos fuertes y débiles de las diferentes estrategias. Solamente conociendo cómo funcionan estos algoritmos podremos elegir los más apropiados para cada problema y evaluar de manera crítica los resultados obtenidos.

Tras un breve repaso de fundamentos bioquímicos, este material presenta algunos algoritmos básicos, en su mayoria heurísticos, plantea problemas y estrategias para resolverlos. A lo largo del curso encontraréis referencias a artículos que profundizan sobre aspectos particulares de cada tema, junto con ejemplos que a veces requieren de ciertos conocimientos de programación (en Perl y Python). Los enlaces al código fuente en el texto tienen un formato distinto: 
<a href="https://github.com/eead-csic-compbio/bioinformatica_estructural/blob/master/code/prog3.1.py" style="color: black; text-decoration: underline;">[fuente: prog3.1.py]</a>

Este curso creció como material didáctico de la [Licenciatura en Ciencias Genómicas-UNAM](https://www.lcg.unam.mx) desde 2008 hasta 2019. 
En 2022 lo actualicé para añadir el capítulo de AlphaFold, que volví a actualizar en 2025 para el 
[International Master in Plant Genetics, Genomics and Breeding](http://www.masterplantbreeding.com)
organizado por [CIHEAM Zaragoza](https://www.iamz.ciheam.org). 

Agradezco a los alumnos por sus comentarios para mejorarlo, a M.Medina, J.Fernández-Recio y 
A.Pascual-García por participar en el proceso de revisión abierta por pares para Digital.CSIC en 2018, 
y a la [Fundación ARAID](http://www.araid.es) por el apoyo desde el principio.

![](fig/licenciaCC.png)

## Cómo descargar y citar este curso {-}

Puedes descargar este material en formato PDF en [Digital.CSIC](http://hdl.handle.net/10261/21892) y navegarlo en <http://eead-csic-compbio.github.io/bioinformatica_estructural>. 

Este contenido se mantiene en el repositorio 
<https://github.com/eead-csic-compbio/bioinformatica_estructural>,
que incluye código fuente dentro de la carpeta [code](https://github.com/eead-csic-compbio/bioinformatica_estructural/tree/master/code). 

Puedes citarlo como:

Contreras-Moreira B (2018) Algoritmos en bioinformática estructural. Edición 2025. [doi:10.20350/digitalcsic/8544](https://doi.org/10.20350/digitalcsic/8544)

    @book{
      Author = {Contreras-Moreira, Bruno},
      Title = {Algoritmos en bioinform\'{a}tica estructural},
      Publisher = {Digital.CSIC},
      Edition = {2025},
      Year = {2018},
      url="https://doi.org/10.20350/digitalcsic/8544",
      doi = "10.20350/digitalcsic/8544"
    }

## Recursos complementarios {-}

Si tuviese que recomendar un libro de texto como acompañamiento para este material sería posiblemente 
_[Structural Bioinformatics: An Algorithmic Approach](http://www.structuralbioinformatics.com)_. 

En español, el compendio [Bioinformática con Ñ](https://zenodo.org/communities/bioinfconn) 
tiene varios capítulos que pueden ser muy buen complemento para este material, varios de ellos citados en el texto.

En el blog de nuestro laboratorio también tratamos frecuentemente estos temas: <https://bioinfoperl.blogspot.com/>

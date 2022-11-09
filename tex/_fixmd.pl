#!/usr/bin/perl 
use strict;
use warnings;

# Fixes Pandoc-generated markdown to adapt it to Bookdown

if(!$ARGV[1]) {
  die "# usage: <raw.md> <fixed.md>\n"
}

my ($mdfile, $fixedfile) = @ARGV;
my ($text,$params);

open(RAWMD,"<",$mdfile) ||
  die "# ERROR: cannot open $mdfile\n";

open(MD,">",$fixedfile) ||
  die "# ERROR: cannot write to $fixedfile\n";

while(<RAWMD>) {

  # 1) Fix figure legends
  # ![ Estructura ... Figura tomada de <https>. []{label="fig:dna"}](fig/dna.png){#fig:dna width="100%"}
  # ![ (A) Estructura ... (PDB:... ), .... []{label="fig:MGW"}](fig/MGW.jpeg){#fig:MGW}

  if(/^!\[ ([A-Za-z\(]+).*\{(#\S+)/) {
    ($text, $params) = ($1, $2); 

    # remove unneded label
    s/\[\]\{label="\S+"\}//;

    s/^!\[ \Q$text\E/!\[ [Figura]($params). $text/;
  }

  # 2) Fix table legends
  # : Nomenclatura de los 20 aminoácidos esenciales[]{label="tab:amino"}
  if(/^\s+:\s*(\S+)/) {
    $text = $1; 

    s/^\s+:\s*$text/\*\*Tabla\*\*\. $text/; 
  }

  # 3) Fix links to internal refs
  #[\[tab:hidrof\]](#tab:hidrof){reference-type="ref" reference="tab:hidrof"}
  if(/\[\\\[([^\\]+)\\\]\]\(/) {
    s/\[\\\[/[/g;
    s/\\\]\]/]/g;
  }

  print MD $_; 

}

close(MD); 

close(RAWMD);
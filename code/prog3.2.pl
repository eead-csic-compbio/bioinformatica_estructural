#!/usr/bin/perl -w

# programa 3.2 algoritmo de alineamiento global perfil-perfil
# Bruno Contreras-Moreira

use strict;

my %AAORDER = ('A',1,'R',2,'N',3,'D',4,'C',5,'Q',6,'E',7,'G',8,'H',9,'I',10,'L',11,
		'K',12,'M',13,'F',14,'P',15,'S',16,'T',17,'W',18,'Y',19,'V',20);
my $GAPCOST = -8; # coste de un gap 
my $SSBONUS = 2;  # premio por igual estructura secundaria

## -1) archivos de entrada
my $perfil1 = './files/1ngk_A.pssm'; # perfil generado con PSI-BLAST
my $perfil2 = './files/1s69_A.pssm'; 
my $SS1     = './files/1ngk_A.psipred'; # estructura secundaria predicha con PSIPRED
my $SS2     = './files/1s69_A.psipred'; 

print "# $0 input: $perfil1 $perfil2 $SS1 $SS2 params: $GAPCOST $SSBONUS\n\n";

## 0) define variables y lee perfiles 
my ($ID,$total,$gaps,@matrix,$l1,$l2,$i,$j,$aa1,$aa2,$par) = (0,0,0);
my ($align1,$align2,$ss1,$ss2,$ruler,$gapi,$gapj,$score) = ('','','','','');

my ($seq1,@perfil1) = lee_perfil($perfil1);
my ($seq2,@perfil2) = lee_perfil($perfil2);
my @SS1 = lee_SS($SS1);
my @SS2 = lee_SS($SS2);

$l1 = length($seq1);
$l2 = length($seq2); 

## 1) define e inicia matriz de programacion dinamica
# http://es.wikipedia.org/wiki/Algoritmo_Needleman-Wunsch
for($j=0;$j<=$l1;$j++){ $matrix[0][$j]{'score'} = $j * $GAPCOST; }
for($i=0;$i<=$l2;$i++){ $matrix[$i][0]{'score'} = $i * $GAPCOST; }

## 2) rellena la matriz fila a fila
for($i=1;$i<=$l2;$i++) 
{
	for($j=1;$j<=$l1;$j++) 
	{
        	$score = evalua_par($perfil1[$j-1],$perfil2[$i-1]);
		if($SS1[$j-1] eq $SS2[$i-1] && $SS2[$i-1] ne 'C'){ $score += $SSBONUS }
		
		# calcula 3 posibles scores: diagonal y gaps
        	$par = $matrix[$i-1][$j-1]{'score'} + $score;
        	$gapi = $matrix[$i-1][$j]{'score'} + $GAPCOST;
        	$gapj = $matrix[$i][$j-1]{'score'} + $GAPCOST;
		
		($matrix[$i][$j]{'score'},$matrix[$i][$j]{'dir'}) = max($par,$gapi,$gapj);
	}
}

## 3) reconstruye alineamiento
($i,$j) = ($l2,$l1); 
$score = $matrix[$i][$j]{'score'};

while (1) 
{
    last if(!$matrix[$i][$j]{'dir'});
     
    if ($matrix[$i][$j]{'dir'} eq 'diagonal') 
    {
    	$i--; $j--;
	$aa1 = substr($seq1,$j,1);
	$aa2 = substr($seq2,$i,1);
        $align1 = $aa1 . $align1;
        $align2 = $aa2 . $align2;
	$ss1    = $SS1[$j] . $ss1;
	$ss2    = $SS2[$i] . $ss2;
	if($aa1 eq $aa2)
	{ 
		$ID++; 
		$ruler = '|' . $ruler;
	}
	else{ $ruler = ' ' . $ruler; }
	$total++;
    }
    elsif($matrix[$i][$j]{'dir'} eq 'gapj') 
    {
        $align1 = substr($seq1,$j-1,1) . $align1;
        $align2 = '-' . $align2;
	$ss1    = $SS1[$j-1] . $ss1;
	$ss2    = '-' . $ss2;
	$ruler = ' ' . $ruler;
        $j--;
    }
    else 
    {
        $align1 = '-' . $align1;
        $align2 = substr($seq2,$i-1,1) . $align2;
	$ss1    = '-' . $ss1;
	$ss2    = $SS2[$i-1] . $ss2;
	$ruler = ' ' . $ruler;
        $i--;
	$gaps++; # en secuencia1
    }   
}

print "# identical aligned residues = $ID/$total gaps = $gaps score = $score\n";
print "$perfil1\n$ss1\n$align1\n$ruler\n$align2\n$ss2\n$perfil2\n";

#####################################################

# lee fichero PSSM generado por PSI-BLAST con opcion -Q
sub lee_perfil
{
	my ($PSSMfile) = @_;
	 
	my ($secuencia,@perfil,$col,$aa,$weights) = ('');

        # 1 K   -4  2 -3 -3 -6  6  1 -5 -3 -6 -5  4 -4 -6  5 -3 -4 -6 -5 -5     
	open(PSSM,$PSSMfile) || die "# lee_perfil: no puedo leer $PSSMfile\n";
	while(<PSSM>)
	{
		if(/^\s+(\d+)\s+(\w)\s+(.+?)\n/)
		{
			($col,$aa,$weights)=($1,$2,$3); 
			$col -= 1; # cuenta desde 0
			push(@{$perfil[$col]},$aa); # posicion 0: secuencia
			push(@{$perfil[$col]},(split(/\s+/,$weights))); # pos 1..20: pesos
			$secuencia .= $aa;
		}
	}
	close(PSSM);

	return ($secuencia,@perfil);    
}
    
# evalua una pareja de aminoacidos consultando su vector de pesos/sustituciones
# usa global: %AAORDER
sub evalua_par
{
	my ($pssv1,$pssv2) = @_;
	
	my $score1 = $pssv2->[$AAORDER{$pssv1->[0]}];
	my $score2 = $pssv1->[$AAORDER{$pssv2->[0]}];
	return sprintf("%1.2f",($score1+$score2)/2);
}

# lee fichero de prediccion de estructura secundaria generado con PSIPRED
sub lee_SS
{
	my($SSfile) = @_;
	
	my (@SS);

	#Pred: CCHHHHHCCHHHHHHHHHHHHHHHHCCHHHHHHCCCCCHHHHHHHHHHHHHHHHCCCCCC
	open(PSIPRED,$SSfile) || die "# lee_SS: no puedo leer $SSfile\n";
	while(<PSIPRED>)
	{
		if(/^Pred: (\w+?)\n/){ push(@SS,(split(//,$1))); }
	}
	close(PSIPRED);

	return (@SS);    
}	

sub max
{
	my ($par,$gapi,$gapj) = @_;
	
	if($gapi>$gapj && $gapi>$par){ return($gapi,'gapi'); }
	elsif($gapj >= $par && $gapj >= $gapi){ return($gapj,'gapj'); }
	else{ return($par,'diagonal'); }
}            		

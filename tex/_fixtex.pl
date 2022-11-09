#!/usr/bin/perl 
use strict;
use warnings;

# Fixes original LATEX files so that they can be converted to Markdown

my $figpath = 'fig/';
my $figfullpath = "../$figpath";
my $oldfigpath = "../$figpath/old/";
my $repourl = 'https://github.com/eead-csic-compbio/bioinformatica_estructural';
my $codeurl = "$repourl/blob/master/code";
my $filesurl = "$codeurl/files";

#ls fig/ | perl -lne 'if(/\.(\S+)$/){ print $1}' | sort -u
my @figexts = qw(
  png
  jpg
  jpeg
  gif
  cdr
  dia
  pptx
);

if(!$ARGV[1]) {
  die "# usage: <raw.tex> <fixed.tex>\n"
}

my ($texfile, $fixedfile) = @ARGV;


## 1) parse and edit the original LATEX content
open(TEX,"<",$texfile) ||
  die "# ERROR: cannot read $texfile\n";

open(FIXTEX,">",$fixedfile) ||
  die "# ERROR: cannot create $fixedfile\n";

my ($ext, $params, $file, $fullfile);
my ($URL, $text, $edtext);

while(<TEX>) {

  # 1.1) fix figures, sources in fig/
  # \includegraphics[width=0.8\textwidth]{flujoinfo}
  if(/%\\includegraphics/) {

  } elsif(/includegraphics\[(.*?)\]\{(\S+)\}/) {

    ($params, $file) = ($1, $2);
    $fullfile = '';

    # get figure extension
    for $ext (@figexts) {
      if(-s "$figfullpath$file.$ext") {
        if($fullfile) {
          `mv $figfullpath$file.$ext $oldfigpath`
	} else {
          $fullfile = "$file.$ext";
	}
      }
    }

    if($fullfile) {
      s/includegraphics\[(.*?)\]\{(\S+)\}/includegraphics[$params]{$figpath$fullfile}/g;
    } else {
      print "# cannot find $_\n";
    } 

  } elsif(/includegraphics\{(\S+)\}/) {

    $file = $1;
    $fullfile = '';

    for $ext (@figexts) {
      if(-s "$figfullpath$file.$ext") {
	if($fullfile) {
          `mv $figfullpath$file.$ext $oldfigpath`
        } else {
          $fullfile = "$file.$ext";
        }
      }
    }

    if($fullfile) {
      s/includegraphics\{(\S+)\}/includegraphics{$figpath$fullfile}/g;
    } else {
      print "# cannot find $_";
    }

  } elsif(/%\\htmladdnormallink/) {
    print FIXTEX $_;
  } 
  
  if(/\\caption/) {
	  #$
  }

  if(/htmladdnormallink/) { 
    # 1.2) pandoc does not like \htmladdnormallink

    while(/htmladdnormallink\{(.+)?\}\{([^\}]+)/g) {
      ($text, $URL) = ($1, $2);

      if($URL =~ /\.\/files\/(.+)/) {
        # change local paths to URLs
	$file = $1;
        s/htmladdnormallink\{\Q$text\E\}\{\Q$URL\E\}/href{$filesurl\/$file}{$text}/;

      } elsif($URL =~ /\.\/code\/(.+)/) {
	# change local paths to URLs      
	$file = $1;
        s/htmladdnormallink\{\Q$text\E\}\{\Q$URL\E\}/href{$codeurl\/$file}{$text}/;

      } elsif($text =~ /http/) {
	# simple URLS      
        s/htmladdnormallink\{\Q$text\E\}\{\Q$URL\E\}/url{$URL}/;

      } else {
	# URLs with target text
        s/htmladdnormallink\{\Q$text\E\}\{\Q$URL\E\}/href{$URL}{$text}/
      }
    }
  } 
  
  if(/\\verbatiminput/) {
    # 1.3) pandoc does not like \verbatiminput, add placeholder
    s/^\\verbatiminput/verbatiminput/;
  } 
 
  if(/(ref)\{fig:([^\}]+)\}/ || /(label)\{fig:([^\}]+)\}/) {
    # 1.4) pandoc does not like internal refs with_
    ($ext, $text) = ($1, $2);
    $edtext = $text;
    $edtext =~ s/_//g; 
    s/$ext\{fig:$text\}/$ext\{fig:$edtext\}/;
  }

  if(/\\italics/) {
    # 1.5) pandoc does not like \italics

    while(/\\italics\{([^\}]+)}/g) {

      $text = $1;
      s/\\italics\{\Q$text\E\}/\\emph{$text}/;
    }
  } 

  # 1.6) copy unchanged and edited lines
  print FIXTEX $_;
}

close(FIXTEX);

close(TEX);


#!/usr/bin/perl 
use strict;
use warnings;
use File::Temp qw/ tempfile /;

my $pandocEXE = 'pandoc';

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
  die "# usage: <file.tex> <file.md>\n"
}

my ($texfile, $mdfile) = @ARGV;




## 1) parse and edit the original LATEX content,
##    creates temp file
open(TEX,"<",$texfile) ||
  die "# ERROR: cannot read $texfile\n";

my ($tmpfh, $tmpfilename) = tempfile( 'texXXXXXXXX', UNLINK => 1 );

my ($ext, $params, $file, $fullfile, $URL, $text);

while(<TEX>) {

  # 1.1) fix figures, sources in fig/
  # \includegraphics[width=0.8\textwidth]{flujoinfo}
  if(/%\\includegraphics/) {
    print $tmpfh $_;

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
      print $tmpfh $_;
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
      print $tmpfh $_;
    } else {
      print "# cannot find $_";
    }

  } elsif(/%\\htmladdnormallink/) {
    print $tmpfh $_;

  } elsif(/htmladdnormallink/) { 
    # 1.2) pandoc does not like \htmladdnormallink

    while(/htmladdnormallink\{(.+)?\}\{(.+)?\}/g) {
      ($text, $URL) = ($1, $2); #print ">$URL $_";

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

    print $tmpfh $_;

  } elsif(/\\verbatiminput/) {
    # 1.3) pandoc does not like \verbatiminput, add placeholder

    s/^\\verbatiminput/verbatiminput/;
    print $tmpfh $_;

  } elsif(/\\italics/) {
    # 1.4) pandoc does not like \italics

    while(/\\italics\{([^\}]+)}/g) {

      $text = $1;
      s/\\italics\{\Q$text\E\}/\\emph{$text}/;
    }

    print $tmpfh $_;

  } else {

    # 1.5) copy all other lines unchanged
    print $tmpfh $_;
  }
}

close($tmpfh);

close(TEX);

## 2) convert LATEX to markdown
print "$pandocEXE -f latex -t markdown --verbose -s $tmpfilename -o $mdfile\n";
system("$pandocEXE -f latex -t markdown --verbose -s $tmpfilename -o $mdfile");

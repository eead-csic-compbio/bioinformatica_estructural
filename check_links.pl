use strict;
use warnings;
use LWP::UserAgent;
my $agent = LWP::UserAgent->new();

while(my $file = <*.md>) {
  print "## $file\n";
  open(MD,$file);
  while(<MD>) {
    if(/\[[^\]+]\]\((\S+)\)/ || /<(\S+)>/) {
      my $link = $1;
      $link =~ s/\\//g;
      printf("%s %s\n",$agent->head($link)->message(),$link) if($agent->head($link)->message() ne 'OK');
    }
  }
}


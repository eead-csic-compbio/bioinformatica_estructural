use strict;
use warnings;
use LWP::UserAgent;
my $agent = LWP::UserAgent->new();

while(my $file = <*.tex>) 
{
    print "## $file\n";
	open(TEX,$file);
	while(<TEX>)
	{
		if(/htmladdnormallink\{.*?\}\{(\S+)?\}/)
		{
			next if(/%.*?htmladdnormallink/);

			my $link = $1;
			$link =~ s/\\//g;
			printf("%s %s\n",$agent->head($link)->message(),$link) if($agent->head($link)->message() ne 'OK');
		}
	}
}


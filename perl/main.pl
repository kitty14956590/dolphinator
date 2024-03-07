#!/usr/bin/perl -w

use strict;
use Getopt::Std;
use Encode;
binmode(STDOUT, ":encoding(UTF-8)");

my %options=();
getopts("e:?d:?n", \%options);

sub rgb_prints {
	my $red = $_[0];
	my $green = $_[1];
	my $blue = $_[2];
	my $string = $_[3];
	print(sprintf("\033[38;2;%d;%d;%dm%s\033[38;2;255;255;255m", $red, $green, $blue, $string));
}

if (!$options{n}) {
	rgb_prints(0,154,255,"                                   __\nhttps://dolphinonkeys.com      _.-~  )\n                    _..--~~~~,'   ,-/     _\n                 .-' . . . .'   ,-','    ,' )\n               ,' . . . _   ,--~,-'__..-'  ,'\n             ,' . . .  (@)' ---~~~~      ,'\n            / . . . . '~~             ,-'\n           / . . . . .             ,-'\n          ;  . . . .  - .        ,'\n         :  . . . .       _     /\n        .  . . . .          \\`-.:\n       .  . . ./  - .          )\n      .   . . |  _____..---.._/ __ Seal :3 _\n~---~~~~----~~~~             ~~\n\n");
}

if ($options{e}) {
	my $string = $options{e};
	# my @characters = $string =~ /.{1}/g;
	my $encoded = Encode::decode("UTF-8", $string);
	my @characters = $encoded =~ /.{1}/g;
	map {
		my $binary = sprintf("%0.16b", ord($_));
		$binary = ($binary =~ s/1/e/rg) =~ s/0/E/rg;
		rgb_prints(196,0,255, $binary);
	} @characters;
	print("\n");
} elsif ($options{d}) {
	my $string = $options{d};
	$string = ($string =~ s/e/1/rg) =~ s/E/0/rg;
	my @characters = $string =~ /.{16}/g;
	map {
		rgb_prints(196,0,255,chr(oct("0b$_")));
	} @characters;
	print("\n");
}

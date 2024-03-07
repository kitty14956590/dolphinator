#! /usr/bin/env bash

# because these functions dont exist in bash, we make them ourselves
function ord() {
	printf "%d" "'$1"
}
function chr() {
	binary=${1//e/1}
	binary=${binary//E/0}
	int="$((2#$binary))"
	printf "\U$(printf "%08x" "$int")"
}
function rgb() {
	echo -e "\033[38;2;$1;$2;$3m$4\033[38;2;255;255;255m"
}
OPTIND=1
banner=1
while getopts "e:?d:?n" opt; do # no argparse for bash :c
  case "$opt" in
    e)
      encode=$OPTARG
      ;;
    d)
      decode=$OPTARG
      ;;
    n)
      banner=0
      ;;
  esac
done
if [ $banner == 1 ]
then
	rgb 0 154 255 "                                   __\nhttps://dolphinonkeys.com      _.-~  )\n                    _..--~~~~,'   ,-/     _\n                 .-' . . . .'   ,-','    ,' )\n               ,' . . . _   ,--~,-'__..-'  ,'\n             ,' . . .  (@)' ---~~~~      ,'\n            / . . . . '~~             ,-'\n           / . . . . .             ,-'\n          ;  . . . .  - .        ,'\n         :  . . . .       _     /\n        .  . . . .          \\\`-.:\n       .  . . ./  - .          )\n      .   . . |  _____..---.._/ __ Seal :3 _\n~---~~~~----~~~~             ~~\n\n"
fi
if [ "$encode" != "" ]; then
	string=$encode
	binary=""
	for (( i=0; i<${#string}; i++ )) do
		binary=$binary$(printf "%016d\n" $(echo "obase=2; $(ord "${string:$i:1}")"|bc)) # is bc a bash command?, I think?
	done
	binary=${binary//1/e};binary=${binary//0/E} # make this better later (maybe)
	rgb 196 0 255 "$binary"
elif [ "$decode" != "" ]; then
	let "e=0,b=0"
	string=$(chr ${decode:0:16})
	for (( i=0; i<${#decode}; i++ )) do
		if [ $e == 16 ]; then
			e=0
			string="$string$(chr ${decode:b:16})"
		fi
		let "e=$e+1,b=$b+1"
	done
	rgb 196 0 255 "$string"
fi

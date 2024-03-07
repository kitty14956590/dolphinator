#!/usr/bin/env php
<?php
// this is the banner
$show_banner = 1;
$i = 0;
foreach ($argv as $arg) {
	if (strcmp($arg, "-n") == 0) {
		array_splice($argv, $i, 1);
		$show_banner = 0;
	}
	$i++;
}
if ($show_banner) :
?>
[38;2;0;154;255m                                   __
https://dolphinonkeys.com      _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-' . . . .'   ,-','    ,' )
               ,' . . . _   ,--~,-'__..-'  ,'
             ,' . . .  (@)' ---~~~~      ,'
            / . . . . '~~             ,-'
           / . . . . .             ,-'
          ;  . . . .  - .        ,'
         :  . . . .       _     /
        .  . . . .          \`-.:
       .  . . ./  - .          )
      .   . . |  _____..---.._/ __ Seal :3 _
~---~~~~----~~~~             ~~
[38;2;255;255;255m
<?php
endif;

function rgb_print($red, $green, $blue, $text) {
	echo "\033[38;2;" . $red . ";" . $green . ";" . $blue . "m" . $text . "\033[38;2;255;255;255m";
}

if (!function_exists("mb_convert_encoding")) {
	// "mbstring is a non-default extension. This means it is not enabled by default"
	rgb_print(255, 0, 0, "php-mbstring not installed :c");
	die();
}

if ($argc < 3) {
	rgb_print(255, 0, 0, "not enough arguments :c\n");
	die();
}

$flag = $argv[1];
if ($flag[0] != '-' || ($flag[1] != 'd' && $flag[1] != 'e')) {
	rgb_print(255, 0, 0, "invalid command :c\n");
	die();
}

$strings = array_slice($argv, 2);

if (strcmp($flag, "-e") == 0) {
	foreach ($strings as $arg) {
		foreach (mb_str_split($arg) as $char) {
			$value = unpack('H*', mb_convert_encoding($char, "UTF-16", "UTF-8"));
			$binary = base_convert($value[1], 16, 2);
			$padded = str_pad($binary, 16, "0", STR_PAD_LEFT);
			$dolphinscript = str_replace(["1", "0"], ["e", "E"], $padded);
			rgb_print(196, 0, 255, $dolphinscript);
		}
	}
} else {
	foreach ($strings as $arg) {
		$characters = str_split($arg, 16);
		foreach($characters as $char) {
			$binary = str_replace(["e", "E"], ["1", "0"], $char);
			$codepoint = bindec($binary);
			$utf8str = mb_chr($codepoint, "UTF-8");
			rgb_print(196, 0, 255, $utf8str);
		}
	}
}
echo "\n";
?>

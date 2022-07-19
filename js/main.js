#!/bin/env node
const { ArgumentParser } = require('argparse')
function rgb(red,green,blue,text) {
	// I don't like this but it said I cant have octal escape in format stirng
	return "\033[38;2;" + red + ";" + green + ";" + blue + "m" + text + "\033[38;2;255;255;255m"
}
function iterate_thingy(thinger,funct) {
	var i = -1
	while (i++ != thinger.length -1) {
		funct(i)
	}
}
const parser = new ArgumentParser({ description: 'Dolphinspeak encode/decoder :3' })
group = parser.add_mutually_exclusive_group(required=true)
group.add_argument("-e","--encode", {type: "str", help: 'encode string into dolphin speak'})
group.add_argument("-d","--decode", {type: "str", help: "decode dolphin speak into string"})
parser.add_argument("-n","--no-banner", {help:"removes the banner :c", action:'store_true'})
let args = parser.parse_args()
if(!args.no_banner) {
	console.log(rgb(0,154,255,"                                   __\nhttps://dolphinonkeys.com      _.-~  )\n                    _..--~~~~,'   ,-/     _\n                 .-' . . . .'   ,-','    ,' )\n               ,' . . . _   ,--~,-'__..-'  ,'\n             ,' . . .  (@)' ---~~~~      ,'\n            / . . . . '~~             ,-'\n           / . . . . .             ,-'\n          ;  . . . .  - .        ,'\n         :  . . . .       _     /\n        .  . . . .          \`-.:\n       .  . . ./  - .          )\n      .   . . |  _____..---.._/ __ Seal :3 _\n~---~~~~----~~~~             ~~\n\n"))
}
try {
	if(args.encode) {
		encode = args.encode
		iterate_thingy(encode, function(i){process.stdout.write(rgb(196,0,255,encode.charCodeAt(i).toString(2).padStart(16,"0").replace(/1/g,"e").replace(/0/g,"E")))})
		console.log()
	} else if(args.decode) {
		var decode = args.decode.match(/.{1,16}/g)
		iterate_thingy(decode, function(i){process.stdout.write(rgb(196,0,255,String.fromCharCode(parseInt(decode[i].replace(/e/g,"1").replace(/E/g,"0"),2))))})
		console.log()
	} else {
		console.log(rgb(255,0,0,"invalid command :c"))
	}
} catch(err) {
	console.log(rgb(255,0,0,String(err)))
}

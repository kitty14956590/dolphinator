#! /usr/bin/env python3
import argparse
def rgb(red,green,blue,text):
	return '\033[38;2;%s;%s;%sm%s\033[38;2;255;255;255m' % (red,green,blue,text)
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e","--encode", type=str, help="encode string into dolphin speak")
group.add_argument("-d","--decode", type=str, help="decode dolphin speak into string")
parser.add_argument("-n","--no-banner", help="removes the banner :c", action='store_true')
args = parser.parse_args()
if not args.no_banner:
	print(rgb(0,154,255,"""                                   __
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
~---~~~~----~~~~             ~~\n\n"""))
try:
	if args.encode:
		print(rgb(196,0,255,''.join([bin(ord(i))[2:].zfill(16) for i in [char for char in args.encode]]).translate({48:69,49:101})))
	elif args.decode:
		replaced = args.decode.translate({69:48,101:49})
		print(rgb(196,0,255,''.join([chr(int(replaced[index:index+16],2)) for index in range(0, len(replaced), 16)])))
	else:
		print(rgb(255,0,0,"invalid command :c"))
except Exception as e:
	print(rgb(255,0,0,str(e)))

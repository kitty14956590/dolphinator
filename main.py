import sys, argparse
def rgb(red,green,blue,text):
	return '\033[38;2;%s;%s;%sm%s\033[38;2;255;255;255m' % (red,green,blue,text)
print(rgb(0,154,255,"""                                   __
https://dolphinonkeys.com      _.-~  )
                    _..--~~~~,'   ,-/      _
                 .-' . . . .'   ,-','    ,' )
               ,' . . . _   ,--~,-'__..-'  ,'
             ,' . . .  (@)' ---~~~~      ,'
            / . . . . '~~             ,-'
           / . . . . .             ,-'
          ;  . . . .  - .        ,'
         :  . . . .       _     /
        .  . . . .          \`-.:
       .  . . ./  - .          )
      .   . . |  _____..---.._/ __ Seal :3 __
~---~~~~----~~~~             ~~\n\n"""))
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e","--encode", type=str, help="translate into dolphin speak")
group.add_argument("-d","--decode", type=str, help="translate from dolphin speak")
args = parser.parse_args()
try:
	if args.encode:
		print(rgb(196,0,255,''.join(bin(ord(i))[2:].zfill(16)for i in args.decode).replace('0','E').replace('1','e')))
	elif args.decode:
		replaced = args.decode.replace("E","0").replace("e","1")
		print(rgb(196,0,255,''.join(chr(int(replaced[index:index+16],2))for index in range(0,len(replaced),16))))
	else:
		print(rgb(255,0,0,"invalid command :c"))
except Exception as e:
	print(rgb(255,0,0,str(e)))

import sys, argparse
def rgb(red,green,blue,text):
	return '\033[38;2;%s;%s;%sm%s\033[38;2;255;255;255m' % (red,green,blue,text)
print(rgb(0,154,255,"""                                  __
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
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e","--encode", type=str, help="encode string into dolphin speak")
group.add_argument("-d","--decode", type=str, help="decode dolphin speak into string")
args = parser.parse_args()
try:
	if args.encode:
		binary = []
		for charf in sys.argv[2]:
			binary.append(bin(ord(charf))[2:].zfill(16))
		print(rgb(196,0,255,''.join(binary).replace('0','E').replace('1','e')))
	elif args.decode:
		chars = []
		replaced = sys.argv[2].replace("E","0").replace("e","1")
		for index in range(0, len(replaced), 16):
			chars.append(chr(int(replaced[index:index+16],2)))
		print(rgb(196,0,255,''.join(chars)))
	else:
		print(rgb(255,0,0,"invalid command :c"))
except Exception as e:
	print(rgb(255,0,0,str(e)))

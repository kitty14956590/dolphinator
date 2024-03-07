#!/usr/bin/env python3

import glob, os, re

if os.getuid() == 0 or os.geteuid() == 0:
	os.setuid(65534)
	os.seteuid(65534)
def rgb (a,b,c,text):
	return "\033[38;2;%s;%s;%sm%s\033[38;2;255;255;255m"%(a,b,c,text)
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
for i in glob.glob("./*/main*"):
	test = ansi_escape.sub('', os.popen(i + " -e \"キティa猫咪喵ニャー\" -n 2>&1 0>&1").read()).replace("\n","")
	if test == "EEeeEEEEeEeEeeEeEEeeEEEEeeEEEeeEEEeeEEEEeEeEEEeeEEEEEEEEEeeEEEEeEeeeEEeeEEeEeEeeEeEeEeEEeEeEeEeEEeEeEeEeeEeeEeEeEEeeEEEEeeEEeEeeEEeeEEEEeeeEEEeeEEeeEEEEeeeeeeEE":
		print(rgb(0,255,0,"[*] %s passed encode test" % i[2:]))
	else:
		print(rgb(255,0,0,"[!] %s failed encode test" % i[2:]))
	test = ansi_escape.sub('', os.popen(i + " -d \"EEeeEEEEeEeEeeEeEEeeEEEEeeEEEeeEEEeeEEEEeEeEEEeeEEEEEEEEEeeEEEEeEeeeEEeeEEeEeEeeEeEeEeEEeEeEeEeEEeEeEeEeeEeeEeEeEEeeEEEEeeEEeEeeEEeeEEEEeeeEEEeeEEeeEEEEeeeeeeEE\" -n").read()).replace("\n","")
	if test == "キティa猫咪喵ニャー":
		print(rgb(0,255,0,"[*] %s passed decode test" % i[2:]))
	else:
		print(rgb(255,0,0,"[!] %s failed decode test" % i[2:]))

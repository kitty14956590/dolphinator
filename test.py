#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import glob, os, re

if os.getuid() == 0 or os.geteuid() == 0:
	os.setuid(65534)
	os.seteuid(65534)

def rgb (a,b,c,text):
	return "\033[38;2;%s;%s;%sm%s\033[38;2;255;255;255m"%(a,b,c,text)

ansi_remove = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
for i in glob.glob("./*/main*"):
	test = os.popen(i + " -e \"キティespañolлтфш1الa猫咪喵ニャーλεμόνι\" -n 2>&1 0>&1").read().lstrip().rstrip()
	test = ansi_remove.sub("", test)
	if test == "EEeeEEEEeEeEeeEeEEeeEEEEeeEEEeeEEEeeEEEEeEeEEEeeEEEEEEEEEeeEEeEeEEEEEEEEEeeeEEeeEEEEEEEEEeeeEEEEEEEEEEEEEeeEEEEeEEEEEEEEeeeeEEEeEEEEEEEEEeeEeeeeEEEEEEEEEeeEeeEEEEEEEeEEEEeeeEeeEEEEEeEEEeEEEEeEEEEEEeEEEeEEEeEEEEEEEeEEEeEEeEEEEEEEEEEEEEeeEEEeEEEEEeeEEEeEEeeeEEEEEeeEEeEEEeEEEEEEEEEEEeeEEEEeEeeeEEeeEEeEeEeeEeEeEeEEeEeEeEeEEeEeEeEeeEeeEeEeEEeeEEEEeeEEeEeeEEeeEEEEeeeEEEeeEEeeEEEEeeeeeeEEEEEEEEeeeEeeeEeeEEEEEEeeeEeeEeEeEEEEEEeeeEeeeeEEEEEEEEeeeeEEeeEEEEEEEEeeeEeeeeEeEEEEEEeeeEeeeEEe":
		print(rgb(0,255,0,"[*] %s passed encode test" % i[2:]))
	else:
		print(rgb(255,0,0,"[!] %s failed encode test" % i[2:]))
	test = os.popen(i + " -d \"EEeeEEEEeEeEeeEeEEeeEEEEeeEEEeeEEEeeEEEEeEeEEEeeEEEEEEEEEeeEEeEeEEEEEEEEEeeeEEeeEEEEEEEEEeeeEEEEEEEEEEEEEeeEEEEeEEEEEEEEeeeeEEEeEEEEEEEEEeeEeeeeEEEEEEEEEeeEeeEEEEEEEeEEEEeeeEeeEEEEEeEEEeEEEEeEEEEEEeEEEeEEEeEEEEEEEeEEEeEEeEEEEEEEEEEEEEeeEEEeEEEEEeeEEEeEEeeeEEEEEeeEEeEEEeEEEEEEEEEEEeeEEEEeEeeeEEeeEEeEeEeeEeEeEeEEeEeEeEeEEeEeEeEeeEeeEeEeEEeeEEEEeeEEeEeeEEeeEEEEeeeEEEeeEEeeEEEEeeeeeeEEEEEEEEeeeEeeeEeeEEEEEEeeeEeeEeEeEEEEEEeeeEeeeeEEEEEEEEeeeeEEeeEEEEEEEEeeeEeeeeEeEEEEEEeeeEeeeEEe\" -n").read().lstrip().rstrip()
	test = ansi_remove.sub("", test)
	if test == "キティespañolлтфш1الa猫咪喵ニャーλεμόνι":
		print(rgb(0,255,0,"[*] %s passed decode test" % i[2:]))
	else:
		print(rgb(255,0,0,"[!] %s failed decode test" % i[2:]))

#!/bin/ruby
require 'optparse'
options = {}
OptionParser.new do |opt|
  opt.on('--decode text') { |o| options[:decode] = o }
  opt.on('--encode text') { |o| options[:encode] = o }
  opt.on('--no-banner') { |o| options[:banner] = "" }
end.parse!
def rgb (a,b,c,text) 
	print("\033[38;2;%s;%s;%sm%s\033[38;2;255;255;255m"%[a,b,c,text])
end
unless options[:banner] then
	rgb(0,154,255,"                                   __\nhttps://dolphinonkeys.com      _.-~  )\n                    _..--~~~~,'   ,-/     _\n                 .-' . . . .'   ,-','    ,' )\n               ,' . . . _   ,--~,-'__..-'  ,'\n             ,' . . .  (@)' ---~~~~      ,'\n            / . . . . '~~             ,-'\n           / . . . . .             ,-'\n          ;  . . . .  - .        ,'\n         :  . . . .       _     /\n        .  . . . .          \\\`-.:\n       .  . . ./  - .          )\n      .   . . |  _____..---.._/ __ Seal :3 _\n~---~~~~----~~~~             ~~\n\n")
	puts
end
if options[:encode] then
	print("\033[38;2;196;0;255m")
	for char in options[:encode].split("") do
		print(("%016d"%char.ord().to_s(2)).tr("10","eE"))
	end
	print("\033[38;2;255;255;255m")
	puts
elsif options[:decode] then
	print("\033[38;2;196;0;255m")
	for char in options[:decode].scan(/.{1,16}/) do
		print(char.tr("eE","10").to_i(2).chr("UTF-8"))
	end
	print("\033[38;2;255;255;255m")
	puts
end

#!/usr/bin/python
from os import popen
xprop=popen("xprop -root").read()
def grepvalue(needle, haystack, seplen=0):
	return[x[1][x[1].find(needle)+len(needle)+seplen:]for x in list(enumerate(haystack.split("\n")))if needle in x[1]][0]
print(' '.join(["^fg(#A6E22E)"+x[1]+"^fg()"if x[0] else x[1]for x in[(int(grepvalue("_NET_CURRENT_DESKTOP(CARDINAL)",xprop,3))==x[0],x[1])for x in enumerate([x.strip("\"")for x in grepvalue("_NET_DESKTOP_NAMES(UTF8_STRING)",xprop,3).split(", ")])]]))

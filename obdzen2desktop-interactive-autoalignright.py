#!/usr/bin/python
#This script provides a desktop switcher menu in dzen2, it is agnostic to desktop names and number and it automatically aligns itself to the rightmost side of the screen.
#Executes in 0.04 seconds on my machine.
#Only one step configuration!
a=6 #Width of one character of the font this will render in.
#You do however, need to set keybinds such that meta + n switches to desktop n, if you want the interactive element.
from os import popen
xprop=popen("xprop -root").read()
def grepvalue(needle, haystack, seplen=0):
	return[x[1][x[1].find(needle)+len(needle)+seplen:]for x in list(enumerate(haystack.split("\n")))if needle in x[1]][0]
msg= ":: "+' '.join(["^ca(1,xdotool key super+{})".format(x[0]+1)+("^bg(#43443C)"+x[1][1]+"^bg()"if x[1][0] else x[1][1])+"^ca()"for x in enumerate([(int(grepvalue("_NET_CURRENT_DESKTOP(CARDINAL)",xprop,3))==x[0],x[1])for x in enumerate([x.strip("\"")for x in grepvalue("_NET_DESKTOP_NAMES(UTF8_STRING)",xprop,3).split(", ")])])])
print("^pa(%s)"%(int(grepvalue("_NET_WORKAREA(CARDINAL)",xprop,3).split(",")[2])-(len(''.join([m for m in [x.split("^")[0] for x in msg.split(")")] if not m=='']))*6))+msg)
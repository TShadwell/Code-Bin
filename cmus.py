#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import popen
out = ""
cmus = popen("cmus-remote -Q").read()
def bf(needle):
	return not cmus.find(needle) == -1
def genbar(enders, bar, empty, length, ratio):
	bl = round((length -2) / ratio)
	return enders[0] + bar * bl + (length-2-bl) * empty + enders[1]
#Get info
if bf("cmus is not running"):
	out = "Nothing playing"
else:
	out += ""
	#assemble dictionary
	data = []
	for q in [x.split("tag ")[1] for x in cmus.split("\n") if not x.find("tag ") ==-1]:
		n = q.find(" ")
		data.append((q[0:n],q[n+1:len(q)]))
	data = dict(data)
	duration = int(cmus.split("\n")[2].split("duration ")[1])
	position = int(cmus.split("\n")[3].split("position ")[1])
	if (position == 0):
		position = 1
	if(bf("status stopped")):
		out += "Nothing selected"
	elif bf("status playing"):
		out += " %s - %s %s" % (data['artist'], data['title'], genbar("[]","="," ",6,int(duration)/int(position)))
	elif bf("status paused"):
		out += " %s - %s %s" % (data['artist'], data['title'], genbar("[]","="," ",6,int(duration)/int(position)))
print (out.encode("UTF-8").decode())




















#Old dictionary assembler left here to laugh at
##tags = dict([(x.split("tag ")[1][0:(x.split("tag ")[1].find(" "))],x.split("tag ")[1][(x.split("tag ")[1].find(" ")):len(x.split("tag ")[1])]) for x in cmus.split("\n") if not x.find("tag ") ==-1])
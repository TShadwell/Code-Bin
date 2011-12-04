#!/usr/bin/env python
#####################
icon_dir = "/home/thomas/Documents/dzen/dzen_bitmaps"
dzen_height = 20
bar_width = 50
artist_colour = "#ffffff"#87ff00
title_colour = ""
foreground_colour = "#ffffff"#87ff00
background_colour = "#ffffff"
#####################
from os import popen
out = ""
cmus = popen("cmus-remote -Q").read()
def colour(hexcode = ""):
	return "^fg(" +hexcode + ")"
def icon(iconname, filename=".xbm", direc=icon_dir) :
	return "^i(" + direc+ "/" + iconname + filename + ")"
def bf(needle):
	return needle in cmus
def genbar(bcurrent, bmax=100, width=bar_width, height=((2/4)*dzen_height) + 2, foreground=foreground_colour, background=background_colour):
	return popen("echo \"%s %s\" | gdbar -h %s -w %s -fg %s -bg %s -s o -nonl" %  (round(bcurrent), round(bmax), height, width, "\\" + foreground,"\\" + background)).read()

#Get info

if bf("not running"):
	out = "Nothing playing"
else:
	out += icon("music")
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
		out += icon("stop")
	elif bf("status playing"):
		out += ""
		if data['title'].find(data['artist']) == 0:
			out += "  %s %s" % (genbar(position, duration),colour(title_colour) + data['title'])
		else:
			out += " %s %s - %s" % (genbar(position, duration), colour(artist_colour) + data['artist']+ colour(),  colour(title_colour) + data['title'] +colour())
	elif bf("status paused"):
		out += ""
		if data['title'].find(data['artist']) == 0:
			out += "  %s %s" % (genbar(position, duration), colour(title_colour) + data['title'] + colour())
		else:
			out += " %s %s - %s" % (genbar(position, duration), colour(artist_colour) + data['artist'] + colour(), colour(title_colour) + data['title'] + colour())
print (out)




















#Old dictionary assembler left here to laugh at
##tags = dict([(x.split("tag ")[1][0:(x.split("tag ")[1].find(" "))],x.split("tag ")[1][(x.split("tag ")[1].find(" ")):len(x.split("tag ")[1])]) for x in cmus.split("\n") if not x.find("tag ") ==-1])

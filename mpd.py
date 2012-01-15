builder = False
progressbar = True
if progressbar:
	class pbar:
		fgc="b5b5b5"
		bgc="575757"
volumemaster = True
volumebarmaster = True
if volumebarmaster:
	class vbarm:
		fgc="a6e22e"
		bgc="575757"
volumebar = False
if volumebar:
	class vbar:
		fgc="b5b5b5"
		bgc="575757"
icons = True
if icons:
	icondir = "/home/thomas/Documents/dzen/dzen-xbm-pack"
	icons = ["mpd.xbm", "volhi.xbm"]
from os import popen
from string import Template
#MPD widget for dzen2
#What we need.
Inputs = ["artist", "album", "title"]
#Pass this to MPC- we're not going to do the hard work!
MPCo = popen ("mpc -f " + ",N0P3,".join(["%{0}%".format(var) for var in Inputs])).read().split("\n")
canShowInfo  = not(len(MPCo) == 2) #Nothing queued
#Construct a dictionary of the info we need.
if canShowInfo:
	info = dict(list(zip(Inputs, MPCo[0].split(",N0P3,")))+ [tuple([(value == " on") if value == " on" or value == " off" else value for value in a.split(":")]) for a in MPCo[2].split("   ")] + [("elapsed", MPCo[1].split("(")[-1].rstrip(")"))])
	if progressbar:
		info["progressbar"] = popen("echo {} | gdbar -w 75 -h 6 -fg \#{} -bg \#{} -nonl".format(info["elapsed"].rstrip("%"), pbar.fgc, pbar.bgc)).read().strip("\n")
else:
	info = {}
if volumebar:
	info["volumebar"] = popen("echo {} | gdbar -h 16 -ss 1 -sw 9 -sh 1 -s v -fg \#{} -bg \#{} ".format(info["volume"].rstrip("%"), vbar.fgc, vbar.bgc)).read().strip("\n")
if volumemaster:
	info["volumemaster"] = popen("amixer get Master").read().split("\n")[-2].split("[")[1].split("]")[0]
	if volumebarmaster:
			info["volumebarmaster"] = popen("echo {} | gdbar -h 16 -ss 1 -sw 4 -sh 3 -s v -fg \#{} -bg \#{} ".format(info["volumemaster"].rstrip("%"), vbarm.fgc, vbarm.bgc)).read().strip("\n")
if icons:
	for icon in icons:
		info["".join(icon.split(".")[:-1]) + "icon"] = "^i(" + icondir + "/" + icon + ")"
if builder:
	print("You can use these in the template!\n\t" + ', '.join(["$%s"% value for value in info]) + "\nCurrent output:")

#Hint- if you don't want to separate a symbol and a word with a space, use ^r(0x0), or more glitchily, use " \b" as the separator.
#It's a bit of a hack, but it works!
main = "$volumebarmaster" 
ifmusic ="$mpdicon^fg(#FFFFFF)$artist^fg() ^r(9x1) $title $progressbar" \
if canShowInfo else \
"^ca(1,urxvt -e ncmpcpp)$mpdicon^r(0x0)Nothing Playing^ca()"
#Ok, fun is over.
a = Template(main+ifmusic)
print(a.substitute(info))
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
volumebar = True
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
	info = dict(list(zip(Inputs, MPCo[0].split(",N0P3,")))+ [tuple([(value == " on") if value == " on" or value == " off" else value for value in a.split(":")]) for a in MPCo[-2].split("   ")] + [("elapsed", MPCo[1].split("(")[-1].rstrip(")"))])
	if progressbar:
		info["progressbar"] = popen("echo {} | gdbar -ss 1 -sw 3 -w {} -h 1 -fg \#{} -bg \#{} -nonl".format(info["elapsed"].rstrip("%"), (len(info["artist"] + info["title"] + "  ")*6) + 7, pbar.fgc, pbar.bgc)).read().strip("\n")
else:
	info = {}
if volumebar and canShowInfo:
	info["volumebar"] = popen("echo {} | gdbar -h 16 -ss 1 -sw 4 -sh 1 -s v -fg \#{} -bg \#{} ".format(info["volume"].rstrip("%"), vbar.fgc, vbar.bgc)).read().strip("\n")
if volumemaster:
	info["volumemaster"] = popen("amixer get Master").read().split("\n")[-2].split("[")[1].split("]")[0]
	if volumebarmaster:
			info["volumebarmaster"] = popen("echo {} | gdbar -h 16 -ss 1 -sw 4 -sh 1 -s v -fg \#{} -bg \#{} ".format(info["volumemaster"].rstrip("%"), vbarm.fgc, vbarm.bgc)).read().strip("\n")
if icons:
	for icon in icons:
		info["".join(icon.split(".")[:-1]) + "icon"] = "^i(" + icondir + "/" + icon + ")"
if builder:
	print("You can use these in the template!\n\t" + ', '.join(["$%s"% value for value in info]) + "\nCurrent output:")

#Hint- if you don't want to separate a symbol and a word with a space, use ^r(0x0), or more glitchily, use " \b" as the separator.
#It's a bit of a hack, but it works!
main = "^p(_TOP)Vol.^p()^p(-25)^pa(;9)^ib(1)alsa^ib(0)^p() $volumebarmaster" + ("^fg(#282828)^r(1x16)^fg()$volumebar ^pa(;8)mpd^p()"if canShowInfo else '')
ifmusic =" ^fg(#a8b0a8)^r(2x16)^fg()^fg(#a6e22e)$mpdicon^fg()^p(_TOP)^fg(#FFFFFF)$artist^fg() ^p(;5)^r(9x1)^p(_TOP)$title^p()^ib(1)^p(-" + str((len(info["artist"] + info["title"] + "  ")*6) + 6) + ";9)$progressbar^ib(0)^p()" \
if canShowInfo else \
" ^fg(#a8b0a8)^r(2x16)^fg()^fg(#282828)^r(3x1)^fg()^ca(1,urxvt -e ncmpcpp)$mpdicon^r(0x0)None^ca()"
#Ok, fun is over.
a = Template(main+ifmusic)
print(a.substitute(info))
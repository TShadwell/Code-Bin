#Unfinished!
#!/usr/bin/python
#Python Window Manager for dzen2, requires xprop.
#Settings
char_width = 6
screen_width= 1024
#
from os import popen
from math import floor

def xpropdict(CommandSwitches):
	a = popen("xprop " + CommandSwitches).read().split("\n")
	dicti = {}
	for i in range(len(a)):
		if a[i] == "":
			pass
		elif ("	") in a[i]:
			pass
		elif (" = " in a[i]):
			k, b = a[i].split(" = ")
			if ", " in b:
				b = [d.strip("\"") for d in b.split(", ")]
			dicti[k] = b
		elif (a[i][-1] == ":"):
			lsChildren =[]
			for line in a[i+1:]:
				if line.find("	") == False:
					lsChildren.append(line.strip("	"))
				else:
					break
				dicti[a[i][:1]] = [tuple(h[1].split(": ")) if len(h[1].split(": "))>1 else (h[0]) for h in enumerate(lsChildren)]
		elif (": " in a[i]):
			k= a[i].split(": ")[0]
			if "#" in a[i]:
				b=a[i].split("# ")[1]
			else:
				b=a[i].split(": ")[1]
			if ", " in b:
				b = [d.strip("\"") for d in b.split(", ")]
			dicti[k] = b


	return dicti
root = xpropdict("-root")
desks = dict(enumerate(root["_NET_DESKTOP_NAMES(UTF8_STRING)"]))
desktops={}
for desktop in root["_NET_DESKTOP_NAMES(UTF8_STRING)"]:
	desktops[desktop] = []
desktops[None]=[]
for process in root["_NET_CLIENT_LIST_STACKING(WINDOW)"]:
	m = xpropdict("-id %s"%process)
	desktops[desks[int(m["_NET_WM_DESKTOP(CARDINAL)"])] if int(m["_NET_WM_DESKTOP(CARDINAL)"]) in desks else None].append(m)
out =""
l=""
for n, desk in desks.items():
	l += desk + " "
out+= desks[int(root["_NET_SHOWING_DESKTOP(CARDINAL)"])] + " "

dn_l = floor(\
(screen_width - len(l)*char_width) /\
(len(desks[int(root["_NET_SHOWING_DESKTOP(CARDINAL)"])])))


for window in desktops[desks[int(root["_NET_SHOWING_DESKTOP(CARDINAL)"])]]:
	out += (str(window["_NET_WM_VISIBLE_NAME(UTF8_STRING)"]).strip("\""))[:dn_l] + " | "

print(out)






		


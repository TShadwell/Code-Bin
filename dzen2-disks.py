from os import popen
nicknames = {"":"d1", "windows": "^fg(#282828)^r(1x16)^fg()", "data": "d2"}
o = ""
def formup(line):
	percentage = ""
	for i in reversed(list(range(line.index("%")))):
		if line[i] == " ":
			break
		percentage += line[i]
	a= line.split("/")[-1]
	return nicknames[a] + popen("echo {} | gdbar -h 16 -ss 1 -sw 4 -sh 1 -s v -fg \#a6e22e -bg \#575757".format(''.join(list(reversed(percentage))))).read().strip("\n") if a in nicknames else ""
print(''.join([formup(line) for line in popen("df").read().split("\n")[2:-1]]))

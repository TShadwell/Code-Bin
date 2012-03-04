from urllib.request import urlopen
name="Thomas"
a=str(urlopen("http://c3l6.org/honours/combinedhonoursboard").read())
print(name+" is %s in the world, currently."%((lambda n:str(n)+(["th","st","nd","rd"][int(str(n)[-1])]if n<4 else"th"))(a[:a.find(name)].count("</tr>")-1)))
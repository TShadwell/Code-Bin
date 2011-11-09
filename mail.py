#Conky Gmail notification python script- brings up notify-osd with subjects of e-mails too.
#CHANGE THESE:
##############
#USERNAME#####
username = ""###
#PASSWORD#####
password = ""###
##############
##############
#FOR SIMPLE USE,
#IGNORE FURTHER ON.






from imaplib import IMAP4_SSL
from os import system
obj = IMAP4_SSL('imap.gmail.com','993')
obj.login(username,password)
obj.select()
length = len(obj.search(None, 'UnSeen')[1][0].split())
if length > 0:
	#Only do this if we have messages, I can imagine this would be CPU intensive otherwise.
	msgs = []
	typ, unread_ids = obj.search(None, 'UnSeen')
	unreads = unread_ids[0].decode("utf-8").split(" ")
	print(" " +str(length) + " unread!")
	for ids in unreads:
		typ, msg_data = obj.fetch(ids, "(BODY.PEEK[HEADER.FIELDS (SUBJECT)])")
		msgs.append(msg_data)
	system("notify-send " + "\"" + str(length) + " unread mails!\" \"" + ", ".join([x[0][1].decode("utf-8")[9:-4] for x in msgs]) + "\""+ ".")
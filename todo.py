#!/usr/bin/env python
#Short program to get todo list from taskwarrior
from os import popen 
print(" ".join([x.split(" ")[-1] for x in popen("task next").read().split("\n")[3:-3]]))

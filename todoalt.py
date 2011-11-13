#!/usr/bin/env python
#(Very) short Python script to construct a todo list (or any kind of list) from Taskwarrior (task).
from os import popen
a = [x.split(" ")[-1] for x in popen("task next").read().split("\n")[3:-3]]
b = [x.split(" ")[-1] for x in popen("task active").read().split("\n")[3:-3]]
print((("Todo: "  + ", ".join(a) + ".") * (len(a)>0) + (" Active: "  + ", ".join(b) + ".") * (len(b)>0)).replace("-"," "))

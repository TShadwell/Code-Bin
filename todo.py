#!/usr/bin/env python
#(Very) short Python script to construct a todo list (or any kind of list) from Taskwarrior (task).
from os import popen 
print(", ".join([x.split(" ")[-1] for x in popen("task next").read().split("\n")[3:-3]]) + ".")

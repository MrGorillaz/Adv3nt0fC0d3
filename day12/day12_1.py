import numpy as np
file = open("day12_demo1.txt","r")

values = file.readlines()
file.close()

groups = {}

for line in range(len(values)):
    values[line] = values[line].strip()
    group = values[line].split(" ")

    groups["line_"+str(line)] = { "group":group[0], "damage_list":group[1].split(",")}







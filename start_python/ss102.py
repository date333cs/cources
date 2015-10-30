#!/usr/bin/python
import sys
 
y_vec = []
 
def read_data(filename):
        f = open(filename, 'r')
        line = f.readline()
        while line:
                y_vec.append(float(line))
                line = f.readline()
 
        return len(y_vec)
 
n = read_data("random200.txt")
 
for i in y_vec:
        print i
 
print "#data =", n

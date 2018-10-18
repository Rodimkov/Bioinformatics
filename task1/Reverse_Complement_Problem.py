# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:54:06 2018

@author: Yuri
"""

tmp = 'AGCT'
string = input()

for i in range(len(string)):
    for j in range(4):
        if tmp[j] == string[i]:
            string = string[:i] + tmp[3 - j] + string[i+1:]
            break
			
st = string[::-1]
print(st)
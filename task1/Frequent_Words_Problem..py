# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:00:17 2018

@author: Yuri
"""

string = input()
n = int(input())
k_mers = []
frequent_max = -1

for i in range(len(string) - n + 1):
    frequent = 0
    tmp = string[i: i + n]
	
    for j in range(i + 1, len(string) - n + 1):
        if string[j: j + n] == tmp:
            frequent += 1	
	
    if frequent == frequent_max:
        k_mers.append(tmp)
	
    if frequent > frequent_max:
        frequent_max = frequent
        k_mers.clear()
        k_mers.append(tmp)

for i in k_mers:	
	print(i, end=" ")
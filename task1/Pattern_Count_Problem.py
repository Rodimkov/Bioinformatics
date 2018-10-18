# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:58:11 2018

@author: Yuri
"""

pattern = input()
genome = input()

count = 0

for i in range(len(genome)  - len(pattern) + 1):
	if genome[i:i + len(pattern)] == pattern:
		count += 1

print(count)
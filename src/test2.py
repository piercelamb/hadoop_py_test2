'''
Created on Oct 29, 2014

@author: Pierce Lamb
'''
f = open('keyvalue.txt', 'r')

oldAsset = ""

for line in f:
    if line == '\n':
        continue
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    asset, count = data_mapped
    
    if 

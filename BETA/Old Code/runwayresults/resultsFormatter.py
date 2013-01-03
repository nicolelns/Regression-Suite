#! /usr/bin/python
import sys
import re


f = open('deletemelater.txt', 'r').readlines()
g = open('resultsFormatted.txt', 'w')
r = 0
results = {}
for line in f:
    
    if r % 2 == 0:
        line1 = line.strip('\n')
        #print line1, "LINE1" 
    else:
        line2 = line.strip('\n')
        #print line2, "LINE2"
        concatenate = line1 + line2
        #print concatenate, "CONCAT"
        results[concatenate] = r
#    try:
#        if r % 2 == 0:
#            print r, "R IN TRY"
#    except:
#        print line1 + line2, "CONCATENATE"
#        results[line1 + line2] = r

    r += 1
#print results
#print r, "R"
#print line1, "LINE1"
#print line2, "LINE2"
print len(results), "LEN RESULTS"
print len(f), "LEN F"

rk = results.keys()
#print rk

for item in rk:
    g.write(item)
    g.write('\n')
g.close()

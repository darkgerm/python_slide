#!/usr/bin/env python3
import re

table = {}

#Dec 21 17:07:08 nat235 pure-ftpd: (?@192.168.0.15) [INFO] ioi32 is now logged in
for line in open('xferlog', errors='ignore'):
    if 'logged' not in line: continue
    
    cols = line.split(' ')
    ip, user = cols[5][3:-1], cols[7]
    
    if ip not in table:         table[ip] = [user]
    elif user not in table[ip]: table[ip] += [user]
    else:                       pass        # do not add again

for key, value in sorted(table.items()):
    print('{:20s} {}'.format(key, value))


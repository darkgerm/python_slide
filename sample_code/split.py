#!/usr/bin/env python3

pass_f = open('/etc/passwd')

for line in pass_f:
    if line.strip()[0] == '#': continue
    arr = line.split(':')
    if len(arr) < 2: continue
    print('username = {:<10} uid = {}'.format(arr[0], arr[2]))

pass_f.close()


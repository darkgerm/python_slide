#!/usr/bin/env python3
import re
import subprocess as sp

cmd = 'ping -c 5 linux1.cs.nctu.edu.tw | tail -n +2 | head -n 5'

ping_rst_bytes = sp.check_output(cmd, shell=True)
ping_rst = ping_rst_bytes.decode()

times = []
for line in ping_rst.split('\n'):
    reobj = re.search('time=(\d*\.\d*) ms', line)
    if reobj:
        times.append(float(reobj.group(1)))

print('sum = {:.3f} ms'.format(sum(times)))
print('max = {:.3f} ms'.format(max(times)))
print('min = {:.3f} ms'.format(min(times)))


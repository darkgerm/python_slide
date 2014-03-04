#!/usr/bin/env python3
import re
from urllib.request import urlopen

url = 'https://www.esolutions.se/whatsmyinfo'
pattern = '<div class="col-md-8">(\d+\.\d+\.\d+\.\d+)</div>'

content = urlopen(url).read().decode()
reobj = re.search(pattern, content)
if reobj:
    print('my ip: {}'.format(reobj.group(1)))
else:
    print('cannot find your ip QQ.')


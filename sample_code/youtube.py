#!/usr/bin/env python3
import os
import re
import sys
from urllib.request import urlopen
from urllib.parse import quote

sys.path.append(os.path.abspath('./beautifulsoup4-4.3.2'))
from bs4 import BeautifulSoup

def youtube_search(keyword, n=6):
    url_fmt = (
        'http://www.youtube.com/results'
        '?hl=en&search_query={}'
    )
    url = url_fmt.format(quote(keyword))
    
    content = urlopen(url).read().decode()
    html = BeautifulSoup(content)
    
    base = 'http://www.youtube.com'
    for link in html.find_all(href=re.compile("watch\?v=")):
        if 'Watch Later' not in str(link):
            print(base + link.get('href'))
            print(link.text.strip())
            print()
            n -= 1
            if n == 0: break
    

def main1():
    import getopt
    
    def usage():
        print('Usage: %s [-n N] keyword.' % sys.argv[0])
        exit(1)
        
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'n:')
        
    except getopt.GetoptError as err:
        usage()
        
    if len(args) != 1: usage()
    
    n = 6
    for opt, arg in opts:
        if opt == '-n': n = int(arg)
        
    youtube_search(args[0], n=n)


def main2():
    import argparse
    parser = argparse.ArgumentParser(
            description='Youtube search engine.'
    )
    parser.add_argument('-n', type=int, default=6,
            help='number of search result. default is 6.')
    parser.add_argument(
            'keyword', nargs=1,
            help='keyword to search.'
    )
    args = parser.parse_args()
    
    youtube_search(args.keyword[0], n=args.n)


if __name__ == '__main__':
    main2()


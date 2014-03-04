#!/usr/bin/env python3
"""Check the input is a vaild id or not."""
import re

table = dict(
    A=10, J=18, S=26,  
    B=11, K=19, T=27,  
    C=12, L=20, U=28,  
    D=13, M=21, V=29,  
    E=14, N=22, W=32,  
    F=15, O=35, X=30,  
    G=16, P=23, Y=31,  
    H=17, Q=24, Z=33,  
    I=34, R=25,
)

def check(id_):
    digit = table[id_[0]]
    cks = digit // 10 + digit % 10 * 9
    cks += sum(int(id_[i]) * (9-i) for i in range(1, 9))
    cks += int(id_[9])
    return cks % 10 == 0


# Alternative check.
def check2(id_):
    cks = int('10987654932210898765431320'[ord(id_[0]) - ord('A')])
    cks += sum(int(id_[i]) * (9-i) for i in range(1, 9))
    cks += int(id_[9])
    return cks % 10 == 0


if __name__ == '__main__':
    while True:
        id_ = input('please input id: ')
        
        if not re.search('^[A-Z]\d{9}$', id_):
            print('wrong format!')
            
        elif check(id_):
            print('valid')
        
        else:
            print('invalid')


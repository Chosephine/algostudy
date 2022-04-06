# boj2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941
# 백준은 왜 아래 import 가 없으면 틀리는 것인가....

import sys
input=sys.stdin.readline


words = input()
n = len(words)
m = cnt = 0
while m < n-1:
    cnt += 1
    if words[m] == 'c':
        if words[m+1] in ('-', '='):
            m += 2
            continue
    elif words[m] == 'd':
        if words[m+1] == '-':
            m += 2
            continue
        elif words[m+1] == 'z':
            if words[m+2] == '=':
                m += 3
                continue
    elif words[m] == 'l':
        if words[m+1] == 'j':
            m += 2
            continue
    elif words[m] == 'n':
        if words[m+1] == 'j':
            m += 2
            continue
    elif words[m] == 's':
        if words[m+1] == '=':
            m += 2
            continue
    elif words[m] == 'z':
        if words[m+1] == '=':
            m += 2
            continue
    m += 1

print(cnt)
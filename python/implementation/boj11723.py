# 백준 11723 집합
# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline

# S: 공집합, ALL: 모든 숫자가 있을 때 비트
S = 0
ALL = (1 << 20) - 1 # 1111...1(2), 20자리 이진수

def pr_add(s: int, x: int):
    # 이진수에서 x 자리 숫자를 1로 만들기 위해선 x-1 만큼 shift 해야 함
    # | (OR) 은 둘 중 하나라도 1이면 1
    return (1 << (x-1)) | s

def pr_remove(s: int, x: int):
    # & (AND) 는 둘 모두가 1이어야 1 => 빼려는 숫자만 0이고, 나머지는 1이기만 하면 나머지에 영향 안미침
    # x가 3일 때 : (1 << (x-1)) 은 100(2), ~하면 011(2)
    # S가 0이면 결과는 000 & 011 => 000
    return s & ~(1 << (x-1))

def pr_check(s: int, x: int):
    # x가 3일 때 : (1 << (x-1)) 은 100(2)
    # S가 0이면 결과는 000 & 100 => 0
    if (1 << (x-1)) & s:
        return 1
    else:
        return 0

def pr_toggle(s: int, x: int):
    # ^ (XOR) 은 둘 중 하나만 1이어야 1
    # x가 3일 때 : (1 << (x-1)) 은 100(2)
    # S가 0이면 결과는 000 ^ 100 => 100 이고, 100 ^ 100 => 000
    return s ^ (1 << (x-1))

def pr_all(s: int):
    return ALL

def pr_empty(s: int):
    return 0


TC = int(input())

for _ in range(TC):
    cmd = input().split()

    # all, empty 가 먼저 있는 이유: 메모리 초과 방지
    if cmd[0] == 'all':
        S = pr_all(S)
    elif cmd[0] == 'empty':
        S = pr_empty(S)

    elif cmd[0] == 'add':
        S =pr_add(S, int(cmd[1]))
    elif cmd[0] == 'remove':
        S = pr_remove(S, int(cmd[1]))
    elif cmd[0] == 'check':
        print(pr_check(S, int(cmd[1])))
    elif cmd[0] == 'toggle':
        S = pr_toggle(S, int(cmd[1]))

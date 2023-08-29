# 백준 11723 집합
# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline

S = []
ALL = [_ for _ in range(1, 21)]

def pr_add(arr:list, x: int):
    arr.append(x)

def pr_remove(arr:list, x: int):
    if pr_check(arr, x):
        arr.remove(x)

def pr_check(arr: list, x: int):
    try:
        arr.index(x)
    except:
        return 0
    else:
        return 1

def pr_toggle(arr:list, x:int):
    if pr_check(arr, x):
        pr_remove(arr, x)
    else:
        pr_add(arr, x)

def pr_all(arr:list):
    arr = ALL

def pr_empty(arr:list):
    arr = []

# debug_chk = 0

TC = int(input())

for _ in range(TC):
    cmd = input().split()
    if cmd[0] == 'all':
        pr_all(S)
    elif cmd[0] == 'empty':
        pr_empty(S)
    elif cmd[0] == 'add':
        pr_add(S, int(cmd[1]))
    elif cmd[0] == 'remove':
        pr_remove(S, int(cmd[1]))
    elif cmd[0] == 'check':
        print(pr_check(S, int(cmd[1])))
        # debug_chk += 1
        # print(_, debug_chk, S, cmd)
    elif cmd[0] == 'toggle':
        pr_toggle(S, int(cmd[1]))


# print(f"call of check: {debug_chk}")
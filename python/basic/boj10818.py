# boj10818 최소, 최대
# https://www.acmicpc.net/problem/10818

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))
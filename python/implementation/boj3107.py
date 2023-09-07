# 백준 3107 IPv6
# https://www.acmicpc.net/problem/3107

import sys
input = sys.stdin.readline

abbr = input().strip()
abbrArray = abbr.split(":")
# print(abbrArray)

answer = ["" for _ in range(8)]

while len(abbrArray) > 8:
    abbrArray.remove("")

idx = 0
for group in abbrArray:
    if group:
        answer[idx] = group
    idx += 1

for i in range(8):
    if answer[-1] == "":
        answer.insert(answer.index(""), "")
        answer.pop(-1)

for i in range(8):
    while len(answer[i]) < 4:
        answer[i] = "0" + answer[i]

print(":".join(answer))

# 25:09:1985:aa:091:4846:374:bb
# 2001:db8:85a3::8a2e:370:7334
# ::1
# 1::
# 1::1
# 1:1::1
# ::1:2:3:4:5:6:7
# 1:2:3::4:5:6:7



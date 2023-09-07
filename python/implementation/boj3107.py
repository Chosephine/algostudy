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

# 아래 코드는 ChatGPT 가 최적화 해준 코드!

# import sys
#
#
# def expand_ipv6(abbr):
#     # If the address uses the :: shorthand
#     if "::" in abbr:
#         prefix, suffix = abbr.split("::")
#         prefix_groups = prefix.split(":") if prefix else []
#         suffix_groups = suffix.split(":") if suffix else []
#
#         missing_groups = 8 - len(prefix_groups) - len(suffix_groups)
#         middle = ["0000"] * missing_groups
#
#         groups = prefix_groups + middle + suffix_groups
#     else:
#         groups = abbr.split(":")
#
#     # Filling each group with leading zeroes until they have 4 characters
#     for i in range(8):
#         while len(groups[i]) < 4:
#             groups[i] = "0" + groups[i]
#
#     return ":".join(groups)
#
#
# # Sample test
# abbr = sys.stdin.readline().strip()
# print(expand_ipv6(abbr))
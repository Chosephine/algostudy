S = input()
nums = '0123456789'
new_S = list()
cnt = 0
for s in S:
    if s in nums:
        cnt += int(s)
    else:
        new_S.append(s)
new_S.sort()

print(''.join(new_S) + str(cnt))

# K1KA5CB7
# AJKDLSI412K4JSJ9D
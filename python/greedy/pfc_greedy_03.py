# baekjoon1439

def stoi(s):
    if s == '0':
        return 0
    if s == '1':
        return 1

S = input()
cnt = [0] * 2

for i in range(len(S)):
    if i == 0:
        cnt[stoi(S[i])] = 1
    else:
        if S[i-1] != S[i]:
            cnt[stoi(S[i])] += 1

print(min(cnt))

# import sys
# sys.stdin = open('3.txt')

wavedata = [0] * 101

def wave(n):
    if n < 4:
        return 1
    elif n < 6:
        return 2
    if wavedata[n] == 0:
        wavedata[n] = wave(n-1) + wave(n-5)
    return wavedata[n]

T = int(input())

for _ in range(T):
    print(wave(int(input())))

# print(wave(70))
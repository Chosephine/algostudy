import sys
sys.stdin = open('1.txt')

C = int(input())
for c in range(1, C+1):
    arr = list(map(int,input().split()))
    N = arr[0]
    SUM = 0
    for i in range(1, len(arr)):
        SUM += arr[i]
    AVG = SUM / N
    cnt = 0
    for j in range(1, len(arr)):
        if arr[j] > AVG:
            cnt += 1
    print('{:.3f}%'.format((cnt/N)*100))


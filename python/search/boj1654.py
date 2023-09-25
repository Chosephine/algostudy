# 백준 1654 랜선 자르기
# https://www.acmicpc.net/problem/1654

# 이분 탐색처럼 풀어야 할 것 같은 느낌은 들었지만 도움이 필요했다ㅠㅠ

# 1st 채점 시간: 552ms
# 2nd 채점 시간: 100ms (input 만 sys.stdin.readline 으로 바꿨을 때 ㅋㅋ;;)

K, N = map(int, input().split(' '))
have = [int(input()) for _ in range(K)]

start = 1
end = max(have)
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(K):
        cnt += have[i] // mid

    if cnt < N:
        end = mid - 1

    elif cnt >= N:
        answer = max(answer, mid)
        start = mid + 1

print(answer)
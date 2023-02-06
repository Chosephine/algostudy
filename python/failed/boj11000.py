import heapq
N = int(input())
stack = [[] for _ in range(N)]
# print(stack)
for n in range(N):
    S, T = map(int, input().split())
    for r in range(N):
        if not stack[r]:
            heapq.heappush(stack[r], -S)
            heapq.heappush(stack[r], -T)
            break
        else:
            end = heapq.heappop(stack[r])
            end *= -1
            if end <= S:
                heapq.heappush(stack[r], -S)
                heapq.heappush(stack[r], -T)
                break
            else:
                stack[r].append(-end)
cnt = 0
for s in range(N):
    if stack[s]:
        cnt += 1
    else:
        break
print(cnt)
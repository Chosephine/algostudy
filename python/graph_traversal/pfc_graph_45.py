# 이코테 45 최종 순위
# https://www.acmicpc.net/problem/3665

import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())

for t in range(TC):

    N = int(input())
    T = list(map(int, input().split()))

    # 유향 그래프 (idx 0 들은 버림)
    graph = [[False] * (N + 1) for _ in range(N+1)]

    # 진입 차수(idx 0 들은 버림)
    degree = [0] * (N + 1)

    for i in range(N):
        for j in range(i + 1, N):
            # T[j] 는 T[i] 를 바라봄
            graph[T[j]][T[i]] = True
            degree[T[i]] += 1


    M = int(input())
    for m in range(M):
        a, b = map(int, input().split())
        if graph[a][b]:
            # a -> b인 상황
            degree[a] += 1
            degree[b] -= 1
        else:
            # b -> a인 상황
            degree[b] += 1
            degree[a] -= 1

        graph[a][b] = not graph[a][b]
        graph[b][a] = not graph[b][a]


    # 위상 정렬을 위한 queue 생성
    d = deque()

    # 차수가 0 인 노드 큐에 삽입
    for i in range(1, N+1):
        if not degree[i]:
            d.append(i)

    # 정답을 위한 list 생성
    answer = []

    # flag 설정
    # certainty: IMPOSSIBLE, cycle: ?
    certainty = True
    cycle = False

    # 만약 차수가 0 인 노드가 없다면 순위를 결정할 수 없음
    if not d:
        certainty = False

    while d:
        # 큐에 삽입된 노드 빼서 answer 에 추가
        turn = d.popleft()
        answer.append(turn)

        # turn 에서 갈 수 있는 노드 차수 빼기
        for node in range(1, N+1):
            if graph[turn][node]:
                degree[node] -= 1

        # 방문하지 않은 노드 중에 차수가 0인 노드가 있다면 큐에 삽입
        for i in range(1, N+1):
            if not degree[i] and i not in answer:
                d.append(i)

        # answer에 모든 노드가 추가되기 전에 큐에 새로 추가된 노드가 없다면 -> IMPOSSIBLE
        # 큐에 두개 이상의 노드가 추가되면 cycle 발생으로 순위 확정 불가 -> ?
        if len(d) == 0 and len(answer) != N:
            certainty = False
            break
        elif len(d) > 1:
            cycle = True
            break

    if not certainty:
        print("IMPOSSIBLE")
    elif cycle:
        print("?")
    else:
        for a in answer[::-1]:
            print(a, end=" ")
        print()




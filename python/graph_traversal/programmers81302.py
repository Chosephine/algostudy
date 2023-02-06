# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque

dr, dc = [-1, 0, 1, 0],[0, 1, 0, -1]

def bfs(place, r, c):
    visited = deque()
    q = deque()
    q.append((r, c, 0))
    result = 1
    while q:
        cr, cc, cnt = q.popleft()
        visited.append((cr, cc))
        if cnt >= 3:
            break
        else:
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P' and (nr, nc) not in visited:
                    if cnt == 2:
                        continue
                    else:
                        result = 0
                        break
                elif 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'O' and (nr, nc) not in visited:
                    q.append((nr, nc, cnt+1))
    return result


def solution(places):
    answer = []
    for place in places:
        print(place)
        people = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    people.append((r, c))
        if not people:
            answer.append(1)
            continue
        else:
            result = 1
            while people:
                sr, sc = people.pop()
                if not bfs(place, sr, sc):
                    result = 0
                    break
            answer.append(result)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/60061
# 이코테 12, 프로그래머스 60061 기둥과 보 설치

def solution(n, build_frame):
    wall = [[0] * (n + 1) for _ in range(n+1)]
    # 기둥은 1, 보는 2
    for frame in build_frame:
        frame_x, frame_y, frame_type, build = frame
        if build:
            if frame_type == 0:
                if 5 - frame_y == 0 or wall[4 - frame_y]:
                    wall[5 - frame_y][frame_x] = 1
            else:
                if wall[5 - frame_y]
            pass
        else:
            pass
    answer = [[]]
    return wall


a = solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
print(a)
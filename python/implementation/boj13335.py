# 백준 13335 트럭
# https://www.acmicpc.net/problem/13335

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    # n: 트럭 대수, w: 다리 길이, L: 다리 하중
    # trucks: 개별 트럭의 무게
    n, w, L = map(int, input().split())
    trucks = list(map(int, input().split()))

    # used_truck: 진입한 트럭 표시
    # bridge: 다리 위의 트럭
    used_truck = [0] * n
    bridge = [0] * w

    # answer: 출력할 정답
    # waiting_truck_idx: 다리 앞에서 대기 중인 트럭의 idx
    answer = 0
    waiting_truck_idx = 0
    while True:
        # weight_of_bridge: 다리 위 하중
        weight_of_bridge = sum(bridge)

        # 종료조건: 모든 트럭이 진입했고, 다리 위에 아무 트럭도 없을 때
        if used_truck[n-1] and not weight_of_bridge:
            break

        # 1초가 흐르고, 트럭들이 이동함
        answer += 1
        weight_of_bridge -= bridge[w - 1]
        for i in range(w-2, -1, -1):
            bridge[i+1] = bridge[i]
        bridge[0] = 0

        # 대기 중인 트럭이 올라와도 다리 위 하중이 버틸 수 있다면 진입
        if waiting_truck_idx < n and weight_of_bridge + trucks[waiting_truck_idx] <= L:
            bridge[0] += trucks[waiting_truck_idx]
            used_truck[waiting_truck_idx] = 1
            waiting_truck_idx += 1

    print(answer)


# deque 로 시뮬레이션 한 코드들이 오히려 시간은 줄어들었음
# q.popleft(), q.append() 하는 과정들..!
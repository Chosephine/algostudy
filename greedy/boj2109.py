n = int(input())  # n = 0인 악랄한 인풋이 채점 100%대에 있읍니다^^
if n != 0:
    requests = [list(map(int, input().split())) for _ in range(n)]
    # 기한이 긴 순서대로 requests 정렬
    requests.sort(key=lambda x: -x[1])

    # request 할당할 work 배열 생성(리스트 길이는 최대 d)
    # 이미 할당한 request 를 체크 하기 위한 used 배열 생성
    work_n = max(requests[x][1] for x in range(n))
    work = [0] * (work_n + 1)  # 이거 안 쓰였네요.....
    used = [0] * n
    fee = 0

    # 가장 기한이 긴 것부터 할당 시작
    for i in range(work_n, 0, -1):
        # 들어갈 수 있는 후보를 담을 배열
        candidates = []

        # 후보 찾기
        for j in range(n):
            if requests[j][1] >= i:
                if not used[j]:
                    candidates.append((requests[j][0], j))
            # 기한 큰 순서대로 정렬했기 때문에 위 조건에 맞지 않으면 promising 하지 않음
            else:
                break

        # 후보 중 가장 돈 많이 주는 request를 할당하기
        max_p = idx = 0
        for k in range(len(candidates)):
            if candidates[k][0] > max_p:
                max_p = candidates[k][0]
                idx = candidates[k][1]
        fee += max_p
        used[idx] = 1

    print(fee)
else:
    print(0)
# 2020 카카오 인턴십: 키패드 누르기
# https://www.notion.so/55656a254b0741c39384c5d5cdb9e4bb

def solution(numbers, hand):
    L = len(numbers)
    result = [0] * L
    # 굳이 2차원 배열을 만들 필요는 없을 것 같아서 그냥 dictionary 에 좌표 저장!
    pad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    # 현재 왼손, 오른손 위치 (좌표로 저장 하는 이유는, 거리를 계산 해야 하니까!)
    cL, cR = (3, 0), (3, 2)
    lst_L, lst_R = [1, 4, 7], [3, 6, 9]  # 매번 리스트 만들면 시간 잡아 먹을 것 같아서 객체로 ^_^

    for i in range(L):  # numbers 의 각 index 를 돌면서
        if numbers[i] in lst_L:  # 왼손만 갈 수 있으면
            cL = pad[numbers[i]]  # 현재 왼손 위치 바꿔 주고
            result[i] = 'L'  # 왼손이 간다는 걸 result list 에 표시
        elif numbers[i] in lst_R:  # 오른손만 갈 수 있으면(이하 동문)
            cR = pad[numbers[i]]
            result[i] = 'R'
        else:  # 2, 5, 8, 0 이라면
            cr, cc = pad[numbers[i]]  # 좌표를 활용해 거리를 계산 해서
            dL = abs(cL[0]-cr) + abs(cL[1] - cc)
            dR = abs(cR[0]-cr) + abs(cR[1] - cc)
            if dL < dR:  # 왼손이 가까우면 왼손이 누르고
                cL = pad[numbers[i]]
                result[i] = 'L'
            elif dL > dR:  # 오른손이 가까우면 오른손이 누르고
                cR = pad[numbers[i]]
                result[i] = 'R'
            else:  # 두 손의 거리가 같으면 왼손잡이/오른손잡이 체크 해서 손 정해주기
                if hand == 'left':
                    cL = pad[numbers[i]]
                    result[i] = 'L'
                else:
                    cR = pad[numbers[i]]
                    result[i] = 'R'
    return ''.join(result)  # join 을 잘 안 써버릇해서 이번엔 써 보았읍니다 ^_^

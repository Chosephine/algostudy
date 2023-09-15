# 백준 1157 단어 공부
# https://www.acmicpc.net/problem/1157

word = input()

# A: ASCII 65, idx 0
# ASCII 코드를 활용할 예정, 카운트 정보를 담을 배열 생성
count = [0] * 26

# 입력 받은 word 대문자로 변환
upper_word = word.upper()

# upper_word 를 순회하며
# 1) 알파벳 갯수 세면서  2) max 정보 갱신
max_cnt = 0
for char in upper_word:
    # 해당 알파벳 index ASCII 코드 활용하여 찾기
    i = ord(char) - 65
    count[i] += 1

    # max_count 정보 갱신
    if count[i] > max_cnt:
        max_cnt = count[i]

# answer 정답을 담을 변수
# 초기값을 False 로 둬서 조건문 대응
answer = False
# count 배열의 index 는 0 ~ 25
for i in range(26):
    if count[i] == max_cnt:
        # 만약 answer 에 False 가 아닌 값이 있다면 True 로 반환될 것
        # 그 말은 max_cnt 를 가진 알파벳이 여러개 라는 것
        if answer:
            answer = '?'
            # 더 순회할 필요가 없음
            break
        # max_cnt 애 대응하는 값이 없었다면 False 인 상태 그대로
        # answer 갱신
        else:
            answer = chr(65 + i)

print(answer)
# 백준 10820 문자열 분석
# https://www.acmicpc.net/problem/10820

def count_category(string:str)->list:
    # 소문자, 대문자, 숫자, 공백 갯수 순서
    categorized = [0, 0, 0, 0]

    for s in string:
        if s.islower():
            categorized[0] += 1
        elif s.isupper():
            categorized[1] += 1
        elif s.isdigit():
            categorized[2] += 1
        else:
            categorized[3] += 1
    return categorized


if __name__ == "__main__":
    # 이 부분은 IDE에서 테스트하기 위한 part
    # import sys
    # sys.stdin = open("input.txt", "r")

    # TC 갯수가 입력되지 않으므로 에러 핸들링 필요
    while True:
        try:
            target = input()

            answer = count_category(target)

            # list 에 공백 넣어서 출력 할 때 ' '.join( list ) 사용
            # join할 때 숫자형 있으면 에러나므로 문자열로 변환
            print(' '.join(map(str, answer)))

        except EOFError:
            break



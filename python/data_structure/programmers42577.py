# 프로그래머스 42577 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577


# 정확성 83.3 / 효율성 0.0
def solution1(phone_book):
    # 한 번호가 다른 번호의 접두어인 경우가 있으면 False, 없으면 True
    phone_book.sort(key=lambda x: len(x))

    answer = True

    page = len(phone_book)
    for i in range(page):
        l = len(phone_book[i])
        for j in range(i + 1, page):
            if phone_book[j][:l] == phone_book[i]:
                answer = False
                break

    return answer

# 정확성 83.3 / 효율성 8.3
def solution2(phone_book):
    phone_book.sort(key=lambda x: len(x))

    answer = True

    page = len(phone_book)
    for i in range(page):
        l = len(phone_book[i])
        for j in range(i + 1, page):
            if phone_book[j][:l] == phone_book[i]:
                return False

    return answer

# 정확성 83.3 / 효율성 16.7
def solution3(phone_book):
    # 사전식으로 정렬해서 바로 뒤에 있는 번호와 비교하기
    phone_book.sort()

    answer = True

    page = len(phone_book)
    for i in range(page - 1):
        l = len(phone_book[i])

        if phone_book[i] == phone_book[i + 1][:l]:
            return False

    return answer
# https://www.acmicpc.net/problem/10825
# 이코테 기출 23, 백준 10825

# from operator import itemgetter
#
# def multisort(xs, specs):
#     for key, reverse in reversed(specs):
#         xs.sort(key=itemgetter(key), reverse=reverse)
#     return xs


# test = [('ABC', 5, 5, 5), ('ABc', 5, 5, 5)]
# multisort(test, ((1, True), (2, False), (3, True), (0, False)))
#
# print(test)

N = int(input())
# (이름, 국어, 영어, 수학)
students = []
for _ in range(N):
    name, k, e, m = input().split()
    students.append((name, int(k), int(e), int(m)))

# multisort(students, ((1, True), (2, False), (3, True), (0, False)))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])

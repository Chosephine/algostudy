# 백준 4195 친구 네트워크
# https://www.acmicpc.net/problem/4195

import sys

input = sys.stdin.readline

def find(node):
    # 주석된 부분 때문에 시간 초과 생김..ㅇㅅㅇ;
    # answer = node
    # while relations[answer] != answer:
    #     answer = relations[answer]
    if relations[node] != node:
        relations[node] = find(relations[node])
    return relations[node]

def union(node1, node2):
    root1 = find(node1)
    num1 = numbers[root1]

    root2 = find(node2)
    num2 = numbers[root2]

    if root1 != root2:
        relations[root2] = root1
        numbers[root1] = num1 + num2

    return numbers[root1]


N = int(input().strip())

for TC in range(N):
    relations = {}
    numbers = {}

    rel_num = int(input().strip())

    for _ in range(rel_num):
        A, B = input().strip().split()

        if A not in relations:
            relations[A] = A
            numbers[A] = 1

        if B not in relations:
            relations[B] = B
            numbers[B] = 1

        print(union(A, B))



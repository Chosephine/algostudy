N, M = map(int, input().split())

arr = [_ for _ in range(1, N+1)]
stack = [0 for _ in range(M)]


def permutation(top):
    # 기저부 : stack 다 차면 멈춰!
    if top == M-1:
        return print(*stack)

    # 실행부
    for n in arr:
        if n not in stack:
            top += 1
            stack[top] = n
            permutation(top)
            stack[top] = 0
            top -= 1


permutation(-1)



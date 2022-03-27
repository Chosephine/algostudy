import sys
sys.stdin = open('input.txt')

# a = [1, 2, 3]
# b = [4, 5]
# a.insert(1, b)  # [1, 4, 2, 3]
# a.pop(3)
# print(a)


for tc in range(1, 11):
    N = int(input())
    passwords = list(input().split())
    M = int(input())
    orders = list(input().split())
    L = len(orders)

    for i in range(L):
        if orders[i] == 'D':
            # i+1 : x, i+2: y
            x = int(orders[i + 1])
            y = int(orders[i + 2])
            for z in range(y):
                passwords.pop(x)

        elif orders[i] == 'I':
            # i+1 : x, i+2: y, i+2+1~: y1~
            x = int(orders[i + 1])
            y = int(orders[i + 2])
            for z in range(y):
                passwords.insert(x + z, orders[i + 3 + z])

    print(f'#{tc}', *passwords[:10])

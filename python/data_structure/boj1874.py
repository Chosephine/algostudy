# 백준 1874 스택수열
# https://www.acmicpc.net/problem/1874

# 계속 이왜안 하고 있었는데 오타 때문이었구나....^^
# 17% 에서 실패 뜨면 NO 답이 안나오는 것..ㅎ..

# n: 1 ~ n 이 대상
n = int(input().strip())

# arr: 검증하고자 하는 수열
arr = []
for _ in range(n):
    arr.append(int(input().strip()))

# start: stack에 넣을 숫자
stack = []
start = 1

# flag: 수열을 만들 수 없다면 True
flag = False

# answer: 연산자를 담을 리스트
answer = []

# 수열에서 처음부터 하나씩 빼면서 수열로 만들 수 있는지 확인
while arr:
    # target: 현재 arr 의 제일 처음에 있는 숫자
    target = arr.pop(0)

    # 스택에 넣을 start 가 target 보다 작거나 같으면 stack 에 target 까지는 넣어 줘야 함
    if start <= target:
        while start <= target:
            stack.append(start)
            answer.append('+')
            start += 1

        # start == target 일 테니까 수열을 만들기 위해 stack 에서 pop
        stack.pop()
        answer.append('-')

    # 스택에 넣을 start 가 target 보다 크면, 현재 stack 안에 있다는 것
    elif start > target:
        # 빼는 순간 수열에 포함되어야 하는 숫자임
        candidate = stack.pop()
        answer.append('-')

        # 근데 이 후보가 target이 아니라면, 수열 만들기 실패!
        if candidate != target:
            flag = True
            break

if flag:
    print('NO')

else:
    for operation in answer:
        print(operation)


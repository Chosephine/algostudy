# 백준 11720 숫자의 합
# https://www.acmicpc.net/problem/11720

N = int(input())

# 모든 문자열을 split 할 거라면 .split('') 같은 거 필요 없음
number = list(map(int, input()))

print(sum(number))
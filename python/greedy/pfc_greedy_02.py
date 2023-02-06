# S = '02984'
S = '567'
result = 0
for s in S:
    num = int(s)
    if num == 0 or result == 0: # 현재 값이 0이거나 대상 숫자(num)가 0이면 더해주기
        result += num
    elif num == 1: # 대상 숫자(num)가 1이면 곱하는게 의미 없으니까 더해주기
        result += num
    else: # 대상 숫자가 2 이상이면 곱하는게 훨씬 숫자 커짐
        result *= num
print(result)
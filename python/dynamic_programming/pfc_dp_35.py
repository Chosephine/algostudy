# 이코테 기출 35 못생긴 수
# Google 인터뷰 기출

# n번째 못생긴 수 찾기
n = int(input())

# 못생긴 수 list
ugly_nums = [0] * n
ugly_nums[0] = 1

# 2, 3, 5를 곱해줄 가장 작은 숫자의 idx
i2 = i3 = i5 = 0

# 못생긴 수 후보
next2, next3, next5 = 2, 3, 5

# 못생긴 수 찾기
for i in range(1, n):
    # 후보군 중에 최소인 수치
    ugly_nums[i] = min(next2, next3, next5)

    if ugly_nums[i] == next2:
        i2 += 1
        next2 = ugly_nums[i2] * 2
    if ugly_nums[i] == next3:
        # elif가 아니라 if를 써야 중복을 피할 수 있다..!!!
        i3 += 1
        next3 = ugly_nums[i3] * 3
    if ugly_nums[i] == next5:
        i5 += 1
        next5 = ugly_nums[i5] * 5

print(ugly_nums)
print(ugly_nums[n-1])

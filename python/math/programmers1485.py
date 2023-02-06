# programmers 찾아라 프로그래밍 마에스터 - 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

nums = [3, 3, 3, 2, 2, 2]
N = len(nums)
nums = set(nums)
if len(nums) >= N//2:
    result = N//2
else:
    result = len(nums)
print(result)
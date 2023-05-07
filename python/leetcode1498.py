# 리트코드 1498 Number of Subsequences That Satisfy the Given Sum Condition
import itertools

def numSubseq(nums: list[int], target: int) -> int:
    cnt = 0
    for i in range(1, len(nums)+1):
        subsets = itertools.combinations(nums, i)
        subsets_list = list(subsets)
        for subset in subsets_list:
            if min(subset) + max(subset) <= target:
                cnt += 1
    return cnt % (10**9 + 7)

print(numSubseq([2,3,3,4,6,7], 12))


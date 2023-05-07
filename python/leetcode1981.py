# 리트코드 1981 Minimize the Difference Between Target and Chosen Elements

def rowSum(mat, m, n, r, c, sum, target):
    if r == m - 1:
        return sum
    temp = 4900 + target
    for cc in range(n):
        s = rowSum(mat, m, n, r + 1, cc, sum + mat[r + 1][cc], target)
        if r != 0:
            return s
        else:
            if abs(s - target) < abs(temp - target):
                temp = s
    return temp

def minimizeTheDifference(mat: list[list[int]], target: int) -> int:
    # mat: mxn matrix
    m: int = len(mat)
    n: int = len(mat[0])

    mat_sum = 4900
    cr = 0

    for c in range(n):
        temp = rowSum(mat, m, n, 0, c, mat[0][c], target)
        if abs(temp - target) < abs(mat_sum - target):
            mat_sum = temp

    return abs(mat_sum - target)


print(minimizeTheDifference([[10,3,7,7,9,6,9,8,9,5],[1,1,6,8,6,7,7,9,3,9],[3,4,4,1,3,6,3,3,9,9],[6,9,9,3,8,7,9,6,10,6]], 5))

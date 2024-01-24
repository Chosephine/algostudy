# 백준 11053 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

# LIS 알고리즘(Longest Increasing Subsequenc)
# 나무위키 [최장 증가 부분 수열] 참고, O(n log n) 시간 복잡도 방법 사용
# n : 수열 A 탐색 / log n : 이분탐색

# 이분 탐색을 위한 함수
def binary_search(x: int, arr: list, start: int, end: int) -> int:
    mid = (start + end) // 2

    # arr[mid]가 x와 같다면 last_number 갱신값이 mid와 같아야 하므로 mid 반환
    if arr[mid] == x:
        return mid - 1

    # end - start 가 1이라면 해당 구간 이내에 x가 있다는 것이므로 start 반환
    if end - start == 1:
        return start

    # mid 보다 작을 땐 왼쪽 구간 재탐색, 클 땐 오른쪽 구간 재탐색
    if x < arr[mid] or not arr[mid]:
        return binary_search(x, arr, start, mid)
    else:
        return binary_search(x, arr, mid, end)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = [0] + list(map(int, input().split()))

    # length : 부분 수열 길이 (근데 이거 필요 없어서 삭제)
    # length = [_ for _ in range(N + 1)]

    # last_number : index 길이의 부분수열일 때 더 작은 숫자를 저장하는 배열
    last_number = [0] * (N + 1)

    # A 순회
    for i in range(1, N + 1):
        # 길이 1일 때 처리 (초기화)
        if i == 1:
            last_number[1] = A[1]

        # 길이 2 이상일 때
        # A[i]가 들어갈 수 있는 구간 이분탐색으로 찾은 후 -> longest_former_index
        # last_number[longest_former_index + 1] 갱신
        else:
            longest_former_index = binary_search(A[i], last_number, 0, N)

            if last_number[longest_former_index + 1] != 0:
                last_number[longest_former_index + 1] = min(last_number[longest_former_index + 1], A[i])
            else:
                last_number[longest_former_index + 1] = A[i]

    # last_number 순회하면서 최장 길이 출력
    for i in range(1, N + 1):
        if i == N and i != 0:
            print(i)

        if not last_number[i]:
            print(i - 1)
            break

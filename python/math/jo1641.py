n, m = map(int, input().split())
if n < 1 or n > 100 or n % 2 == 0 or m < 1 or m > 3:
    print('INPUT ERROR!')
else:
    arr = [[] for _ in range(n + 1)]
    if m == 1:
        end = n * ((n + 1) // 2)
        r = i = 1
        while i <= end:
            if r % 2:
                arr[r].append(i)
                i += 1
            else:
                arr[r] = [i] + arr[r]
                i += 1
            if len(arr[r]) == r:
                r += 1
    if m == 2:
        for r in range(1, n + 1):
            for _ in range(r - 1):
                arr[r].append(' ')
            for c in range(2 * (n - r + 1) - 1):
                arr[r].append(r - 1)

    if m == 3:
        for r in range(1, (n + 1) // 2 + 1):
            if r == (n + 1) // 2:
                for c in range(1, r + 1):
                    arr[r].append(c)
            else:
                for c in range(1, r + 1):
                    arr[r].append(c)
                    arr[n + 1 - r].append(c)

    for rr in range(1, n + 1):
        print(*arr[rr])

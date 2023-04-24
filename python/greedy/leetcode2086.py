# leetcode2086 Minimum Number of Food Buckets to Feed the Hamsters

def minimumBuckets(hamsters: str) -> int:
    hamsters = list(hamsters)
    print(hamsters)
    len_hamsters = len(hamsters)
    food = 0
    for i in range(len_hamsters):
        print(f"this turn: {i} index")
        if hamsters[i] == 'H':
            if 0 <= i - 1 < len_hamsters and hamsters[i-1] == 'F':
                continue
            elif 0 <= i + 1 < len_hamsters and hamsters[i+1] == '.':
                hamsters[i+1] = 'F'
                food += 1
            elif 0 <= i - 1 < len_hamsters and hamsters[i-1] == '.':
                hamsters[i - 1] = 'F'
                food += 1
            else:
                print(hamsters)
                return -1
        if hamsters[i] == 'F':
            continue
    return food


print(minimumBuckets(hamsters=".HHH."))

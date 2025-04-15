n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    total = a + b
    min_val = min(a, b)

    if total % 3 == 0 and max(a, b) <= 2 * min_val:
        print("YES")
    else:
        print("NO")

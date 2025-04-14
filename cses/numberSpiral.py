n=int(input())
queries=[]
for i in range(n):
    y,x=map(int,input().split())
    queries.append((y,x))
for y,x in queries:
    m=max(y,x)
    if m%2==0:
        ans = m * m - x + 1 if y == m else (m - 1) * (m - 1) + y
    else:
        ans = (m - 1) * (m - 1) + x if y == m else m * m - y + 1
    print(ans)



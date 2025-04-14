n=int(input())
a=list(map(int,input().split()))
moves=0
for i in range(n-1):
    if i+1<n and a[i]>a[i+1]:
        moves+=a[i]-a[i+1]
        a[i+1]=a[i]
print(moves)
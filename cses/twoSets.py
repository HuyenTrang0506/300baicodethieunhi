n=int(input())
sum1=0
po1=[]
sum2=0
po2=[]
for i in range(n,0,-1):
    if sum2<sum1:
        sum2+=i
        po2.append(i)
    else:
        sum1+=i
        po1.append(i)
if sum1==sum2:
    print("YES")
    print(len(po1))
    print(*po1)
    print(len(po2))
    print(*po2)
else:
    print("NO")

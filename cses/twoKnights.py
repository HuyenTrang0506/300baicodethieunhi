
n=int(input())
#CT tính tổ hợp n!/k!(n-k)!
#CT rút gọn n(n-1)/2
for i in range(1,n+1):
     result = i*i*(i*i-1)//2 - 4*(i-1)*(i-2)
     print(result)



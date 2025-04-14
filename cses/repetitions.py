s=str(input())
b=[1]*len(s)
for i in range(len(s)):
    if i+1<len(s) and s[i]==s[i+1]:
        b[i+1]=b[i]+1
print(max(b))


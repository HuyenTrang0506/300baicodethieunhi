n=int(input())
a=set(map(int,input().split()))#input array split by space
for i in range(1,n+1):
    if i not in a:
        print(i)
        break
#
# # Calculate the expected sum of the first n natural numbers
# expected_sum = n * (n + 1) // 2
#
# # Calculate the actual sum of the given numbers
# actual_sum = sum(a)
#
# # The missing number is the difference
# print(expected_sum - actual_sum)
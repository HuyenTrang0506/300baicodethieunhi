n = int(input())
count = 0
power_of_5 = 5

while n // power_of_5 > 0:
    count += n // power_of_5
    power_of_5 *= 5

print(count)

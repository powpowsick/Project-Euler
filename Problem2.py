m = 1
n = 2
sum = 2
while m < 4000001 and n < 4000001:
    k = m + n
    m = n
    n = k
    if n % 2 == 0:
        sum += n

print(sum)

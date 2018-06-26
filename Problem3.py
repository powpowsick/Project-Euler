def check_prime(x):
    y = 2
    while y < x/2:
        if x % y == 0:
            return False
        y += 1
    return True


n = 600851475143
div = 1
while div < n:
    if n % div == 0:
        if check_prime(n/div) == True:
            print(n/div)
            break
    div += 2

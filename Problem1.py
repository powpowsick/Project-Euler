counter = 1
sum = 0
while counter < 1000:
    if counter % 5 == 0 or counter % 3 == 0:
        sum += counter
    counter += 1

print(sum)

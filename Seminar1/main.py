E = 3
n = 100
sum = 0
count = 1
while count <= n:
    if count % 2 == 0 and count % E != 0:
        sum += count
    count += 1
print(sum)

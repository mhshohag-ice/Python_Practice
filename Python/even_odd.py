i = 1
j = 2
count = 0
sum1 = 0
sum2 = 0
while True:
    print(i, " ", j)
    sum1 = sum1 + i
    sum2 = sum2 + j
    i = i + 2
    j = j + 2
    count = count + 1
    if count < 50:
        continue
    else:
        break
print(sum1, sum2)

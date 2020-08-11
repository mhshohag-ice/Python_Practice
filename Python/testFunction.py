num = 0
sum = 0.0
while True:
    sval = input('Enter any integer number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input!")
        continue
    num = num + 1
    sum = sum + fval
print(sum, num, sum/num)

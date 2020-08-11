def computepay():
    hrs = input("Enter Hours:")
    rate = input("Enter rate:")
    try:
        h = float(hrs)
        rph = float(rate)
    except:
        print('Error! Enter a numeric number.')
        quit()
    if h < 41.0:
        pay = h * rph;
        return pay
        #print(pay)
    elif h > 40:
        #pay = (h * rph) + ((h-40)* 1.5)
        pay = (40 * rph) + ((h - 40) * rph * 1.5)
        return pay
    #print(pay)
print("Pay",computepay())

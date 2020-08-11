score = input("Enter Score: ")
try:
    i_score = float(score)
except:
    print('Error! Enter a numeric number.')
    quit()
if i_score > 0:
    if i_score <= 1.0:
        if i_score < 0.6:
            print("F")
        elif i_score >= 0.9:
            print("A")
        elif i_score >= 0.8:
            print("B")
        elif i_score >= 0.7:
            print("C")
        elif i_score >= 0.6:
            print("D")
    else:
        print("Out of range!")

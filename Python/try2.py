raw_in = input('Enter a number: ')
try:
    in_value = int(raw_in)
except:
    in_value = - 1

if in_value > 0:
    print('Nice work!')
else:
    print('Not a number')

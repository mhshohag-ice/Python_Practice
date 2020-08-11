handle = open('test.txt', encoding="utf8")

di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    print(words)
    for w in words:
        di[w] = di.get(w,0) + 1
#print(di)

largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print(theword,largest)

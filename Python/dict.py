counts = dict()
names = ['shohag', 'shafin', 'shohag', 'nahiyan', 'nafis']
#for name in names:
    #if name not in counts:
        #counts[name] = 1
    #else:
        #counts[name] = counts[name] + 1
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

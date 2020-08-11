#test_string = input("Enter the file name: ")
test_str = open('test.txt', encoding="utf8")
inp = test_str.read()

#for line in test_str:
    #print(line)
print(len(inp))
print(inp.upper())
print(inp.lower())

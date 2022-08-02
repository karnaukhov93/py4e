fname = input("Enter file name: ")
fh = open(fname)
lst = list()
word = None
for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

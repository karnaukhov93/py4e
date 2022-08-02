fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    if line.startswith("From ") is True:
        lst.append(line.split()[1])
count = len(lst)
for mail in lst:
    print(mail)
print("There were", count, "lines in the file with From as the first word")

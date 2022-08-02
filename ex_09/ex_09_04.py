name = input("Enter file: ")
fh = open(name)
counts = dict()

for st in fh :
    if len(st) is None :
        continue
    if st.startswith("From ") is True :
        word = st.split()[1]
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for k,v in counts.items() :
    if bigcount is None or v > bigcount :
        bigword = k
        bigcount = v
print(bigword, bigcount)

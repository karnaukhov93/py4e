fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        value = value + float(line[line.rfind(":")+1:].lstrip())
        count = count + 1
avg = value / count
print("Average spam confidence:", avg)

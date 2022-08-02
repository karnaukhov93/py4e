fname = input("Enter file name: ")
try:
    fn = open(fname)
except:
    print("File not found")
    quit()
print(fn.read().strip().upper())

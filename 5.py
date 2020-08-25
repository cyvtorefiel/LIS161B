fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()

for line in fhandle:
    print(line.strip().upper())

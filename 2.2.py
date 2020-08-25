fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()

count = 0

for line in fhandle:
    if line.startswith('From '):
        email = line.split()[1]
        count += 1
        print(email)

print("There are {num} lines in file: {fname}".format(num = count, fname = fname))

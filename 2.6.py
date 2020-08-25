fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()


emails = {}

for line in fhandle:
    if line.startswith('From '):
        email = line.split()[1]
        emails[email] = emails.get(emails, 0) + 1

print(emails)
